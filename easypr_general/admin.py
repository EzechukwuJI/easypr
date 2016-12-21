from django.contrib import admin
from easypr_general.models import UserAccount, Address, LatestNews, ClientFeedback, PwResetRecord, ServiceCategory, ServiceItem,MailingList



class UserAccountAdmin(admin.ModelAdmin):
	list_display   =   ('user','company_name','economy_sector','account_type','is_confirmed',)
	list_filter    =   ('economy_sector',)


class ServiceItemAdmin(admin.ModelAdmin):
	prepopulated_fields = {'name_slug':('name',)}


class ServiceCategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'name_slug':('name',)}




admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Address)
admin.site.register(LatestNews)
admin.site.register(ClientFeedback)
admin.site.register(PwResetRecord)
admin.site.register(ServiceCategory, ServiceCategoryAdmin)
admin.site.register(ServiceItem, ServiceItemAdmin)
admin.site.register(MailingList)