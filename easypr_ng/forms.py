from django import forms
from django.contrib.auth.models import User
from easypr_ng.models import *
from easypr_general.models import *
from easypr_general.models_field_choices import *
# from multiupload.fields import MultiFileField




class ContentUploadForm(forms.ModelForm):
	post_title         =    forms.CharField(max_length = 200, widget=forms.TextInput(attrs=
					        {'class' : 'form-control no-border-radius title bg-white', 'placeholder': 'Enter post title', 'required':'required'}))	# platform       			 =    forms.CharField(max_length = 128, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Last Name', 'required':'required'}))
	person_to_quote    =    forms.CharField(max_length = 128, widget=forms.TextInput(attrs=
						    {'class' : 'form-control no-border-radius bg-white', 'placeholder': 'Person to quote', 'required':'required'}))
	persons_position   =    forms.CharField(max_length = 128, widget=forms.TextInput(attrs=
							{'class' : 'form-control no-border-radius bg-white', 'placeholder': 'Position', 'required':'required'}))
	# media_houses             =    forms.CharField(max_length = 128, widget=forms.Select(attrs={'class' : 'form-control', 'placeholder': 'Last Name', 'required':'required'}))
	post_body          =    forms.CharField(max_length = 3000, widget=forms.Textarea(attrs=
							{'class' : 'form-control no-border-radius bg-white', 'placeholder': 'Type or copy and paste content here', 'required':'required','rows':20}))
	publish_online     =    forms.CharField(max_length = 10, widget=forms.CheckboxInput(attrs={'value' : 'false'}))
	


	class Meta:
		model = Publication
		fields = ('post_title','person_to_quote', 'persons_position','post_body','publish_online',)





class BizInfoForm(forms.ModelForm):
	# business_type      =    forms.ModelChoiceField(queryset = BUSINESS_TYPE, widget=forms.Select(attrs={'class' : 'form-control no-border-radius title bg-white', 'required':'required'}))
	business_type      =    forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class' : 'form-control no-border-radius title bg-white', 'required':'required'}))
	company_type       =    forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class' : 'form-control no-border-radius title bg-white', 'required':'required'}))
	is_pr_agent        =    forms.CharField(max_length = 10, widget=forms.CheckboxInput(attrs={'value' : 'false'}))
	size_of_pr_team    =    forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class' : 'form-control no-border-radius title bg-white','required':'required'}))

	class Meta:
		model = PRStrategy
		fields  =  ('business_type','company_type','is_pr_agent','size_of_pr_team')



class TargetAudienceForm(forms.ModelForm):
	target_audience 	=       forms.CharField(max_length = 1000, widget=forms.Textarea(attrs=
							{'class' : 'form-control no-border-radius bg-white', 'required':'required','rows':20}))
	pr_goals        	=       	forms.CharField(max_length = 1000, widget=forms.Textarea(attrs=
									{'class' : 'form-control no-border-radius bg-white', 'required':'required','rows':20}))
	frequency_of_pr 	=       	forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class' : 'form-control no-border-radius title bg-white', 'required':'required'}))
	target_audience_location  =      forms.CharField(max_length = 200, widget=forms.TextInput(attrs={'class' : 'form-control no-border-radius title bg-white', 'required':'required'}))
   



	class Meta:
		model = PRStrategy
		fields = ('target_audience','pr_goals','frequency_of_pr','target_audience_location',)

















