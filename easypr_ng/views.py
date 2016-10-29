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
from easypr_general.models import ServiceCategory
# from easypr_ng.models import MediaHouse, MediaContact, PressMaterial, Redirect_url, Publication, PublicationImage, \
# Purchase, PayDetails, PurchaseInvoice, Bouquet, Sector, MediaPlatform, Comment, CommentReply

from easypr_ng.forms import ContentUploadForm, BizInfoForm, TargetAudienceForm,ServiceRequestForm
from easypr_general.models_field_choices import PR_FREQUENCY
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
    









def ourWorksView(request):
    return render(request, 'easypr_ng/our-works.html', {})






def create_post(request, press_material):
    transaction_id = transaction_ref("publication", Publication, 10)
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
    tr_id       =  transaction_ref("purchase", Purchase, 10)
    pay_id      =  transaction_ref("payment",  PayDetails, 10)
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
        return PRStrategy.objects.filter(pk = pk)
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


def validate_post_keys(request, keys_dict):
    rp = request.POST
    r_dict = {}
    for key in keys_dict.keys():
        # print "expected type: ", keys_dict[key][0]
        if rp.has_key(key):
            if keys_dict[key][0] == "unit":
                r_dict[key]  = rp[key]
            else:
                r_dict[key] = rp.getlist(key)
        else:
            r_dict[key] = keys_dict[key][1]
    return r_dict


def strategyPlannerView(request, step,  anon_userID):
    template = 'easypr_ng/strategy-planner.html'
    context = {}
    context['step'] = 1
    context['step_template'] = 'step_forms/step1.html'
    context['anon_userID'] = anon_userID
    context['form'] = BizInfoForm()
    context['caption'] = "This is the first step to your greatness - this is just a dummy string"

    current_strategy = get_current_strategy(request)

    step = int(step)
    total_steps = 7
   
    if step <= 0 or step > total_steps:
        message = "The page number your are trying to view does not exist"
        return render(request, '404.html', {'response': message})
    elif not PRStrategy.objects.filter(anon_userID = anon_userID).exists():
        message = "No strategy creation in progress for this ID, you can start a new strategy below."  
        messages.error(request, message)
        return redirect(reverse('easypr_ng:strategy-planner-intro'))

    if request.method == "POST":
        rp = request.POST  
        if step == 1:
            fields_dict_and_defaults = {'business_type':['unit', 'NA'],'company_type':['unit', 'NA'],'is_pr_agency':['unit','No'],'size_of_company':['unit',0]}
            valid_dict = validate_post_keys(request, fields_dict_and_defaults)
            print "current strategy object: ", current_strategy
            current_strategy.update(business_type = valid_dict['business_type'], company_type = valid_dict['company_type'],
                is_pr_agent = valid_dict['is_pr_agency'], size_of_pr_team = valid_dict['size_of_company'])
            
            # context values for next step
            sectors = get_sectors()
            next_caption = "We are creating a unique experience for you!"
            next_form = TargetAudienceForm()
            next_step = 2
            context.update({'step':next_step,'caption':next_caption, 'form':next_form,'sectors':sectors, 'anon_userID':anon_userID, 'step_template':'step_forms/step2.html'}) #for next form page
             
        if step == 2:
            fields_dict_and_defaults = {'target_audience':['list', 'NA']}
            valid_dict = validate_post_keys(request, fields_dict_and_defaults)
        
            current_strategy.update(target_audience = ",".join(valid_dict['target_audience']))
            
            next_caption = "Your business is about to experience a great and phenomenal boost"
            next_step = 3
            pr_goals =  ['Lead generation','Traffic', 'Engagement', 'SEO', 'Sales', 'Social']
            context.update({'step':next_step, 'caption':next_caption, 'pr_goals':pr_goals, 'pr_frequency':PR_FREQUENCY, 'step_template':'step_forms/step3.html'})

        if step == 3:
            fields_dict_and_defaults = {'pr_goals':['list', 'NA'],'pr_frequency':['unit','NA']}
            valid_dict = validate_post_keys(request, fields_dict_and_defaults)
        
            current_strategy.update(pr_goals = ",".join(valid_dict['pr_goals']), frequency_of_pr = valid_dict['pr_frequency'])
            
            next_caption = "Simplified and targeted PR services for maximum productivity. "
            next_step = 4
            target_audience =  ['Local','Regional', 'State', 'National', 'International']

            context.update({'step':next_step, 'caption':next_caption, 'target_audience':target_audience, 'step_template':'step_forms/step4.html' })

        if step == 4:
            fields_dict_and_defaults = {'target_audience':['list', '[]'],'use_external_db':['unit','NA'],'current_db':['unit', 'NA']}
            valid_dict = validate_post_keys(request, fields_dict_and_defaults)
        
            current_strategy.update(target_audience_location = ",".join(valid_dict['target_audience']), currently_use_pr_db = valid_dict['use_external_db'], pr_db_used = valid_dict['current_db'])
            # save selections from step 3
            next_caption = "create any progressive content for this stage caption."
            next_step = 5
            social_media_platform =  ['Facebook','Twitter','Youtube','Instagram','Vimeo','Pinterest','LinkedIn','Google']
            context.update({'step':next_step, 'caption':next_caption, 'media_platform':social_media_platform, 'step_template':'step_forms/step5.html'})

        if step == 5:
            fields_dict_and_defaults = {'social_media_platform':['list', '[]']}
            valid_dict = validate_post_keys(request, fields_dict_and_defaults)
        
            current_strategy.update(social_media_used = ",".join(valid_dict['social_media_platform']))
            next_caption = "create any progressive content for this stage caption."
            next_step = 6
            context.update({'step':next_step, 'caption':next_caption, 'step_template':'step_forms/step6.html'})

        if step == 6:
            fields_dict_and_defaults = {'need_pr_writing':['unit', 'No'], 'need_media_pitching':['unit','No'],'has_newsroom':['unit','No']}
            valid_dict = validate_post_keys(request, fields_dict_and_defaults)
        
            current_strategy.update(require_pr_writing= valid_dict['need_pr_writing'],require_media_pitching = valid_dict['need_media_pitching'], do_you_have_newsroom = valid_dict['has_newsroom'])
            
            next_caption = "Hurray! you have successfully created a unique PR strategy for your brand."
            next_step = 7
            context.update({'step':next_step, 'caption':next_caption, 'step_template':'step_forms/step7.html'})
        if step == 7:
            fields_dict_and_defaults = {'company_name':['unit', 'NA'], 'contact_name':['unit','NA'],'email':['unit','NA'], 'phone_no':['unit','NA']}
            valid_dict = validate_post_keys(request, fields_dict_and_defaults)

            if valid_dict['company_name'] == "NA" or valid_dict['contact_name'] == "NA" or valid_dict['email']  == "NA":
                messages.info(request, "You have not made any entries yet, please refresh the page to continue.")
                return redirect(reverse('easypr_ng:strategy-planner', kwargs={'step':1, 'anon_userID':current_strategy[0].anon_userID}))
        
            current_strategy.update(company_name = valid_dict['company_name'],contact_name = valid_dict['contact_name'],email = valid_dict['email'], phone_number = valid_dict['phone_no'], completed = True)
            messages.success(request, "Thank you!. We have received your submission, A member of the EasyPR team will contact you shortly")
            return redirect(reverse('easypr_ng:strategy-planner-intro')) 
    return render(request, template, context)






def  servicesView(request, service_category):
    context = {}
    service   =   ServiceCategory.objects.filter(name_slug = service_category)
    if not service.exists():
        message = "service not found"
        return render(request, 'easypr_general/coming-soon.html', {'response': message})
    context['service-list'] = service[0].serviceitem_set.all()
    context['service'] = service[0]
    return render(request, 'easypr_general/services-details.html', context)


def bundlePlanView(request):
    context = {}
    template = 'easypr_ng/package-plans.html'
    return render(request, template, context)


def get_startedView(request, category,item):
    context = {}
    context['form'] = ServiceRequestForm
    template = "easypr_ng/pricing.html"
    return render(request, template, context)


def submitContentView(request, category, item):
    template = "easypr_ng/submit-content.html"
    return render(request, template, {})


def requestServiceView(request, category, item):
    context['form'] = ServiceRequestForm

    template = "easypr_ng/request-service.html"
    return render(request, template, context)










