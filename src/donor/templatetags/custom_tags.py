from django import template
register = template.Library()



@register.filter()
def uppercase(blood_group):
    return blood_group.upper()