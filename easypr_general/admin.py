from django.contrib import admin
from easypr_general.models import UserAccount, Address, LatestNews, ClientFeedback, PwResetRecord



class UserAccountAdmin(admin.ModelAdmin):
	list_display   =   ('user','company_name','economy_sector','account_type','is_confirmed',)
	list_filter    =   ('economy_sector',)





admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register(Address)
admin.site.register(LatestNews)
admin.site.register(ClientFeedback)
admin.site.register(PwResetRecord)