from django.contrib import admin
from easypr_ng.models import  MediaHouse, MediaContact,PressMaterial, Redirect_url, \
Publication,PubDocument,Purchase,PayDetails,PurchaseInvoice, Bouquet


class MediaHouseAdmin(admin.ModelAdmin):
	list_display = ('name','platform',)


class PublicationAdmin(admin.ModelAdmin):
	list_display = ('post_title','press_material','posted_by', 'publish_online','date_posted','status',)
	list_filter = ('status','press_material',)
	prepopulated_fields = {'title_slug':('post_title',)}


class BouquetAdmin(admin.ModelAdmin):
	list_display = ('name', 'press_material','Num_of_media','amount_payable_N','amount_payable_D','percentage_commission',)


class PayDetailsAdmin(admin.ModelAdmin):
	list_display = ('date_paid', 'transaction_id','payment_method','amount_paid','bank_name',)
	list_filter  = ('date_paid','bank_name',)


class PurchaseAdmin(admin.ModelAdmin):
	list_display = ('user','date_purchased','transaction_id','bouquet','payment_details',)
	list_filter  = ('bouquet','status',)



admin.site.register(MediaHouse, MediaHouseAdmin)
admin.site.register(MediaContact)
admin.site.register(PressMaterial)
admin.site.register(Redirect_url)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(PubDocument)
admin.site.register(Bouquet, BouquetAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PayDetails, PayDetailsAdmin)
admin.site.register(PurchaseInvoice)








