from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from easypr_ng import views


# Create your urls here.
urlpatterns  =  [

             
	url(r'^$',                         					                views.indexView,               name='index'),
	url(r'^request-a-service/$',      				                    views.requestServiceView,      name='request-service'),

	url(r'^news/(?P<post_id>[-\d]+)/(?P<title_slug>[-\w]+)/$',  		views.readnewsView,            name = 'news-details'),
	url(r'^newsroom/$',                				                    views.newsRoomView,            name = 'newsroom'),
	url(r'^newsroom/category=(?P<category>[-\w\d]+)$',                	views.newsRoomCatView,         name = 'newsroom-cat-view'),
	
	url(r'^post-comment/$',                                 	        views.postCommentView,         name = 'post-comment'),

	url(r'^post/comment/reply/$',                	                    views.postCommentReplyView,    name = 'post-reply'),



	url(r'^our-works/$',                				                views.ourWorksView,            name = 'our-works'),
	url(r'^buy-package/press_material=(?P<press_material>[-\w]+)/package=(?P<package>[-\w]+)/$', views.buy_packageView, name = "buy-package"),
	url(r'^content-upload/preview/ref=(?P<transaction_id>[-\w]+)$',        views.previewPublicationView,  name = "preview-content"),
	url(r'^fetch-media-houses/$',                                          views.get_media_houses,        name = 'get-media-houses'),
	url(r'^payment/ref=(?P<transaction_id>[-\w]+)$',                       views.Payment,                 name = 'payment'),
	url(r'^payment/save-details/ref=(?P<transaction_id>[-\w]+)/$',          views.savePayInfo,            name = 'save-pay-details'),
	url(r'^content-submission/success/$',                                views.confirmationView,          name = 'confirmation'),
	

	# url(r'^fetch-media-houses/(?P<platform>[-\w]+)/$',                  views.get_media_houses,      name = 'get-media-houses'),


	# url(r'^about_us/$',                					views.aboutUsView,        name='about_us'),
	# # url(r'^services/$',                                 views.servicesView,       name='services'),
	# url(r'^newsroom/$',                					views.newsroomView,       name='newsroom'),
	# url(r'^contact_us/$',      		   					views.contactView,        name='contact_us'),
	# url(r'^sign_up/$',         		   					views.signUpView,         name='sign_up'),
	# url(r'^login/$',           		   					views.loginView,          name='login'),
	# url(r'^logout/$',          		   					views.logoutView,         name='logout'),
	# url(r'^accounts/posts/$',          	                views.dashboardView,      name='user-dashboard'),
	# url(r'^terms-and-conditions/$',          		    views.TandCView,          name='tandc'),

	# # url(r'^client/feedback/$',                          views.clientFeedback,           name = 'user-feedback'),
	# url(r'^article/create/new/$',      					views.createArticleView,  name='create-article'),
	# url(r'^services/$',                                 TemplateView.as_view(template_name = "yadel/general/services.html"), name='services'),
	# url(r'^thank-you/$',      					        TemplateView.as_view(template_name = "yadel/general/thank-you.html"), name='registration_success'),
	# url(r'^confirm-registration/(?P<code>[-\w]+)/$',    views.confirmEmail, name = 'confirm-email'),
	# # url(r'^news/(?P<pk>[-\d]+)/(?P<news_title>[-\w]+)/url=(?P<url_link>[-\w]+)/$',  views.loadExternalNews, name = 'news-details')

	# url(r'^news/(?P<pk>[-\d]+)/(?P<news_title>[-\w]+)/$',  views.loadExternalNews, name = 'news-details')

	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)