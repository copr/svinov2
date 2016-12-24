from django.contrib import admin

from eticket.models import *

class TicketFieldAdmin(admin.TabularInline):
    model = TicketField

class OrganizerTicketFieldAdmin(admin.TabularInline):
    model = OrganizerTicketField
    
class TicketAdmin(admin.ModelAdmin):
    inlines = [
        TicketFieldAdmin, OrganizerTicketFieldAdmin,
    ]

class EventFieldAdmin(admin.TabularInline):
    model = EventField
    
class EventAdmin(admin.ModelAdmin):
    inlines = [
        EventFieldAdmin,
    ]

admin.site.register(Event, EventAdmin)
admin.site.register(Ticket, TicketAdmin)
