# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.core import serializers

from utils.getters import *

def serialize_send(request, data):
    d = serializers.serialize('json', data)
    return HttpResponse(d, content_type='application/json')

def article(request, article_id):
    data  = get_article_safe(article_id)
    return serialize_send(request, data)

def posts_by_section(request, section):
    data = get_posts(section)
    return serialize_send(request, data)

def sections_by_section(request, section):
    data = get_sections(section)
    return serialize_send(request, data)

def all_posts(request):
    data = get_all_posts()
    return serialize_send(request, data)

def columns(request, section):
    data = get_columns(section)
    return serialize_send(request, data)

def statics(request, section):
    data = get_statics(section)
    return serialize_send(request, data)

def banner(request, section):
    data = get_banner(section)
    return serialize_send(request, data)

def concrete_static(request, static):
    data = get_static(static)
    return serialize_send(request, data)

def invitations(request):
    data = get_invitations()
    return serialize_send(request, data)

def news(request, main_section):
    data = get_news(main_section)
    return serialize_send(request, data)

def calendars(request, section):
    data = get_calendars(section)
    return serialize_send(request, data)

def sponsors(request):
    data = get_sponsors()
    return serialize_send(request, data)

def contacts(request):
    data = get_contacts()
    return serialize_send(request, data)
