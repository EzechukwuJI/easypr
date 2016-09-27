from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.db.models import F
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from easypr_ng.models import *
from easypr_general.custom_functions import transaction_ref, get_random_code, paginate_list
# from easypr_ng.models import MediaHouse, MediaContact, PressMaterial, Redirect_url, Publication, PublicationImage, \
# Purchase, PayDetails, PurchaseInvoice, Bouquet, Sector, MediaPlatform, Comment, CommentReply

from easypr_ng.forms import ContentUploadForm, BizInfoForm, TargetAudienceForm
import datetime



# collect all economic sectors for a post
def get_sectors():
    post_sectors = Sector.objects.filter(active = True)
    return post_sectors


def get_recent_posts(post_count, order_by):
    recent_posts  =  Publication.objects.published_articles().order_by('-date_posted').order_by(order_by)[:post_count]
    return recent_posts


def  indexView(request):
    context = {}
    press_materials = ["features","press_release","interview","photo_news"]
    for cate in press_materials:
        search_str = cate.replace("_"," ")
        context[cate] = Bouquet.objects.filter(press_material__media_type = search_str)
        context['recent_posts'] = get_recent_posts(25,"?")
    return render(request, 'easypr_general/index.html', context)
    



def requestServiceView(request):
    return render(request, 'easypr_ng/request-a-service.html', {})





def ourWorksView(request):
    return render(request, 'easypr_ng/our-works.html', {})






def create_post(request, press_material):
    transaction_id = transaction_ref("publication", Publication)
    rp = request.POST
    title = rp['post_title']
    posted_by = request.user
    content = rp['post_body']
    person = rp['person_to_quote']
    position = rp['persons_position']
    platform = MediaPlatform.objects.get(pk = rp['platform'])
    sector = Sector.objects.get(pk = rp['sector'])
    press_material  =  PressMaterial.objects.get(name_slug = press_material)
    online = rp.get('publish_online', False)
    new_post = Publication.objects.create(transaction_id = transaction_id, post_title = title, post_body = content,person_to_quote = person, persons_position = position,
        posted_by = posted_by, platform = platform, sector = sector, publish_online = online, press_material = press_material)
    selected_media_houses = [ media for media in MediaHouse.objects.filter(pk__in = rp.getlist('selected_media[]'))]
    for media_pk    in  rp.getlist('selected_media[]'):
        media_house =   MediaHouse.objects.get(pk = media_pk )
        new_post.media_houses.add(media_house)
    new_post.save()

    for image in request.FILES.keys():
        pub_image = PublicationImage.objects.create(image = request.FILES[image], caption = request.POST["cap_"+ image], post = new_post)
        # new_post.pictures.add(pub_image)
    new_post.save()
    return new_post



def create_purchase_record(request, bouquet,publication):
    tr_id       =  transaction_ref("purchase", Purchase)
    pay_id      =  transaction_ref("payment",  PayDetails)
    pay_details =  PayDetails.objects.create(user = request.user, transaction_id = pay_id)

    new_purchase = Purchase.objects.create(user = request.user, transaction_id = tr_id, bouquet = bouquet,
        publication = publication, payment_details = pay_details)
    return new_purchase



@login_required()
def buy_packageView(request, press_material,package):
    form = ContentUploadForm()
    context                =   {}
    bouquet                =   get_object_or_404(Bouquet, name_slug = package, press_material = PressMaterial.objects.get(name_slug = press_material))
    template               =  'easypr_ng/content-upload.html'
    context['sectors']     =   Sector.objects.filter(active = True)
    context['platforms']   =   MediaPlatform.objects.filter(active = True)
    context['package']     =   bouquet

    if request.method == "POST":
        form = ContentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_post       =    create_post(request, press_material)
            new_purchase   =   create_purchase_record(request, bouquet, new_post)
            return redirect(reverse('easypr_ng:preview-content', kwargs={'transaction_id':new_post.transaction_id}))
        else:
            print form.errors
            context['form'] = ContentUploadForm(data = request.POST)
            context.update({'press_material':press_material, 'package':package})
            return render(request, template, context)
    context['form'] = ContentUploadForm()
    return render(request, template, context)






@login_required()
def previewPublicationView(request, **kwargs):
    # date_paid = datetime.datetime.strptime('2016-09-23', "%Y-%m-%d")
    # print "date paid", date_paid
    context = {}
    post = Publication.objects.get(transaction_id = kwargs['transaction_id'])
    return render(request, 'easypr_ng/content-preview.html', {'post':post})





@login_required()
def Payment(request, **kwargs):
    publication = get_object_or_404(Publication, transaction_id = kwargs['transaction_id'])
    purchase  = get_object_or_404(Purchase, publication = publication)
    if not publication.completed:
        template = 'easypr_ng/payment.html'
        return render(request, template, {'post':publication, 'purchase':purchase})
    else:
        request.session['post_id']       =   publication.pk
        request.session['purchase_id']   =   purchase.pk
        request.session['pay_info_id']   =   purchase.payment_details.pk
        return redirect(reverse('easypr_ng:confirmation'))





@login_required()
def savePayInfo(request, transaction_id):
    #  manual payment processing
    if request.method == "POST":
        rp = request.POST
        purchased  =   get_object_or_404(Purchase, transaction_id = transaction_id)
        pay_details = purchased.payment_details
        PayDetails.objects.filter(pk = pay_details.pk).update(payment_method = rp['method'].replace("_"," ").title(), 
            amount_paid = rp['amount'], date_paid = rp['date'], bank_name = rp['bank'], teller_number = rp['teller'])
        purchased.publication.ordered = True
        Publication.objects.filter(pk = purchased.publication.pk).update(completed = True)
        purchased.ordered = True
        purchased.save()
        return JsonResponse({'response': 'success'})
    else:
        # card payment processing - pending
        pass
   



def get_media_houses(request):
    media_platform  =   request.POST['media_platform']
    template        =  'snippets/media-options.html'
    platform        =   MediaPlatform.objects.filter(pk = media_platform)
    media_houses    =   MediaHouse.objects.filter(platform__icontains = platform)
    return render(request, template, {'available_media': media_houses})


@login_required()
def confirmationView(request):
    active_session_keys = ['post','purchase','pay_info']
    try:
        post         =   get_object_or_404(Publication, pk = request.session.get('post', ''))
        purchase     =   get_object_or_404(Purchase, pk = request.session.get('purchase', ''))
        pay_info     =   get_object_or_404(PayDetails, pk = request.session.get('pay_info', ''))
    except:
        post = purchase = pay_info = {}

    for key in request.session.keys():
        if key in active_session_keys:
            del request.session[key]
    return render(request, 'easypr_ng/confirmation.html', {'post':post,'purchase':purchase,'pay_info':pay_info})



def newsRoomView(request):
    context = {}
    template = 'easypr_general/newsroom.html'
    context['show_news_list'] = True
    context['show_news_details']   =  False

    published_articles       =  paginate_list(request, Publication.objects.published_articles().order_by('-date_posted'), 10)
    context['articles']      =  published_articles
    context['sectors']       =  get_sectors()
    context['recent_posts']  =  get_recent_posts(5,"-date_posted")
    return render(request, template, context)



def newsRoomCatView(request, **kwargs):
    context = {}
    template = 'easypr_general/newsroom.html'
    context['show_news_list'] = True
    context['show_news_details']   =  False
    context['sectors']   =  get_sectors()
    cat_article = paginate_list(request, Publication.objects.published_articles().filter(sector__name_slug = kwargs['category']).order_by('-date_posted'), 1)
    context['articles'] = cat_article
    context['recent_posts'] = get_recent_posts(5,"-date_posted")
    return render(request, template, context)







def  readnewsView(request, post_id, title_slug):
    context = {}
    context['post'] = get_object_or_404(Publication, title_slug = title_slug, pk = post_id)
    # context['post'] = Publication.objects.get(title_slug = title_slug, pk = post_id)
    context['show_news_details']   =  True
    context['show_news_list'] = False
    context['sectors']   =  get_sectors()
    context['recent_posts'] = get_recent_posts(5,"-date_posted")
    return render(request, 'easypr_general/newsroom.html', context)



@login_required()
def postCommentView(request):
    # print "saving comment"
    context  =   {}
    if request.user.is_authenticated:
        if request.method == "POST" and not request.POST['msg'] == "":
            rp = request.POST
            post = get_object_or_404(Publication, pk = rp['post_id'])
            new_comment = Comment.objects.create(post= post, comment = rp['msg'], posted_by = request.user, website=rp['website'])
            context['comment'] = new_comment
        return render(request, 'snippets/post-comments.html', context)
    else:
        return JsonResponse({'error_msg': 'you have to be logged in to comment.'})



# @login_required()
@csrf_exempt
def postCommentReplyView(request):
    if request.user.is_authenticated:
        context = {}
        if request.method == "POST" and not request.POST['msg'] == "":
            comment = get_object_or_404(Comment, pk = request.POST['comment_id'])
            new_reply = CommentReply.objects.create(comment = comment, posted_by = request.user, reply = request.POST['msg'])
            context['reply'] = new_reply
        return render(request, 'snippets/comment-replies.html', context)
    else:
        return JsonResponse({'response':"<a href="" class= 'text-danger'><strong>Kindly login to post your comment</strong></a>"})










@csrf_exempt
def strategyPlannerIntroView(request):
    if request.POST.has_key('start-strategy'):
        anon_userID = get_random_code(35).lower()
        new_strategy = PRStrategy.objects.create(anon_userID = anon_userID)
        request.session['strategy_in_session']   =  new_strategy.pk
        return redirect(reverse('easypr_ng:strategy-planner', kwargs={'step':1, 'anon_userID':anon_userID}))
    return render(request,'easypr_ng/strategy-planner-info.html', {})


def get_current_strategy(request):
    pk = request.session.get('strategy_in_session', "")
    try:
        return PRStrategy.objects.get(pk = pk)
    except:
        return None

# def validate_step_and_ID(request, step, ID):
#     print "validating entries . . ."
#     cstep = int(step)
#     total_steps = 7
#     if cstep <= 0 or cstep > total_steps:
#         message = "The page number your are trying to view does not exist"
#         return render(request, '404.html', {'response': message})
#     elif not PRStrategy.objects.filter(anon_userID = ID).exists():
#         link = '<a href="{% url "easypr_ng:strategy-planner-intro" %}"> Here </a>'
#         message = "No strategy creation in progress for this ID, you can start a new strategy " + link
#         return redirect(reverse('easypr_ng:strategy-planner-intro'))
#     else:
#         pass
    
def do_post_request(request, step, form):
    pass


def strategyPlannerView(request, step,  anon_userID):
    template = 'easypr_ng/strategy-planner.html'
    context = {}
    context['step'] = 1
    context['anon_userID'] = anon_userID
    context['form'] = BizInfoForm()
    context['caption'] = "This is the first step to your greatness - this is just a dummy string"

    current_strategy = get_current_strategy(request)
    # print "current strategy ", current_strategy
    step = int(step)
    total_steps = 7

    if step <= 0 or step > total_steps:
        message = "The page number your are trying to view does not exist"
        return render(request, '404.html', {'response': message})
    elif not PRStrategy.objects.filter(anon_userID = anon_userID).exists():
        message = "No strategy creation in progress for this ID, you can start a new strategy below."  
        messages.error(request, message)
        return redirect(reverse('easypr_ng:strategy-planner-intro'))

    
    if request.method == "POST": # and "submit_step_1"  in request.POST.keys():    
        if step == 1:
            # save selections from step 1
            # context values for nest step
            sectors = get_sectors()
            print "sectors  ", sectors
            next_caption = "We are creating a unique experience for you!"
            next_form = TargetAudienceForm()
            context.update({'step':2,'caption':next_caption, 'form':next_form,'sectors':sectors}) #for next form page

            # return redirect(reverse('easypr_ng:strategy-planner', kwargs=context))
                # save content       
        if step == 2:
            # save selections from step 2
            next_caption = "Your business is about to experience a great and phenomenal boost"
            next_form = object()

            context.update({'step':3, 'caption':step_caption, 'form':next_form})

    return render(request, template, context)














