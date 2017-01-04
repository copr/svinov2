from django.contrib import admin

#pro ty tickety
from django.conf.urls import include, url
from django.utils.html import format_html
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.db.models import Sum

from eticket.models import *
from eticket.utils import render_to_pdf

class TicketFieldAdmin(admin.TabularInline):
    model = TicketField

class OrganizerTicketFieldAdmin(admin.TabularInline):
    model = OrganizerTicketField
    
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'email', 'number_of_tickets',
                    'payment_method', 'reserved_from', 'state_of_payment',
                    'event', 'ticket_sent', 'send_mail','total_count')
    exclude = ['ticket_sent']
    inlines = [
        TicketFieldAdmin, OrganizerTicketFieldAdmin,
    ]

    def total_count(self, request):
        count = Ticket.objects.all().aggregate(Sum('number_of_tickets'))
        return "Celkový počet lístků: " + str(count['number_of_tickets__sum'])

    def process_send_mail(self, request, ticket_id):
        ticket = Ticket.objects.get(id=ticket_id)
        print("posilam maila tady tomuhle panovi", ticket.name, ticket.surname)
        ticket.ticket_sent = True
        ticket.save()
        # z uri vezmu vsechno krome poslednich tri casti
        # neco jako /admin/eticket/ticket
        # pak to dam zas do kupy
        uri_parts = request.path.split('/')[:-3]
        url = "//"
        for u in uri_parts:
            url += u + '/'
        return redirect(url)

    def process_create_ticket(self, request, ticket_id):
        ticket = Ticket.objects.get(id=ticket_id)
        org_fields = OrganizerTicketField.objects.filter(ticket=ticket)
        render_to_pdf('listek.html',
                      {'ticket': ticket,
                       'organizer_fields': org_fields},
                      ticket.name + '_' + ticket.surname)
        uri_parts = request.path.split('/')[:-3]
        url = "//"
        for u in uri_parts:
            url += u + '/'
        return redirect(url)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            url(
                r'^(?P<ticket_id>.+)/send/$',
                self.admin_site.admin_view(self.process_send_mail),
                name='send-mail',
            ),
            url(
                r'^(?P<ticket_id>.+)/create_ticket/$',
                self.admin_site.admin_view(self.process_create_ticket),
                name='create-ticket',
            ),
        ]
        return custom_urls + urls

    def send_mail(self, obj):
        disabled = "disabled"
        if obj.ticket_sent:
            disabled = "disabled"
        return format_html(
            '<a class="button" href="{}" {}>Poslat lístek</a>&nbsp' +
            '<a class="button" href="{}" {}>Vytvořit lupen</a>&nbsp;',
            '', disabled, '', disabled
            #reverse('admin:send-mail', args=[obj.pk]), disabled,
            #reverse('admin:create-ticket', args=[obj.pk]), disabled
        )
    send_mail.short_description = 'Poslat maila'
    send_mail.allow_tags = True

class EventEmailAdmin(admin.TabularInline):
    model = EventEmail

class EventFieldAdmin(admin.TabularInline):
    model = EventField
    
class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventEmailAdmin,
        EventFieldAdmin,
    ]

admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
