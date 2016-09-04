from django.contrib.sites.models import Site
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User 
from easypr_general.models_field_choices import *
from easypr_general.models import UserAccount



class MediaPlatform(models.Model):
  name        =   models.CharField(max_length = 60)
  name_slug   =   models.CharField(max_length = 75)
  active      =   models.BooleanField(default = True)
 

  def __unicode__(self):
    return self.name

  def save(self, *args, **kwargs):
    self.name_slug = slugify(self.name)
    super(MediaPlatform, self).save(*args, **kwargs)



class Sector(models.Model):
  name           =      models.CharField(max_length = 60)
  name_slug      =      models.CharField(max_length = 75)
  active         =      models.BooleanField(default = True)
 


  def __unicode__(self):
    return self.name

  def save(self, *args, **kwargs):
    self.name_slug   =   slugify(self.name)
    super(Sector, self).save(*args, **kwargs)





class MediaHouse(models.Model):
  name                =           models.CharField(max_length = 200)
  name_slug           =           models.CharField(max_length = 200)
  date_added          =           models.DateTimeField(auto_now_add = True)
  contact_persons     =           models.ManyToManyField('MediaContact', blank = True)
  platform            =           models.ManyToManyField('MediaPlatform', blank = True)



  def save(self, *args, **kwargs):
    self.name_slug  = slugify(self.name)
    super(MediaHouse, self).save(*args, **kwargs)



  def __unicode__(self):
    return '%s, %s' %(self.name, self.platform)

  def get_contacts(self):
  	return self.contact_persons.all()




class MediaContact(models.Model):
  media_house              =           models.ForeignKey(MediaHouse)
  first_name               =           models.CharField(max_length = 125)
  last_name                =           models.CharField(max_length = 125)
  date_added               =           models.DateTimeField(auto_now_add = True)
  email                    =           models.CharField(max_length = 225)

  def __unicode__(self):
    return '%s,%s,%s' %(self.media_house, self.first_name + self.last_name, self.email)






class PressMaterial(models.Model):
  name_slug                =         models.CharField(max_length = 150)
  media_type               =         models.CharField(max_length = 150)
  price_per                =         models.FloatField(default = 0.0)
  date_added               =         models.DateTimeField(auto_now_add = True)

  def __unicode__(self):
    return '%s' %(self.media_type)

  def save(self, *args, **kwargs):
    self.name_slug  = slugify(self.media_type)
    super(PressMaterial, self).save(*args, **kwargs)









class Redirect_url(models.Model):
  url     =        models.CharField(max_length = 200, blank = True, null = True, default= None)

  def __unicode__(self):
    return self.url






class Publication(models.Model):
    transaction_id                  =              models.CharField(max_length = 15)
    post_title                      =              models.CharField(max_length = 175)
    title_slug                      =              models.CharField(max_length = 200)
    status                          =              models.CharField(max_length = 50, choices = PUB_STATUS, default = "New")
    post_body                       =              models.TextField(max_length = 3000, null = True, blank = True)
    person_to_quote                 =              models.CharField(max_length = 125, null = True, blank = True)
    persons_position                =              models.CharField(max_length = 125, null = True, blank = True)
    
    uploaded_text                   =              models.FileField(upload_to ='publication/%Y-%M-%D', null=True, blank = True)
    
    posted_by                       =              models.ForeignKey(User)
    platform                        =              models.ForeignKey('MediaPlatform', verbose_name = "Media platform", null = True, blank = True)
    sector                          =              models.ForeignKey('Sector', verbose_name = "Media sector", null = True, blank = True)
    press_material                  =              models.ForeignKey('PressMaterial', verbose_name = "Media category", null = True, blank = True)
    published_by                    =              models.ForeignKey(User, related_name="Edited_and_published_by", null = True, blank = True)
    assigned_to                     =              models.ForeignKey(User, related_name = "Third_party_Editor", null = True, blank = True)
    
    date_published                  =              models.DateTimeField(auto_now_add = False, null=True, blank=True)
    date_posted                     =              models.DateTimeField(auto_now_add = True)

    media_urls                      =              models.ManyToManyField('Redirect_url', )
    site                            =              models.ManyToManyField(Site)
    pictures                        =              models.ManyToManyField('PublicationImage')
    media_houses                    =              models.ManyToManyField('MediaHouse')
    
    deleted                         =              models.BooleanField(default = False)
    publish_online                  =              models.BooleanField("Do you also want online publication of the chosen media? ", default = False)
    ordered                         =              models.BooleanField(default = False)



    def save(self, *args, **kwargs):
        self.title_slug  = slugify(self.post_title)
        super(Publication, self).save(*args, **kwargs)

    def __unicode__(self):
        return '%s' %(self.post_title)



    def get_media_urls(self):
    	return [media.url for media in self.media_urls.all()]




    def get_media_houses(self):
      media = [ media.name for media in self.media_houses.all()]
      return ", ".join(media)




    def get_media_houses_and_contacts(self):
    	contact_dict =  {}
    	contact_list =  []
    	for media in self.media_houses.all():
    		for contact in media.contact_persons.all():
    			contact_dict[media.name] = {'name':contact.first_name + " " + contact.last_name, 'email':contact.email}
    			contact_list.append(contact_dict)
    	return contact_list


    def get_publication_pictures(self):
      return self.pictures.all()



    def read_uploaded_document(self):
    	pass




class PublicationImage(models.Model):
  image     =    models.FileField(upload_to ='media/publicaton_image/%Y-%M-%D', null = True, blank = True)      
  caption   =    models.CharField(max_length = 200, null = True, blank =  True)

  # def __unicode__(self):
  #   return self.publication.title








class Purchase(models.Model):
	user              		=     models.ForeignKey(User, verbose_name = "Purchased By")
	transaction_id   		  =     models.CharField(max_length = 15)
	bouquet           		=     models.ForeignKey('Bouquet')
	publication       		=     models.ForeignKey('Publication')
	deleted           		=     models.BooleanField(default = False)
	ordered           		=     models.BooleanField(default = False) # set to true on order submission after payment is made
	status                =     models.CharField(max_length = 75, choices = PURCHASE_STATUS, default = "New")
	payment_details       =     models.ForeignKey('PayDetails', verbose_name = "Payment details", default = None)
	date_purchased        =     models.DateTimeField(auto_now_add = True)


	def  __unicode__(self):
		return "%s, %s" %(self.transaction_id, self.status)



class PayDetails(models.Model):
	user                    =     models.ForeignKey(User, verbose_name = "Payment By")
	transaction_id          =     models.CharField(max_length = 25, null = True)
	payment_method    		  =     models.CharField(max_length = 75, choices = PAYMENT_OPTIONS, default = "")
	amount_paid             =     models.FloatField(default = 0.0)
	date_paid               =     models.DateTimeField(null = True, blank = True)
	bank_name               =     models.CharField(max_length = 100, null = True, blank = True, choices = BANKS)
	teller_number           =     models.CharField(max_length = 15, null = True, blank = True)


	def __unicode__(self):
		return "%s, %s, %s" %(self.user, self.transaction_id, self.amount_paid)




class PurchaseInvoice(Purchase):
	receipt_no       =        models.CharField(max_length = 12)
	invoice          =        models.FileField(upload_to = 'Invoices/%Y-%M-%D', null = True, blank = True)

	def __unicode__(self):
		return self.receipt_no     

	def get_invoice(receipt_no):
		return self.invoice






class Bouquet(models.Model):
  name                            =       models.CharField(max_length = 75, choices = BOUQUET)
  name_slug             	        =       models.CharField(max_length = 75)
  price_per_media_N               =       models.FloatField("Price in Naira", default = 0.0)
  price_per_media_D               =       models.FloatField("Price in Dollar", default = 0.0)
  discounted_price_per_media_N    =       models.FloatField("Discounted Price Naira", default = 0.0)
  discounted_price_per_media_D    =       models.FloatField("Discounted Price Dollar", default = 0.0)
  num_of_media     		            =       models.IntegerField(default = 0)
  press_material   		            =       models.ForeignKey(PressMaterial)
  media_houses     		            =       models.ManyToManyField(MediaHouse)
  percentage_commission           =       models.FloatField(default = 0.0)
  percentage_savings              =       models.FloatField(default = 0.0)
  amount_payable_N                =       models.FloatField("Total amount in Naira", default = 0.0)
  amount_payable_D                =       models.FloatField("Total amount in Dollar", default = 0.0)



  def save(self, *args, **kwargs):
    self.name_slug  = slugify(self.name)

    amount_to_pay_N = self.price_per_media_N * self.num_of_media
    amount_to_pay_D = self.price_per_media_D * self.num_of_media

    if amount_to_pay_N > amount_payable_N:
      saved_N = (amount_to_pay_N - amount_payable_N)

      self.percentage_savings = (saved_N/amount_payable_N) * 100
    super(Bouquet, self).save(*args, **kwargs)
   
    

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
      

  def get_media_type_slug(self):
    return self.press_material.name_slug

    
    






