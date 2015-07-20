import re

from django import template

register = template.Library()

@register.filter(name='filter_html')
def filter_html(text):
    return re.sub('<.*?>', '', text)

