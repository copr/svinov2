from django.db import models
from django.core.exceptions import ValidationError

class Event(models.Model):
    ''' model co by mel reprezentovat, kazdou akci na kterou se budou prodavat vstupenky'''
    name = models.CharField(max_length = 100, verbose_name="Název")
    price = models.IntegerField(verbose_name="Základní cena")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Akce"
        verbose_name_plural = "Akce"

class EventField(models.Model):
    ''' 
    reprezentuje moznosti, ktere budou nabidnuty uzivateli, na jidlo atd
    definuje se pres samoutnou udalost/akci
    '''
    name = models.CharField(max_length = 100, verbose_name="Název")
    price = models.IntegerField(verbose_name="Cena")
    event = models.ForeignKey(Event)

class Ticket(models.Model):
    '''
    samotna vstupenka, ta by se mela vytvare pres formular nekde na strankach
    pri ulozeni se odesle mail, ve kterem bude cela objednavka shrnuta 
    '''
    NOTPAID = 0
    PARTPAID = 1
    PAID = 2
    MONEYTRANSFER = 0
    PURCHASE_METHODS = (
        (MONEYTRANSFER, 'Převodem na účet'),
    )
    STATES_OF_PAYMENT = (
        (NOTPAID, 'Neuhrazeno'),
        (PARTPAID, 'Částečne uhrazeno'),
        (PAID, 'Uhrazeno'),
    )
    name = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 100)
    email = models.EmailField()
    number_of_tickets = models.IntegerField()
    note = models.TextField()
    state_of_payment = models.IntegerField(default=0, choices=STATES_OF_PAYMENT)
    send_ticket = models.BooleanField(default=False)
    event = models.ForeignKey(Event)

    def __str__(self):
        return "listek " + self.name + ' '  + self.surname

    class Meta:
        verbose_name = "Vstupenka"
        verbose_name_plural = "Vstupenky"

    # TODO: udelat check na #fields musi byt <= number_of_tickets

class TicketField(models.Model):
    '''
    reprezentuje moznosti ktere si vybere konkretni uzivatel treba jidlo atd
    uz z danych moznosti, ty by se mely brat z ticket.event."eventfields"
    '''
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    # pocet kolikrat chci tu danou moznost
    count = models.IntegerField()
    ticket = models.ForeignKey(Ticket)
    
    # TODO: name, price musi byt v ticket.event."eventfield"
    def event_check(self):
        event_tied_to_ticket = self.ticket.event
        event_fields_tied_to_event = EventField.objects.filter(event=event_tied_to_ticket)
        boo = []
        for e in event_fields_tied_to_event:
            boo.append(e.name == self.name and e.price == self.price)
        if not any(boo):
            raise ValidationError('Možnosti u tohle lístku nejsou stejné,jako u události')

    def count_check(self):
        ticket_fields = TicketField.objects.filter(ticket=self.ticket)
        # :D
        sum_of_cunts = 0
        for t in ticket_fields:
            sum_of_cunts += t.count
        if sum_of_cunts + self.count > self.ticket.number_of_tickets:
            raise ValidationError('Víc položek než lístků')
        
    def clean(self):
        self.event_check()
        self.count_check()
    
    def save(self, *args, **kwargs):
        self.event_check()
        self.count_check()
        super(TicketField, self).save(*args, **kwargs)

   

class OrganizerTicketField(models.Model):
    '''
    reprezentuje nejak dodatecne informace, ktere prida organizator 
    treba cislo stolu
    '''
    text = models.CharField(max_length = 100)
    ticket = models.ForeignKey(Ticket)


