from django.conf.urls import include, url
from home.views import site_views as views

urlpatterns = [
    url(r'^react/$', views.react),
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^aktuality/$', views.news_from_front),
    url(r'^aktuality/(?P<article_id>\d+)/$', views.article_from_front),
    url(r'^aktuality/(?P<start>\d+)-(?P<end>\d+)/$', views.article_range_from_front),
    url(r'^aktuality/(?P<article_url>\w+)/$', views.article_from_front_by_url),
    url(r'^(?P<section>\w+)/$', views.section),
    url(r'^(?P<section>\w+)/kalendar/$', views.calendar),
    url(r'^(?P<section>\w+)/aktuality/$', views.news),
    url(r'^(?P<section>\w+)/aktuality/(?P<article_id>\d+)/$', views.article_by_id),
    url(r'^(?P<section>\w+)/aktuality/(?P<start>\d+)-(?P<end>\d+)/$', views.article_range),
    url(r'^(?P<section>\w+)/aktuality/(?P<article_url>\w+)/$', views.article_by_url),
    url(r'^(?P<section>\w+)/(?P<static>\w+)/$', views.static),
]
