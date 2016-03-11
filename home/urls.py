from django.conf.urls import patterns, include, url

from home.site_urls import urlpatterns as site_urls
from home.api_urls import urlpatterns as api_urls

urlpatterns = api_urls + site_urls


