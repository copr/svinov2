import re

from django import template

register = template.Library()

@register.filter(name='filter_html')
def filter_html(text):
    return re.sub('<.*?>', '', text)

@register.filter(name='og_image')
def filter_html(text):
    p = re.compile('(https?://[^/\s]+/\S+\.jpg|png|gif)')
    k = re.compile('(/media/[^/\s]+/\S+\.jpg|png|gif)')
    media_urls = k.findall(text)
    img_urls = p.findall(text)
    tags = ""
    for url in img_urls:
        tags += "<meta property='og:image' content='" + url +  "'/>"
    for url in media_urls:
        tags += "<meta property='og:image' content='http://sdhsvinov.cz" + url +  "'/>"
    return text + tags

