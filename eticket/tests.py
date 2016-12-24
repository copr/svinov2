from django.test import TestCase
from django.core.exceptions import ValidationError
from eticket.models import *

class ModelTestCase(TestCase):
    def setUp(self):
        self.testEvent = Event(name='Test', price=100)
        self.testEvent.save()
        EventField.objects.create(name='obed1',
                                  price=100,
                                  event=self.testEvent)

        self.ticket = Ticket(name='pepa',
                             surname='zdepa',
                             phone_number='423423',
                             email='asf@fasd.cz',
                             number_of_tickets=5,
                             note='',
                             event=self.testEvent)
        self.ticket.save()

    def test_ticketfield_conforms_to_event_save1(self):
        ''' Checkuje jestli je ticketfield ve shode s 
        nastavenim udalosti'''
        tf = TicketField(name='obed1',
                         price=100,
                         count=5,
                         ticket=self.ticket)
        tf.save()

    def test_ticketfield_conforms_to_event_save2(self):
        tf = TicketField(name='neco',
                         price=100,
                         count=5,
                         ticket=self.ticket)
        self.assertRaises(ValidationError, tf.save)

    def test_ticketfield_conforms_to_event_save3(self):
        tf = TicketField(name='obed1',
                         price=200,
                         count=5,
                         ticket=self.ticket)
        self.assertRaises(ValidationError, tf.save)

    def test_ticketfield_conforms_to_event_save4(self):
        tf = TicketField(name='ob',
                         price=20,
                         count=5,
                         ticket=self.ticket)
        self.assertRaises(ValidationError, tf.save)

    def test_ticketfield_not_more_than_count(self):
        tf = TicketField(name='obed1',
                         price=100,
                         count=6,
                         ticket=self.ticket)
        self.assertRaises(ValidationError, tf.save)

    def test_ticketfield_not_more_than_count(self):
        tf1 = TicketField(name='obed1',
                          price=100,
                          count=4,
                          ticket=self.ticket)
        tf1.save()
        tf2 = TicketField(name='obed1',
                          price=100,
                          count=2,
                          ticket=self.ticket)
        self.assertRaises(ValidationError, tf2.save)
