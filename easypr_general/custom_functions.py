import random
import string
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from easypr_ng.models import PressMaterial, Packages
from django.shortcuts import get_object_or_404


def transaction_ref(transaction_type, model, stringlength):
	prefix = transaction_type[:2].upper()
	random_chars = "".join([random.choice(string.ascii_uppercase + string.digits) for n in range(stringlength)])
	trx_id = prefix + str(random_chars)
	return trx_id if not model.objects.filter(transaction_id = trx_id).exists() else transaction_ref(transaction_type,model)	



def get_random_code(stringlength):
    random_chars = "".join([random.choice(string.ascii_letters + string.digits) for n in range(stringlength)])
    return random_chars

# def get_ticket_number(stringlength, model, allowed_chars = None):





def paginate_list(request, objects_list, num_per_page):
    paginator   =   Paginator(objects_list, num_per_page) # show number of jobs per page
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





def get_category_packages_dict(press_material):
    ''' Builds a dictionary fields and list of values for packages in selected 
    pressmaterial, returns package dict and press material'''
    field_name = ""
    counter = 0
    pkg_key_value_dict = {}
    press_category = get_object_or_404(PressMaterial, name_slug = press_material)

    # fetch all applicable packages in the selected category
    pkgs = Packages.objects.filter(category = press_category)
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
                pkg_key_value_dict[field_name] = field_values
    return pkg_key_value_dict, press_category
















