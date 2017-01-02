from django import forms

from eticket.models import Ticket, TicketField

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
    ticket_fields = forms.CharField(queryset=TicketField.objects.all())
    
