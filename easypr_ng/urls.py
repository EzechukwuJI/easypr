from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from easypr_ng import views


urlpatterns  =  [

             
	url(r'^$',                         					                views.indexView,                	     name='index'),
	url(r'^planner/step(?P<step>[-\d]+)/UID=(?P<anon_userID>[-\w\d]+)$',      	    views.strategyPlannerView,   name='strategy-planner'),
	url(r'^planner/$',      	                                        views.strategyPlannerIntroView,          name='strategy-planner-intro'),
	# url(r'^planner/$',      	                                        TemplateView.as_view(template_name = "easypr_ng/strategy-planner-info.html"),     name='strategy-planner-intro'),
	# url(r'^request-a-service/$',      				                views.requestServiceView,      name='request-service'),
	
	url(r'^news/(?P<post_id>[-\d]+)/(?P<title_slug>[-\w]+)/$',  		 views.readnewsView,            name = 'news-details'),
	url(r'^newsroom/$',                				                     views.newsRoomView,            name = 'newsroom'),
	url(r'^newsroom/category=(?P<category>[-\w\d]+)$',                	 views.newsRoomCatView,         name = 'newsroom-cat-view'),
	
	url(r'^post-comment/$',                                 	         views.postCommentView,         name = 'post-comment'),
	url(r'^post/comment/reply/$',                	                     views.postCommentReplyView,    name = 'post-reply'),

	url(r'^our-works/$',                				                 views.ourWorksView,            name = 'our-works'),
	url(r'^buy-package/press_material=(?P<press_material>[-\w]+)/package=(?P<package>[-\w]+)/$', views.buy_packageView, name = "buy-package"),
	url(r'^content-upload/preview/ref=(?P<transaction_id>[-\w]+)$',      views.previewPublicationView,  name = "preview-content"),
	url(r'^fetch-media-houses/$',                                        views.get_media_houses,        name = 'get-media-houses'),
	url(r'^fetch-blog-list/$',                                           views.get_blog_list,           name = 'get-blog-list'),
	url(r'^payment/ref=(?P<transaction_id>[-\w]+)$',                     views.Payment,                 name = 'payment'),
	url(r'^payment/save-details/ref=(?P<transaction_id>[-\w]+)/$',       views.savePayInfo,             name = 'save-pay-details'),
	url(r'^content-submission/success/$',                                views.confirmationView,        name = 'confirmation'),

	url(r'^services/(?P<service_category>[-\w]+)/$',         			 views.servicesView,            name = 'service-details'),
	url(r'^bespoke-bundle-plans/$',                                      views.bundlePlanView,          name = 'bundle-plans'),
	
	url(r'^(?P<category>[-\w]+)/(?P<item>[-\w]+)/pricing/$',             views.get_startedView,         name = 'get-started'),
	url(r'^(?P<category>[-\w]+)/(?P<item>[-\w]+)/submit-content/$',      views.submitContentView,       name = 'submit-content'),
	url(r'^(?P<category>[-\w]+)/(?P<item>[-\w]+)/submit-request/$',      views.requestServiceView,      name = 'request-service'),
	
	




	] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)