from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

@register.filter
def get_item(dictionary, key):
    if not dictionary:
        return ""
    return dictionary.get(key)

@register.filter
def format_like_currency(dictionary, key):
    if not dictionary:
        return ""
    amount = dictionary.get(key)
    dollars = round(float(amount), 2)
    return "$%s%s" % (intcomma(int(dollars)), ("%0.2f" % dollars)[-3:])