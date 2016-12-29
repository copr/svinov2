from django.db import models
from django.core.exceptions import ValidationError

class Event(models.Model):
    ''' model co by mel reprezentovat, kazdou akci na kterou se budou prodavat vstupenky'''
    name = models.CharField(max_length = 100, verbose_name="Název")
    price = models.IntegerField(verbose_name="Základní cena")
    organizer_mail = models.EmailField(verbose_name="Mail organizátora")

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
    PAYMENT_METHODS = (
        (MONEYTRANSFER, 'Převodem na účet'),
    )
    STATES_OF_PAYMENT = (
        (NOTPAID, 'Neuhrazeno'),
        (PARTPAID, 'Částečne uhrazeno'),
        (PAID, 'Uhrazeno'),
    )
    name = models.CharField(max_length = 100, verbose_name='Jméno')
    surname = models.CharField(max_length = 100, verbose_name='Příjmení')
    phone_number = models.CharField(max_length = 100, verbose_name='Telefon')
    email = models.EmailField()
    number_of_tickets = models.IntegerField(verbose_name='Počet lístků')
    payment_method = models.IntegerField(choices=PAYMENT_METHODS,
                                         verbose_name='Platební metoda')
    note = models.TextField(verbose_name='Poznámka')
    state_of_payment = models.IntegerField(default=0, choices=STATES_OF_PAYMENT,
                                           verbose_name='Stav platby')
    pdf = models.FileField(blank=True,null=True, verbose_name="pdf")
    ticket_sent = models.BooleanField(default=False, verbose_name='Lístek odeslán')
    event = models.ForeignKey(Event, verbose_name='Událost')

    def __str__(self):
        return "listek " + self.name + ' '  + self.surname

    class Meta:
        verbose_name = "Vstupenka"
        verbose_name_plural = "Vstupenky"


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
    
    def event_check(self):
        ''' checkuje jestli ticket field odpovidat nastavenim u eventu '''
        event_tied_to_ticket = self.ticket.event
        event_fields_tied_to_event = EventField.objects.filter(event=event_tied_to_ticket)
        boo = []
        for e in event_fields_tied_to_event:
            boo.append(e.name == self.name and e.price == self.price)
        if not any(boo):
            raise ValidationError('Možnosti u tohle lístku nejsou stejné,jako u události')

    def count_check(self):
        ''' checkuje jestli pocet vybranych "obedu" je <= #tickets '''
        ticket_fields = TicketField.objects.filter(ticket=self.ticket)
        # :D
        sum_of_cunts = 0
        for t in ticket_fields:
            sum_of_cunts += t.count
        if sum_of_cunts + self.count > self.ticket.number_of_tickets:
            raise ValidationError('Víc položek než lístků')
        
    def clean(self):
        ''' tohle je v django administraci '''
#        print(self.cleaned_data)
        # self.event_check()
        # self.count_check()

    
    def save(self, *args, **kwargs):
        ''' tohle se vola vzdy prii ukladani '''
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


