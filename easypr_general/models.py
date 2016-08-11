from django.contrib.sites.models import Site
# import timezone
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User 
from models_field_choices import TITLE, COUNTRIES, FEEDBACK_STATUS
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

