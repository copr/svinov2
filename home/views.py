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
    return render(request, 'pozvanky.html', {'sections': sections, 'posts': posts, 'size': 1/len(sections)*PERCENT,
                                             'current_section': '', 'invitations': invitations})

def section(request, section):
    sections = get_sections(section)
    posts = get_posts(section)
    cur_section = Section.objects.get(name=section)
    return render(request, 'front_page.html', {'sections': sections, 'posts': posts, 'size': 1/len(sections)*PERCENT,
                                               'current_section': cur_section})

def static(request, section, static):
    sections = get_sections(section)
    static = get_static(static)
    cur_section = Section.objects.get(name=section)
    if cur_section.name == 'index':
        print('name == index')
        cur_section = {'name': '', 'url': 'index'}
    return render(request, 'static.html', {'sections': sections, 'article': static, 'size': 1/len(sections)*PERCENT,
                                            'current_section': cur_section})

def news_from_front(request):
    sections = get_sections('index')
    posts = get_all_posts()
    cur_section = Section.objects.get(name=section)
    return render(request, 'news.html', {'sections': sections, 'posts': posts, 'size': 1/len(sections)*PERCENT, 
                                         'current_section': cur_section})

def news(request, section):
    sections = get_sections(section)
    posts = get_posts(section)
    cur_section = Section.objects.get(name=section)
    return render(request, 'news.html', {'sections': sections, 'posts': posts, 'size': 1/len(sections)*PERCENT,
                                         'current_section': cur_section})

def article(request, section, article_id):
    sections = get_sections(section)
    article = get_article(article_id)
    cur_section = Section.objects.get(name=section)
    return render(request, 'article.html', {'sections': sections, 'article': article, 'size': 1/len(sections)*PERCENT,
                                            'current_section': cur_section})


def article_from_front(request, article_id): 
    return article(request, 'index', article_id)
