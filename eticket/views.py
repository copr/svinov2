# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core import serializers
from django.utils.safestring import mark_safe
from django.http import HttpResponseRedirect
from django.http import Http404
import json

from eticket.models import Event, EventField, EventEmail, Ticket
from utils.getters import *
from eticket.utils import send_summary_mail

def form(request, event):
    event = Event.objects.get(url=event)
    if event.sold_out:
        raise Http404()
    sections = get_sections('index')
    invitations = get_invitations()
    posts = get_all_posts()
    calendars = get_calendars('index')
    sponsors = get_sponsors()
    contacts = get_contacts()
    event_fields = EventField.objects.filter(event=event)
    js_event = mark_safe(serializers.serialize("json", [event]))
    js_event_fields = mark_safe(serializers.serialize("json", event_fields))
    if request.method == 'POST':
        d = request.POST
        print(d)
        ticket = Ticket(name=d['name'],
                        surname=d['surname'],
                        phone_number=d['phone_number'],
                        email=d['email'],
                        number_of_tickets=d['number_of_tickets'],
                        note=d['note'],
                        payment_method = Ticket.MONEYTRANSFER,
                        state_of_payment=Ticket.NOTPAID,
                        ticket_sent = False,
                        event=event)
        ticket.save()
        organizer_mails = EventEmail.objects.filter(event=ticket.event).values_list('mail', flat=True)
        send_summary_mail(ticket.email, list(organizer_mails), ticket)
        print(ticket)
        price = int(ticket.number_of_tickets)*event.price
        return render(request, 'summary.html', {'sections': sections,
                                                'posts': posts,
                                                'current_section': '',
                                                'invitations': invitations,
                                                'calendars': calendars,
                                                'sponsors': sponsors,
                                                'contacts': contacts,
                                                'event': js_event,
                                                'event_fields': js_event_fields,
                                                'ticket': ticket,
                                                'price': price})
    else:
        return render(request, 'form.html', {'sections': sections,
                                             'posts': posts,
                                             'current_section': '',
                                             'invitations': invitations,
                                             'calendars': calendars,
                                             'sponsors': sponsors,
                                             'contacts': contacts,
                                             'event': js_event,
                                             'event_fields': js_event_fields})
    
