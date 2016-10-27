from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from easypr_general import views


# Create your urls here.
urlpatterns  =  [

             
	url(r'^$',                         				views.indexView,                name='homepage'),
	url(r'^who-we-are/$',                			views.aboutUsView,              name='about-us'),
	# url(r'^services/(?P<service_category>[-\w]+)/$',         views.servicesView,             name='service-details'),
	url(r'^contact_us/$',      		   				views.contactView,              name='contact-us'),
	url(r'^user/sign-up/$',         		   	    views.createUserAccount,        name='sign-up'),
	
	url(r'^user/dashboard$',         		   	     views.userDashboard,        name='user-dashboard'),
	# url(r'^product/detail/product-name/$',         	 views.productDetails,        name='product-detail'),
	
	url(r'^login/$',           		   				views.loginView,          		name='login'),
	url(r'^logout/$',          		   				views.logOutView,         		name='logout'),
	url(r'^careers/$',          	                views.careersView,        		name='careers'),
	# url(r'^terms-and-conditions/$',          		    views.TandCView,          name='tandc'),
	# # url(r'^client/feedback/$',                          views.clientFeedback,           name = 'user-feedback'),
	# url(r'^article/create/new/$',      					views.createArticleView,  name='create-article'),
	url(r'^forgot-password/$', 						views.forgotPasswordView,  	name='forgot-password'),
    url(r'^reset-password/Qcr=(?P<code>[-\w]+)/$', 	views.resetPasswordView,  	name='reset-password'),
	url(r'^confirm-registration/(?P<code>[-\w]+)/$',    		        views.confirmEmail, 			name = 'confirm-email'),
	url(r'^thank-you/$',      					    TemplateView.as_view(template_name = "easypr_general/thank-you.html"), name='registration_success'),
	# url(r'^services/$',       views.servicesView,  name='services'),
	# url(r'^services/(?P<name_slug>[-\w]+)/$',       views.servicesView,  name='services'),
	# url(r'^services/$',                             TemplateView.as_view(template_name = "easypr_general/services.html"),  name='services'),
	url(r'^frequently-asked-questions/$',          	TemplateView.as_view(template_name = "easypr_general/faq.html"),  name='faq'),
	url(r'^how-it-works/$',          	            TemplateView.as_view(template_name = "easypr_general/how-it-works.html"),  name='how-it-works'),
	url(r'^terms-and-conditions/$',          	    TemplateView.as_view(template_name = "easypr_general/terms-and-conditions.html"),  name='terms-and-conditions'),


	# url(r'^news/(?P<pk>[-\d]+)/(?P<news_title>[-\w]+)/$',  views.loadExternalNews, name = 'news-details')

	] 
	 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)