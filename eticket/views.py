from django.shortcuts import render
from django.core import serializers
from django.utils.safestring import mark_safe
import json

from eticket.models import Event

def form(request):
    results = [Event.objects.all()[0]]
    js_data = mark_safe(serializers.serialize("json",results))
    return render(request, 'form.html', {'event': js_data})
