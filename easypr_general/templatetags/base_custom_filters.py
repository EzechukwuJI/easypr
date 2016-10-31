from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()



@register.filter
def strip_chars(value, char):
	return value.replace(char, " ")