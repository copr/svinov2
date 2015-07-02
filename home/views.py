# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse

from utils.getters import *

#TODO sections je spatny nazev pro vsechny lepsi je asi neco jako clenove menu
#TODO to co je ted sections posilat jako nejakou strukturu ve ktere jsou zvlast jmena na zobrazeni a zvlast urls

PERCENT = 100

def index(request):
    sections = get_sections('index')
    invitations = get_invitations()
    posts = get_all_posts()
    calendars = get_calendars('index')
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'pozvanky.html', {'sections': sections, 'posts': posts, 'size': 1/len(sections)*PERCENT,
                                             'current_section': '', 'invitations': invitations, 'calendars': calendars,
                                             'sponsors': sponsors, 'contacts': contacts})

def section(request, section):
    sections = get_sections(section)
    posts = get_posts(section)
    cur_section = get_current_section(section)
    calendars = get_calendars(section)
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'front_page.html', {'sections': sections, 'posts': posts, 'size': 1/len(sections)*PERCENT,
                                               'current_section': cur_section, 'calendars': calendars, 'sponsors': sponsors,
                                               'contacts': contacts})

def static(request, section, static):
    sections = get_sections(section)
    static = get_static(static)
    cur_section = get_current_section(section)
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'static.html', {'sections': sections, 'article': static, 'size': 1/len(sections)*PERCENT,
                                           'current_section': cur_section, 'sponsors': sponsors, 'contacts': contacts})

def news_from_front(request):
    sections = get_sections('index')
    posts = get_all_posts()
    cur_section = get_current_section('index')
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'news.html', {'sections': sections, 'posts': posts, 'size': 1/len(sections)*PERCENT, 
                                         'current_section': cur_section, 'sponsors': sponsors, 'contacts': contacts})

def news(request, section):
    sections = get_sections(section)
    posts = get_posts(section)
    cur_section = get_current_section(section)
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'news.html', {'sections': sections, 'posts': posts, 'size': 1/len(sections)*PERCENT,
                                         'current_section': cur_section, 'sponsors': sponsors, 'contacts': contacts})

def article(request, section, article_id):
    sections = get_sections(section)
    article = get_article(article_id)
    cur_section = get_current_section(section) 
    sponsors = get_sponsors()
    contacts = get_contacts()
    return render(request, 'article.html', {'sections': sections, 'article': article, 'size': 1/len(sections)*PERCENT,
                                            'current_section': cur_section, 'sponsors': sponsors, 'contacts': contacts})

def article_from_front(request, article_id): 
    return article(request, 'index', article_id)

def test(request):
    return render(request, 'test.html')
