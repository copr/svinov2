from django.shortcuts import render
from django.core import serializers
from django.utils.safestring import mark_safe
import json

from eticket.models import Event, EventField

def form(request):
    event = Event.objects.all()[0]
    event_fields = EventField.objects.filter(event=event)
    # d['event'] = event
    # d['event_fields'] = event_fields
    js_event = mark_safe(serializers.serialize("json", [event]))
    js_event_fields = mark_safe(serializers.serialize("json", event_fields))
    return render(request, 'form.html', {'event': js_event,
                                         'event_fields': js_event_fields})
