import random
import string
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from easypr_ng.models import PressMaterial, Package
from django.shortcuts import get_object_or_404
from easypr.settings import DEFAULT_FROM_EMAIL
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import get_template, render_to_string
from django.template import Context, RequestContext
from django.shortcuts import render, redirect
# from easypr_general.views import current_site



def transaction_ref(transaction_type, model, stringlength):
    prefix = transaction_type[:2].upper()
    random_chars = "".join([random.choice(string.ascii_uppercase + string.digits) for n in range(stringlength)])
    trx_id = prefix + str(random_chars)
    if transaction_type == "request":
        return trx_id if not model.objects.filter(ticket_number = trx_id).exists() else transaction_ref(transaction_type, model)    
    return trx_id if not model.objects.filter(transaction_id = trx_id).exists() else transaction_ref(transaction_type, model)	



def get_random_code(stringlength):
    random_chars = "".join([random.choice(string.ascii_letters + string.digits) for n in range(stringlength)])
    return random_chars


def paginate_list(request, objects_list, num_per_page):
    paginator   =   Paginator(objects_list, num_per_page)
    page  = request.GET.get('page')
    try:
        paginated_list  = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer, deliver first page
        paginated_list   =   paginator.page(1)
    except  EmptyPage:
        #if page is out of range(e.g 9999), deliver last page of results
        paginated_list      =   paginator.page(paginator.num_pages)
    return paginated_list



def get_category_packages_dicts_list(press_material):
    ''' Builds a dictionary fields and list of values for packages in selected 
    pressmaterial, returns package dict and press material'''
    field_name = ""
    counter = 0
    pkg_key_value_dict = {}
    pkg_key_value_dicts_list  = []
    press_category = get_object_or_404(PressMaterial, name_slug = press_material)

    # fetch all applicable packages in the selected category
    pkgs = Package.objects.filter(category = press_category)
    fields_to_delete = ['category','ID','promo_starts','promo_ends','promo_price_dollar','promo_price_naira','is_promo','active','featured_package']
    if pkgs:
        for field in pkgs[0]._meta.fields: # get non hidden field names for packages
            field_values = []
            if not field.__dict__['_verbose_name'] == None:
                field_name = field.__dict__['_verbose_name']
            else:
                field_name = field.__dict__['name']
            for pkg in pkgs:
                field_value = getattr(pkg, field.__dict__['name'])
                field_values.append(field_value)
            if field_name not in fields_to_delete:
                pkg_key_value_dicts_list.append({field_name: field_values})
    return pkg_key_value_dicts_list, press_category




def easypr_send_mail(request, **kwargs):
    if request.user.is_authenticated():
        name = request.user.get_full_name()
        to = request.user.email
    else:
        name       =   kwargs.get('recipient')
        to         =   kwargs.get('useremail')
    text           =   kwargs.get('text',"")
    subject        =   kwargs.get('subject',"")
    extra_ctx      =   kwargs.get('context',{})

    from_email = '{} <{}>'.format(get_current_site(request).name, DEFAULT_FROM_EMAIL)
    msg_text   = render_to_string(text)
    ctx        = {
        'username': name,
        'body': get_template(text).render(Context({'request':request})),
        'request':request,
        'domain_name':get_current_site(request).domain,
        'display_name':get_current_site(request).name
        }
    if not extra_ctx == {}:
        extra_ctx.update({'request':request})
        ctx['body'] = get_template(text).render(Context(extra_ctx))
    message = get_template('emails/base-email.html').render(Context(ctx))

    msg = EmailMessage(subject, message, from_email, [to])
    msg.content_subtype = 'html'
    try:
        print "Sending mail ..."
        msg.send()
    except Exception as e:
        print "email not sent because %s" %(e)
    return HttpResponse(message)











