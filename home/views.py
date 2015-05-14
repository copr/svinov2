# -*- coding: utf-8 -*-
from django.shortcuts import render
from home.models import Section, SubSection

def home(request):
    sections = Section.objects.all()
    l = []
    for section in sections:
        subsections = SubSection.objects.filter(section=section)
        d = {'name': section.name,
             'subsections': subsections}
        l.append(d)
    return render(request, 'index.html', {'sections': l})


