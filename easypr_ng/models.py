from django.contrib.sites.models import Site
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User 
from easypr_general.models_field_choices import *
from easypr_general.models import UserAccount
from django.db.models import Q, Sum
import random
# from django.contrib.auth.models import User 
from easypr.settings import VAT
from easypr.settings import NAIRA_DOLLAR_RATE as exchange_rate



class MediaPlatform(models.Model):
  name        =   models.CharField(max_length = 60)
  name_slug   =   models.CharField(max_length = 75)
  active      =   models.BooleanField(default = True)
 

  def __unicode__(self):
    return '%s' %(self.name)

  def save(self, *args, **kwargs):
    self.name_slug = slugify(self.name)
    super(MediaPlatform, self).save(*args, **kwargs)
    return True



class Sector(models.Model):
  name           =      models.CharField(max_length = 60)
  name_slug      =      models.CharField(max_length = 75)
  active         =      models.BooleanField(default = True)
 

  def __unicode__(self):
    return '%s' %(self.name)

  def save(self, *args, **kwargs):
    self.name_slug   =   slugify(self.name)
    super(Sector, self).save(*args, **kwargs)


class MediaContact(models.Model):
  media_house              =           models.ForeignKey('MediaHouse')
  first_name               =           models.CharField(max_length = 125)
  last_name                =           models.CharField(max_length = 125)
  date_added               =           models.DateTimeField(auto_now_add = True)
  email                    =           models.CharField(max_length = 225)
  phone_number             =           models.CharField(max_length = 15, null = True, blank = True)

  def __unicode__(self):
    return '%s,%s,%s' %(self.media_house.name, self.first_name + self.last_name, self.email)


class MediaHouse(models.Model):
  name                =           models.CharField(max_length = 200)
  name_slug           =           models.CharField(max_length = 200)
  date_added          =           models.DateTimeField(auto_now_add = True)
  # contact_persons     =           models.ManyToManyField('MediaContact', blank = True)
  platform            =           models.ManyToManyField('MediaPlatform')



  def save(self, *args, **kwargs):
    self.name_slug  = slugify(self.name)
    super(MediaHouse, self).save(*args, **kwargs)


  def __unicode__(self):
    return '%s' %(self.name)


  def get_contacts(self):
  	return self.mediacontact_set.all()




class PressMaterial(models.Model):
  name_slug                =         models.CharField(max_length = 150)
  media_type               =         models.CharField(max_length = 150)
  price_per                =         models.FloatField(default = 0.0)
  date_added               =         models.DateTimeField(auto_now_add = True)
  caption                  =         models.CharField(max_length = 125)

  def __unicode__(self):
    return '%s' %(self.media_type)

  def save(self, *args, **kwargs):
    self.name_slug  = slugify(self.media_type)
    super(PressMaterial, self).save(*args, **kwargs)



class PublicationManager(models.Manager):

  def published_articles(self):
    return self.get_queryset().filter(Q(status = "Published"), Q(deleted = False))

  def new_articles(self):
      return self.get_queryset().filter(status = "New", deleted = False)



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

    # media_urls                      =              models.ManyToManyField('Redirect_url', )
    site                            =              models.ManyToManyField(Site)
    # pictures                        =              models.ManyToManyField('PublicationImage')
    media_houses                    =              models.ManyToManyField('MediaHouse')
    
    deleted                         =              models.BooleanField(default = False)
    publish_online                  =              models.BooleanField("Do you also want online publication of the chosen media? ", default = False)
    completed                       =              models.BooleanField(default = False)
    objects                         =              PublicationManager()


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


    def get_images(self):
      return self.publicationimage_set.all()


    def featured_image(self):
      try:
        return self.get_images()[random.choice(range(0, self.get_images().count() -1))].image.url
      except:
        return None


    def get_post_comments(self):
      return self.comment_set.all()

    def read_uploaded_document(self):
    	pass




class PublicationImage(models.Model):
  post      =    models.ForeignKey('Publication', null = True, blank = True)
  image     =    models.FileField(upload_to ='publicaton_image/%Y/%M/%D', null = True, blank = True)      
  caption   =    models.CharField(max_length = 200, null = True, blank =  True)

 

class Redirect_url(models.Model):
  url     =        models.CharField(max_length = 200, blank = True, null = True, default= None)
  post    =        models.ForeignKey('Publication', null=True, blank = True)

  def __unicode__(self):
    return self.url


class Comment(models.Model):
  post            =     models.ForeignKey('Publication')
  posted_by       =     models.ForeignKey(User)
  date_posted     =     models.DateTimeField(auto_now_add = True)
  comment         =     models.TextField(max_length = 1000)
  website         =     models.CharField(max_length = 150, null = True, blank = True)


class CommentReply(models.Model):
  comment         =     models.ForeignKey('Comment')
  posted_by       =     models.ForeignKey(User)
  date_posted     =     models.DateTimeField(auto_now_add = True)
  reply           =     models.TextField(max_length = 1000)
  


class Purchase(models.Model):
  user              		=     models.ForeignKey(User, verbose_name = "Purchased By")
  transaction_id   		  =     models.CharField(max_length = 15)
  package           		=     models.ForeignKey('Package')
  publication       		=     models.OneToOneField('Publication')
  deleted           		=     models.BooleanField(default = False)
  ordered           		=     models.BooleanField(default = False) # set to true on order submission after payment is made
  status                =     models.CharField(max_length = 75, choices = PURCHASE_STATUS, default = "New")
  payment_details       =     models.ForeignKey('PayDetails', verbose_name = "Payment details", default = None)
  date_purchased        =     models.DateTimeField(auto_now_add = True)


  def  __unicode__(self):
    return "%s %s" %(self.transaction_id, self.status)

  def media_outreach_credit(self):
    return self.package.media_outreach_credit

  def  price_dollar(self):
    return self.package.price_dollar


  def  price_naira(self):
    return self.package.price_naira

  # def VAT_N(self):
  #   return  VAT * self.price_naira

  # def VAT_D(self):
  #   return float(VAT * self.price_dollar)


  # def   amount_payable_D(self):
  #   total = self.VAT_D + self.price_dollar
  #   return total

  # def   amount_payable_N(self):
  #   total = float(self.VAT_N + self.price_naira)
  #   return total






class PayDetails(models.Model):
    user                    =     models.ForeignKey(User, verbose_name = "Payment By")
    transaction_id          =     models.CharField(max_length = 25, null = True)
    payment_method    		  =     models.CharField(max_length = 75, choices = PAYMENT_OPTIONS, default = "")
    amount_paid             =     models.FloatField(default = 0.0)
    date_paid               =     models.CharField(max_length = 100, null = True, blank = True,)
    bank_name               =     models.CharField(max_length = 100, null = True, blank = True, choices = BANKS)
    currency                =     models.CharField(max_length = 100, null = True, blank = True)
    teller_number           =     models.CharField(max_length = 15, null = True,  blank = True)
    pay_status              =     models.CharField(max_length = 25, choices = PAYMENT_STATUS, default = "pending")
    verified_by             =     models.BooleanField(default = False)
    date_verified           =     models.DateTimeField(auto_now_add = False, null =True, blank = True)

    def __unicode__(self):
      return "%s, %s, %s" %(self.transaction_id, self.amount_paid, self.pay_status)




class PurchaseInvoice(Purchase):
	receipt_no       =        models.CharField(max_length = 12)
	invoice          =        models.FileField(upload_to = 'Invoices/%Y-%M-%D', null = True, blank = True)

	def __unicode__(self):
		return self.receipt_no     

	def get_invoice(receipt_no):
		return self.invoice




# class Bouquet(models.Model):
#   name                            =       models.CharField(max_length = 75, choices = BOUQUET)
#   name_slug             	        =       models.CharField(max_length = 75)
#   price_per_media_N               =       models.FloatField("Price in Naira", default = 0.0)
#   price_per_media_D               =       models.FloatField("Price in Dollar", default = 0.0)
#   discounted_price_per_media_N    =       models.FloatField("Discounted Price Naira", default = 0.0)
#   discounted_price_per_media_D    =       models.FloatField("Discounted Price Dollar", default = 0.0)
#   num_of_media     		            =       models.IntegerField(default = 0)
#   press_material   		            =       models.ForeignKey(PressMaterial)
#   media_houses     		            =       models.ManyToManyField(MediaHouse)
#   percentage_commission           =       models.FloatField(default = 0.0)
#   percentage_savings              =       models.FloatField(default = 0.0)
#   amount_payable_N                =       models.FloatField("Total amount in Naira", default = 0.0)
#   amount_payable_D                =       models.FloatField("Total amount in Dollar", default = 0.0)



#   def save(self, *args, **kwargs):
#     self.name_slug  = slugify(self.name)

#     amount_to_pay_N = self.price_per_media_N * self.num_of_media
#     amount_to_pay_D = self.price_per_media_D * self.num_of_media

#     if amount_to_pay_N > amount_payable_N:
#       saved_N = (amount_to_pay_N - amount_payable_N)

#       self.percentage_savings = (saved_N/amount_payable_N) * 100
#     super(Bouquet, self).save(*args, **kwargs)
   

#   def __unicode__(self):
#     return "%s, %s" %(self.press_material, self.name)


#   def get_total_price(self, currency):
#     amount = 0.0
#     if currency == "naira":
#     	amount = self.price_per_media_N * self.Num_of_media
#     elif currency == "dollar":
#     	amount = self.price_per_media_D * self.Num_of_media
#     amount += (amount * VAT)
#     return currency, round(amount, 2)
      

#   def get_media_type_slug(self):
#     return self.press_material.name_slug

    
    



class PRStrategy(models.Model):
  anon_userID                 =       models.CharField('Annonymous user ID', max_length = 75)
  # company info
  business_type               =       models.CharField(max_length = 25, choices = BUSINESS_TYPE, default = "Company")
  company_type                =       models.CharField(max_length = 75, choices = COMPANY_TYPE, default = "Private")
  is_pr_agent                 =       models.CharField(max_length = 75, choices = (('Yes', 'Yes',),('No','No',),), default = "No")
  size_of_pr_team             =       models.IntegerField(default = 0)
  #target
  target_audience             =      models.TextField(max_length = 1000, null = True) #models.ManyToManyField(Sector, null = True)
  pr_goals                    =      models.TextField(max_length = 1000, null = True)
  frequency_of_pr             =      models.CharField(max_length = 100, choices = PR_FREQUENCY, default = "monthly")
  target_audience_location    =      models.CharField(max_length = 250, null= True)
  
  currently_use_pr_db         =      models.BooleanField(default = False)
  social_media_used           =      models.TextField(max_length = 1000, null = True)
  pr_db_used                  =      models.TextField(max_length = 1000, null = True)
  
  require_pr_writing          =      models.BooleanField(default = False)
  require_media_pitching      =      models.BooleanField(default = False)
  do_you_have_newsroom        =      models.BooleanField(default = False)
  name_pr_newsroom_link       =      models.CharField(max_length = 200)

  date_submitted              =      models.DateTimeField(auto_now_add = True)
  action_status               =      models.CharField(max_length = 75, choices = ACTION_STATUS, default = "Contacted")
  # user details
  company_name                =      models.CharField(max_length = 200, null = True)
  contact_name                =      models.CharField(max_length = 125, null = True)
  email                       =      models.CharField(max_length = 125, null = True)
  phone_number                =      models.CharField(max_length = 25,  null = True)

  # tracking
  completed                  =       models.BooleanField(default = False)


  class Meta():
    ordering = ['date_submitted']
    verbose_name_plural = "PR Strategy"

  def __unicode__(self):
    return '%s | %s | %s' %(self.company_name, self.company_type, self.business_type)

  def get_target_audience(self):
    audience_list = "".join(self.target_audience.split(','))
    return audience_list

  def get_pr_goals(self):
    pr_goals = "".join(self.pr_goals.split(','))
    return pr_goals




class  ServiceRequest(models.Model):
  ticket_number           =     models.CharField(max_length = 14)
  service_type            =     models.CharField(max_length = 100, choices = SERVICE_TYPE)
  sector                  =     models.CharField(max_length = 100, choices = ECONOMY_SECTOR)
  brief_description       =     models.TextField(max_length = 500, null = True, blank = True)
  target_media            =     models.CharField(max_length = 125, choices = MEDIA_PLATFORM)
  time_service_needed     =     models.CharField(max_length = 75)  
  preffered_call_time     =     models.CharField(max_length = 50)
  allow_call              =     models.BooleanField(default = False)

  contact_person          =     models.CharField(max_length = 125)
  contact_email           =     models.EmailField(max_length = 255)
  phone_number            =     models.CharField(max_length = 15)
  
  status                  =     models.CharField(max_length = 25, choices = ACTION_STATUS, default = "new")
  request_outcome         =     models.CharField(max_length = 25, choices = REQUEST_OUTCOME)

  contacted_by            =     models.OneToOneField(User, related_name = "contacted_by", null = True, blank = True)
  closed_by               =     models.OneToOneField(User, related_name = "closed_by", null = True, blank = True)
  date_requested          =     models.DateTimeField(auto_now_add = True)
  date_closed             =     models.DateTimeField(null = True, blank = True)


  def __unicode__(self):
    return '%s - %s' %(self.ticket_number, self.service_type)


  class Meta:
    ordering = ('-date_requested',)
    verbose_name_plural = "Service request"




class  InterviewRequest(models.Model):
  ticket_number                =     models.CharField(max_length = 14)
  preferred_interview_date     =     models.DateTimeField()
  preferred_media_house        =     models.ManyToManyField('MediaHouse')
  interview_venue              =     models.TextField(max_length =  300, null = True)
  interview_date               =     models.DateTimeField()
  interview_time               =     models.DateTimeField()

  contact_person               =     models.CharField(max_length = 125)
  contact_email                =     models.EmailField(max_length = 255)
  phone_number                 =     models.CharField(max_length = 15)
  person_to_be_interviewed     =     models.CharField(max_length = 125)

  status                       =     models.CharField(max_length = 25, choices = ACTION_STATUS, default = "new")
  request_outcome              =     models.CharField(max_length = 25, choices = REQUEST_OUTCOME)

  contacted_by                 =     models.OneToOneField(User, related_name = "interview_contacted_by", null = True, blank = True)
  closed_by                    =     models.OneToOneField(User, related_name = "interview_closed_by", null = True, blank = True)
  date_requested               =     models.DateTimeField(auto_now_add = True)
  date_closed                  =     models.DateTimeField()


  def __unicode__(self):
    return '%s - %s' %(self.ticket_number, self.status)

  class Meta:
    ordering = ('-date_requested',)
    verbose_name_plural = "Interview request"



class BasePackage(models.Model):
  category                 =         models.ForeignKey(PressMaterial)
  name                     =         models.CharField(max_length = 75, choices = PACKAGES )
  media_outreach_credit    =         models.CharField(max_length = 25, default = 1)
  online                   =         models.CharField("online_newspaper_publishing", max_length = 5, choices =  BOOLEAN_CHOICES)
  monitoring               =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  free_consulting          =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  newsroom                 =         models.CharField("Newsroom via EasyPR Media Desk", max_length = 5, choices =  BOOLEAN_CHOICES)
  google_news_inclusions   =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  reuters_news_network     =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  hyperlinks               =         models.CharField("hyperlinks in online press release", max_length = 5)
  notification             =         models.CharField("publication notification via email", max_length = 5, choices =  BOOLEAN_CHOICES)
  autopost                 =         models.CharField("autopost to social media account", max_length = 5, choices =  BOOLEAN_CHOICES)
  analytics                =         models.CharField("detailed analytics report", max_length = 5, choices =  BOOLEAN_CHOICES)
  expedited                =         models.CharField("expedited release processing", max_length = 5, choices =  BOOLEAN_CHOICES)
  available_on_homepage    =         models.CharField("news made available to journalists, bloggers and researchers via EasyPR homepage", max_length = 5, choices =  BOOLEAN_CHOICES)
  content_writing          =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  content_editing          =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  featured_package         =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  price_naira              =         models.FloatField(max_length = 25, default = 0.0)
  price_dollar             =         models.FloatField(max_length = 25, default = 0.0)
  active                   =         models.BooleanField(default = False)
  is_promo                 =         models.BooleanField(default = False)
  promo_starts             =         models.DateTimeField(auto_now_add = True)
  promo_ends               =         models.DateTimeField(auto_now_add = True)
  promo_price_dollar       =         models.FloatField(max_length = 25, default = 0.0)
  promo_price_naira        =         models.FloatField(max_length = 25, default = 0.0)
  


  class Meta:
    abstract = True


class Package(models.Model):
  category                 =         models.ForeignKey(PressMaterial)
  name                     =         models.CharField(max_length = 75, choices = PACKAGES )
  media_outreach_credit    =         models.CharField(max_length = 25, default = 1)
  online                   =         models.CharField("online_newspaper_publishing", max_length = 5, choices =  BOOLEAN_CHOICES)
  monitoring               =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  free_consulting          =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  newsroom                 =         models.CharField("Newsroom via EasyPR Media Desk", max_length = 5, choices =  BOOLEAN_CHOICES)
  google_news_inclusions   =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  reuters_news_network     =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  hyperlinks               =         models.CharField("hyperlinks in online press release", max_length = 5)
  notification             =         models.CharField("publication notification via email", max_length = 5, choices =  BOOLEAN_CHOICES)
  autopost                 =         models.CharField("autopost to social media account", max_length = 5, choices =  BOOLEAN_CHOICES)
  analytics                =         models.CharField("detailed analytics report", max_length = 5, choices =  BOOLEAN_CHOICES)
  expedited                =         models.CharField("expedited release processing", max_length = 5, choices =  BOOLEAN_CHOICES)
  available_on_homepage    =         models.CharField("news made available to journalists, bloggers and researchers via EasyPR homepage", max_length = 5, choices =  BOOLEAN_CHOICES)
  content_writing          =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  content_editing          =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  featured_package         =         models.CharField(max_length = 5, choices =  BOOLEAN_CHOICES)
  price_naira              =         models.FloatField(max_length = 25, default = 0.0)
  price_dollar             =         models.FloatField(max_length = 25, default = 0.0)
  active                   =         models.BooleanField(default = False)
  is_promo                 =         models.BooleanField(default = False)
  promo_starts             =         models.DateTimeField(auto_now_add = True)
  promo_ends               =         models.DateTimeField(auto_now_add = True)
  promo_price_dollar       =         models.FloatField(max_length = 25, default = 0.0)
  promo_price_naira        =         models.FloatField(max_length = 25, default = 0.0)
 
  def __unicode__(self):
    return '%s' %(self.name)


  def save(self, *args, **kwargs):
    self.price_naira = self.price_dollar * exchange_rate
    super(Package, self).save(*args, **kwargs)


  def VAT_N(self):
    return  VAT * self.price_naira


  def VAT_D(self):
    return float(VAT * self.price_dollar)


  def   amount_payable_D(self):
    vat = float(VAT *  self.price_dollar)
    return vat + self.price_dollar


  def   amount_payable_N(self):
    vat = float(VAT * self.price_naira)
    return vat + self.price_naira


  def get_category_packages(self, category):
    pass


  class Meta:
    verbose_name_plural = "Packages"











