from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.db.models import F
from django.contrib import messages

from easypr_ng.models import *
from easypr_general.custom_functions import transaction_ref, get_random_code, paginate_list
from easypr_ng.models import MediaHouse, MediaContact, PressMaterial, Redirect_url, Publication, PubDocument, \
Purchase, PayDetails, PurchaseInvoice, Bouquet






def  indexView(request):
    # current_site = get_current_site(request)
    # return HttpResponse(current_site.domain)
    return render(request, 'easypr_general/index.html', {})
    

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















@login_required()
def createArticleView(request):
    articles = Publication.objects.filter(posted_by = request.user, deleted=False, status = "published").order_by('-date_posted')
    article_form = PublicationForm()
    article_doc_form = DocumentUploadForm()
    media_categories  =  MediaCategory.objects.all()
    media_names = MediaNames.objects.all()
    if request.method == "POST":
        rp = request.POST
        form = PublicationForm(request.POST, request.FILES)
        doc_form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid() and doc_form.is_valid():
            article = form.save(commit = False)
            article.posted_by = request.user
            article.status = "new"
            article.save()
            upload_doc = PubDocument(document = request.FILES['document'], publication = article)
            upload_doc.save()
            messages.success(request, "Thank You. Your article has been submitted for publication, We will notify you as soon as this article is published")
        else:
            # print form.errors
            return render(request, 'yadel/general/submit-article.html', {'article_form':article_form, 'doc_form':article_doc_form, 'media_names':media_names, 'media_categories':media_categories,'articles':articles})
    return render(request, 'yadel/general/submit-article.html', {'article_form':article_form,'doc_form':article_doc_form, 'media_names':media_names, 'media_categories':media_categories, 'articles':articles})







