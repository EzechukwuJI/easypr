from django.contrib import admin
from easypr_ng.models import  MediaHouse, MediaContact,PressMaterial, Redirect_url, \
Publication,PublicationImage,Purchase,PayDetails,PurchaseInvoice, Bouquet,MediaPlatform, Sector


class MediaHouseAdmin(admin.ModelAdmin):
	list_display = ('name',)


class PublicationAdmin(admin.ModelAdmin):
	list_display = ('post_title','press_material','posted_by', 'publish_online','date_posted','status',)
	list_filter = ('status','press_material',)
	prepopulated_fields = {'title_slug':('post_title',)}



class SectorAdmin(admin.ModelAdmin):
	prepopulated_fields = {'name_slug':('name',)}


class MediaPlatformAdmin(admin.ModelAdmin):
	prepopulated_fields = {'name_slug':('name',)}


class BouquetAdmin(admin.ModelAdmin):
	list_display = ('name', 'press_material','num_of_media','amount_payable_N','amount_payable_D','percentage_commission',)


class PayDetailsAdmin(admin.ModelAdmin):
	list_display = ('date_paid', 'transaction_id','payment_method','amount_paid','bank_name',)
	list_filter  = ('date_paid','bank_name',)


class PurchaseAdmin(admin.ModelAdmin):
	list_display = ('user','date_purchased','transaction_id','bouquet','payment_details',)
	list_filter  = ('bouquet','status',)








admin.site.register(MediaHouse, MediaHouseAdmin)
admin.site.register(MediaContact)
admin.site.register(MediaPlatform, MediaPlatformAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(PressMaterial)
admin.site.register(Redirect_url)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(PublicationImage)
admin.site.register(Bouquet, BouquetAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PayDetails, PayDetailsAdmin)
admin.site.register(PurchaseInvoice)








