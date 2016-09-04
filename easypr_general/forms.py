from django import forms
from django.contrib.auth.models import User

from easypr_ng.models import *
from easypr_general.models import *
from easypr_general.models_field_choices import *
# from multiupload.fields import MultiFileField





class UserRegistrationForm(forms.ModelForm):
	first_name      =    forms.CharField(max_length = 128, help_text = "",widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'First Name', 'required':'required'}))
	last_name       =    forms.CharField(max_length = 128, help_text = "",widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Last Name', 'required':'required'}))
	email           =    forms.EmailField(max_length = 128, help_text = "",widget=forms.EmailInput(attrs={'class' : 'form-control', 'placeholder': 'Email','required':'required'}))
	password        =    forms.CharField(max_length=15, widget=forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder':'Password','required':'required'}))
	
	class Meta:
		model = User
		fields =  ('first_name','last_name','email','password')



class UserProfileForm(forms.ModelForm):
	title       			=       forms.ChoiceField(widget=forms.Select(choices = TITLE, attrs={'class' : 'form-control', 'required':'required'}))       
	company_name      		=    	forms.CharField(max_length = 128, help_text = "",widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'First Name', 'required':'required'}))
	economy_sector     		=       forms.ChoiceField(widget=forms.Select(choices = ECONOMY_SECTOR, attrs={'class' : 'form-control', 'required':'required'}))
	phone_no                =       forms.CharField(max_length = 128, help_text = "",widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Phone Number', 'required':'required'}))
	website                 =       forms.CharField(max_length = 128, help_text = "",widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Phone Number', 'required':'required'}))
	address                 =       forms.CharField(max_length = 128, help_text = "",widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Phone Number', 'required':'required'}))


	class Meta:
		model = UserAccount
		fields   =   ('title','company_name','economy_sector','phone_no','website','address',)




class LoginForm(forms.ModelForm):
	email = forms.EmailField(max_length = 128, help_text = "",widget=forms.TextInput
		(attrs={'class':'form-control','placeholder': 'Email','autofocus':'autofocus','required':'required'}))

	password = forms.CharField(max_length=10,required=True, widget=forms.PasswordInput
		(attrs={'class' : 'form-control','placeholder':'Password','required':'required'}))
	
	class Meta:
		# Associate form with a model
		model = User
		fields = ('email','password',)




		