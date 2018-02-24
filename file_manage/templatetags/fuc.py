from django.template import Library
from django.utils.safestring import mark_safe



register = Library()

@register.simple_tag
def formatter_datetime(time_obj):
		s ='%s-%s-%s  %s:%s:%s'%(time_obj.year,time_obj.month,time_obj.day,time_obj.hour,time_obj.minute,time_obj.second)
		return mark_safe(s)



@register.simple_tag
def return_model_name(qs):
	model_name = qs._meta.label
	model_name = model_name.rsplit('.')[1]
	return model_name


