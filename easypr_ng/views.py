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
from easypr_ng.models import *
from easypr_general.custom_functions import transaction_ref, get_random_code, paginate_list
from easypr_ng.models import MediaHouse, MediaContact, PressMaterial, Redirect_url, Publication, PublicationImage, \
Purchase, PayDetails, PurchaseInvoice, Bouquet, Sector, MediaPlatform

from easypr_ng.forms import ContentUploadForm
import datetime






def  indexView(request):
    context = {}
    press_materials = ["features","press_release","interview","photo_news"]
    for cate in press_materials:
        search_str = cate.replace("_"," ")
        context[cate] = Bouquet.objects.filter(press_material__media_type = search_str)
    return render(request, 'easypr_general/index.html', context)
    



def requestServiceView(request):
    return render(request, 'easypr_ng/request-a-service.html', {})


# def  newsroomView(request):
#     articles = paginate_list(request, Publication.objects.filter(deleted = False, status = "published").order_by('-date_posted'), 5)
#     return render(request, 'yadel/general/newsroom.html', {'articles':articles})




def ourWorksView(request):
    return render(request, 'easypr_ng/our-works.html', {})




def  newsroomView(request):
    context = {}
    context['show_news_list'] = True
    context['show_news_details']   =  False

    return render(request, 'easypr_general/newsroom.html', context)


def  readnewsView(request, post_id, title_slug):
    context = {}
    context['show_news_details']   =  True
    context['show_news_list'] = False
    return render(request, 'easypr_general/newsroom.html', context)





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
        pub_image = PublicationImage.objects.create(image = request.FILES[image], caption = request.POST["cap_"+ image])
        new_post.pictures.add(pub_image)
    new_post.save()
    return new_post






def create_package_bundle(request, bouquet,publication):
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
            new_post   =    create_post(request, press_material)

            new_purchase   =   create_package_bundle(request, bouquet, new_post)

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
    print "date paid", date_paid
    context = {}
    post = Publication.objects.get(transaction_id = kwargs['transaction_id'])

    return render(request, 'easypr_ng/content-preview.html', {'post':post})




@login_required()
def savePayInfo(request, transaction_id):
    print "transaction_id ", transaction_id
    if request.method == "POST":
        rp = request.POST
        purchased  =   get_object_or_404(Purchase, transaction_id = transaction_id)
        pay_details = purchased.payment_details
        PayDetails.objects.filter(pk = pay_details.pk).update(payment_method = rp['method'].replace("_"," ").title(), amount_paid = rp['amount'], date_paid = rp['date'], bank_name = rp['bank'], teller_number = rp['teller'])
        return JsonResponse({'response': 'success'})
   




@login_required()
def Payment(request, **kwargs):
    template = 'easypr_ng/payment.html'
    publication = get_object_or_404(Publication, transaction_id = kwargs['transaction_id'])
    pay_info = get_object_or_404(Purchase, publication = publication)
    return render(request, template, {'post':publication, 'pay_info':pay_info})






def get_media_houses(request):
    media_platform  =   request.POST['media_platform']
    template        =  'snippets/media-options.html'
    platform        =   MediaPlatform.objects.filter(pk = media_platform)
    media_houses    =   MediaHouse.objects.filter(platform__icontains = platform)
    return render(request, template, {'available_media': media_houses})





@login_required()
def confirmationView(request):
    return render(request, 'easypr_ng/confirmation.html', {})

# @login_required()
# def createArticleView(request):
#     articles = Publication.objects.filter(posted_by = request.user, deleted=False, status = "published").order_by('-date_posted')
#     article_form = PublicationForm()
#     article_doc_form = DocumentUploadForm()
#     media_categories  =  MediaCategory.objects.all()
#     media_names = MediaNames.objects.all()
#     if request.method == "POST":
#         rp = request.POST
#         form = PublicationForm(request.POST, request.FILES)
#         doc_form = DocumentUploadForm(request.POST, request.FILES)
#         if form.is_valid() and doc_form.is_valid():
#             article = form.save(commit = False)
#             article.posted_by = request.user
#             article.status = "new"
#             article.save()
#             upload_doc = PubDocument(document = request.FILES['document'], publication = article)
#             upload_doc.save()
#             messages.success(request, "Thank You. Your article has been submitted for publication, We will notify you as soon as this article is published")
#         else:
#             # print form.errors
#             return render(request, 'yadel/general/submit-article.html', {'article_form':article_form, 'doc_form':article_doc_form, 'media_names':media_names, 'media_categories':media_categories,'articles':articles})
#     return render(request, 'yadel/general/submit-article.html', {'article_form':article_form,'doc_form':article_doc_form, 'media_names':media_names, 'media_categories':media_categories, 'articles':articles})







