from django.contrib.sites.models import Site
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User 
from easypr_general.models_field_choices import *
from easypr_general.models import UserAccount




class MediaHouse(models.Model):
  name                =           models.CharField(max_length = 200)
  date_added          =           models.DateTimeField(auto_now_add = True)
  contact_persons     =           models.ManyToManyField('MediaContact', blank = True)
  platform            =           models.CharField(max_length = 25, choices = MEDIA_PLATFORM)

  def __unicode__(self):
    return '%s, %s' %(self.name, self.platform)

  def get_contacts(self):
  	return self.contact_persons.all




class MediaContact(models.Model):
  media_house              =           models.ForeignKey(MediaHouse)
  first_name               =           models.CharField(max_length = 125)
  last_name                =           models.CharField(max_length = 125)
  date_added               =           models.DateTimeField(auto_now_add = True)
  email                    =           models.CharField(max_length = 225)

  def __unicode__(self):
    return '%s,%s,%s' %(self.media_house, self.first_name + self.last_name, self.email)




class PressMaterial(models.Model):
  media_type               =         models.CharField(max_length = 150)
  price_per                =         models.FloatField(default = 0.0)
  date_added               =         models.DateTimeField(auto_now_add = True)

  def __unicode__(self):
    return '%s' %(self.media_type)



class Redirect_url(models.Model):
  url     =        models.CharField(max_length = 200, blank = True, null = True, default= None)

  def __unicode__(self):
    return self.url





class Publication(models.Model):
    posted_by                       =              models.ForeignKey(User)
    post_title                      =              models.CharField(max_length = 175)
    title_slug                      =              models.CharField(max_length = 200)
    status                          =              models.CharField(max_length = 50, choices = PUB_STATUS, default = "new")
    date_posted                     =              models.DateTimeField(auto_now_add = True)
    press_material                  =              models.ForeignKey('PressMaterial')
    media_houses                    =              models.ManyToManyField('MediaHouse')
    content                         =              models.TextField(max_length = 3000, null = True, blank = True)
    person_to_quote                 =              models.CharField(max_length = 125, null = True, blank = True)
    persons_position                =              models.CharField(max_length = 125, null = True, blank = True)
    pictures                        =              models.FileField(upload_to ='media/', null = True, blank = True)
    uploaded_text                   =              models.FileField(upload_to ='publication/%Y-%M-%D', null=True, blank = True)
    deleted                         =              models.BooleanField(default = False)
    publish_online                  =              models.BooleanField("Do you also want online publication of the chosen media? ", default = False)
    published_by                    =              models.ForeignKey(User, related_name="Edited_and_published_by", null = True, blank = True)
    date_published                  =              models.DateTimeField(auto_now_add = False, null=True, blank=True)
    media_urls                      =              models.ManyToManyField(Redirect_url)
    site                            =              models.ManyToManyField(Site)


    def save(self, *args, **kwargs):
        self.title_slug  = slugify(self.post_title)
        super(Publication, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s' %(self.title)

    def get_media_urls(self):
    	return [media.url for media in self.media_urls.all]


    def get_media_houses_and_contacts(self):
    	contact_dict =  {}
    	contact_list =  []
    	for media in self.media_houses.all:
    		for contact in media.contact_persons.all():
    			contact_dict[media.name] = {'name':contact.first_name + " " + contact.last_name, 'email':contact.email}
    			contact_list.append(contact_dict)
    	return contact_list




    def read_uploaded_document(self):
    	pass




class PubDocument(models.Model):
  publication                     =              models.OneToOneField(Publication, verbose_name="Related publication", null = True, blank = True)
  document                        =              models.FileField(upload_to ='publication/%Y-%M-%D', null=True, blank = True)

  def __unicode__(self):
    return self.publication.title







class Purchase(models.Model):
	user              		=     models.ForeignKey(UserAccount, verbose_name = "Purchased By")
	transaction_id   		  =     models.CharField(max_length = 15)
	bouquet           		=     models.ForeignKey('Bouquet')
	publication       		=     models.ForeignKey('Publication')
	deleted           		=     models.BooleanField(default = False)
	ordered           		=     models.BooleanField(default = False) # set to true on order submission after payment is made
	status                =     models.CharField(max_length = 75, choices = PURCHASE_STATUS)
	payment_details       =     models.ForeignKey('PayDetails', verbose_name = "Payment details")
	date_purchased        =     models.DateTimeField(auto_now_add = True)


	def  __unicode__(self):
		return "%s, %s" %(self.transaction_ref, self.status)



class PayDetails(models.Model):
	user                    =     models.OneToOneField(User)
	transaction_id          =     models.CharField(max_length = 25)
	payment_method    		  =     models.CharField(max_length = 75, choices = PAYMENT_OPTIONS)
	amount_paid             =     models.FloatField(default = 0.0)
	date_paid               =     models.DateTimeField(auto_now_add = True)
	bank_name               =     models.CharField(max_length = 100, null = True, blank = True, choices = BANKS)
	teller_number           =     models.CharField(max_length = 15, null = True, blank = True)


	def __unicode__(self):
		return "%s, %s, %s" %(self.user, self.transaction_ref, self.amount_paid)




class PurchaseInvoice(Purchase):
	receipt_no       =        models.CharField(max_length = 12)
	invoice          =        models.FileField(upload_to = 'Invoices/%Y-%M-%D', null = True, blank = True)

	def __unicode__(self):
		return self.receipt_no     

	def get_invoice(receipt_no):
		return self.invoice






class Bouquet(models.Model):
	name             		=       models.CharField(max_length = 75, choices = BOUQUET)
	price_per_media_N       =       models.FloatField("Price in Naira", default = 0.0)
	price_per_media_D       =       models.FloatField("Price in Dollar", default = 0.0)
	Num_of_media     		=       models.IntegerField(default = 0)
	press_material   		=       models.ForeignKey(PressMaterial)
	media_houses     		=       models.ManyToManyField(MediaHouse)
	percentage_commission   =       models.FloatField(default = 0.0)
	amount_payable_N        =       models.FloatField("Total amount in Naira", default = 0.0)
	amount_payable_D        =       models.FloatField("Total amount in Dollar", default = 0.0)

	
	def __unicode__(self):
		return "%s, %s" %(self.press_material, self.name)


	def get_total_price(self, currency):
		amount = 0.0
		if currency == "naira":
			amount = self.price_per_media_N * self.Num_of_media
		elif currency == "dollar":
			amount = self.price_per_media_D * self.Num_of_media
		amount += (amount * VAT)
		return currency, round(amount, 2)






