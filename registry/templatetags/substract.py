from django import template

register = template.Library()


@register.filter
def substract(value):
	return value - 3
