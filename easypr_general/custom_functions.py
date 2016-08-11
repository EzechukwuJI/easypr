import random
import string


def transaction_ref(transaction_type, model):
	prefix = transaction_type[:2].upper()
	random_chars = "".join([random.choice(string.ascii_uppercase + string.digits) for n in range(10)])
	trx_id = prefix + str(random_chars)
	return trx_id if not model.objects.filter(transaction_id = trx_id).exists() else get_transaction_ref(transaction_type,model)	



def get_random_code(stringlength):
    random_chars = "".join([random.choice(string.ascii_letters + string.digits) for n in range(stringlength)])
    return random_chars




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