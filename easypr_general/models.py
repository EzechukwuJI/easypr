from django.contrib.sites.models import Site
# import timezone
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User 
from models_field_choices import TITLE, COUNTRIES, FEEDBACK_STATUS, SERVICE_ITEM, SERVICE_TYPE, ACTION_TYPE
# , ECONOMY_SECTOR
from easypr.settings import VAT


class UserAccount(models.Model):
    title                            =         models.CharField(max_length = 15, choices = TITLE, default = "")
    user                             =         models.OneToOneField(User)
    account_type                     =         models.CharField(max_length = 20,) #choices = ACCOUNT_TYPE)
    phone_no                         =         models.CharField(max_length = 15)
    company_name                     =         models.CharField(max_length  =  100, null = True, blank = True)
    economy_sector                   =         models.CharField(max_length = 75,) #choices = ECONOMY_SECTOR)
    is_confirmed                     =         models.BooleanField(default = False)
    profile_upto_date                =         models.BooleanField(default = False)
    address                          =         models.ForeignKey('Address', default= None, null = True)
    website                          =         models.CharField(max_length = 175, null=True)
    brand_logo                       =         models.ImageField(upload_to = "Client/logo/%Y-%M-%D")
    date_created                     =         models.DateTimeField(auto_now_add = True)
    registration_code                =         models.CharField(max_length = 50)

    def __unicode__(self):
        return '%s '  %(self.user)




class Address(models.Model):
    address         = 		models.TextField(max_length=300, null=True)
    city            = 		models.CharField(max_length=100, null=True)
    state           = 		models.CharField(max_length=50, null=True)
    country         = 		models.CharField(max_length=20, null=True, choices = COUNTRIES)
    created_on      = 		models.DateTimeField(auto_now_add = True)

    class Meta:
      verbose_name_plural = "Address"

    def __unicode__(self):
    	return self.address




class LatestNews(models.Model):
  topic                 =           models.CharField(max_length = 200)
  news_content          =           models.CharField(max_length = 300)
  date_added            =           models.DateTimeField(auto_now_add = True)
  posted_by             =           models.ForeignKey(User)

  def __unicode__(self):
    return '%s' %(self.topic)



class ClientFeedback(models.Model):
  sender     =   models.CharField(max_length = 125)
  email      =   models.CharField(max_length = 225)
  subject    =   models.CharField(max_length = 225)
  message    =   models.TextField(max_length = 1000)
  date_sent  =   models.DateTimeField(auto_now = True)
  status     =   models.CharField(max_length = 20, choices = FEEDBACK_STATUS, default = "Open")


  def __unicode__(self):
    return self.sender.upper()




class PwResetRecord(models.Model):
    user            =       models.OneToOneField(User)
    reset_code      =       models.CharField(max_length = 50)
    expired         =       models.BooleanField    (default = False)
    date_sent       =       models.DateTimeField(auto_now = False, auto_now_add = True)


    def __unicode__(self):
        return '%s, %s'  %(self.user, self.expired)


class ServiceCategory(models.Model):
  name          =    models.CharField(max_length = 175, choices = SERVICE_TYPE, default = "Press Release Distribution")
  name_slug     =    models.CharField(max_length = 175)
  description   =    models.TextField(max_length = 1000)


  def __unicode__(self):
    return '%s' %(self.name)


  def save(self, *args, **kwargs):
    self.name_slug = slugify(self.name)
    super(ServiceCategory, self).save(*args, **kwargs)


class ServiceItem(models.Model):
  category           =    models.ForeignKey(ServiceCategory)
  name               =    models.CharField(max_length = 150, choices = SERVICE_ITEM)
  name_slug          =    models.CharField(max_length = 175)
  image              =    models.FileField(upload_to ='services_image', null = True, blank = True)
  description        =    models.TextField(max_length = 750)
  call_to_action     =    models.CharField(max_length = 75, null = True, blank = True)
  icon_text          =    models.CharField(max_length = 75, null = True, blank = True)
  action_type        =    models.CharField(max_length = 175, choices = ACTION_TYPE, default = "")
  active             =    models.BooleanField(default = False)  


  def __unicode__(self):
    return '%s - %s' %(self.category, self.name)


  def save(self, *args, **kwargs):
    self.name_slug = slugify(self.name)
    super(ServiceItem, self).save(*args, **kwargs)


class MailingList(models.Model):
  email    =    models.CharField(max_length = 175)

  def __unicode__(self):
    return '%' %(self.email)




# def save(self, *args, **kwargs):
#     self.name_slug  = slugify(self.name)

#     amount_to_pay_N = self.price_per_media_N * self.num_of_media
#     amount_to_pay_D = self.price_per_media_D * self.num_of_media

#     if amount_to_pay_N > amount_payable_N:
#       saved_N = (amount_to_pay_N - amount_payable_N)

#       self.percentage_savings = (saved_N/amount_payable_N) * 100
#     super(Bouquet, self).save(*args, **kwargs)












