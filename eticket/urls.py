from django.conf.urls import include, url
import eticket.views as views

urlpatterns = [
    url(r'^formy', views.form),
]
