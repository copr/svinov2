from django.conf.urls import include, url
from home.views import api_views

urlpatterns = [
    url(r'^api/article/(?P<article_id>\d+)/$', api_views.article ),
]
