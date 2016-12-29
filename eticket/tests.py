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
                             payment_method=Ticket.MONEYTRANSFER,
                             note='',
                             state_of_payment=Ticket.NOTPAID,
                             event=self.testEvent)
        self.ticket2 = Ticket(name='slavoj',
                             surname='zizek',
                             phone_number='423423',
                             email='ml@mlm.cz',
                             number_of_tickets=2,
                             payment_method=Ticket.MONEYTRANSFER,
                             note='',
                             state_of_payment=Ticket.NOTPAID,
                             event=self.testEvent)
        self.ticket.save()
        self.ticket2.save()

    def test_ticketfield_conforms_to_event_save0(self):
        ''' Checkuje jestli je ticketfield ve shode s 
        nastavenim udalosti'''
        tf = TicketField(name='obed1',
                         price=100,
                         count=1,
                         ticket=self.ticket)
        tf.save()

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

    # def test_ticketfield_conforms_to_event_clean0(self):
    #     ''' Checkuje jestli je ticketfield ve shode s 
    #     nastavenim udalosti'''
    #     tf = TicketField(name='obed1',
    #                      price=100,
    #                      count=1,
    #                      ticket=self.ticket)
    #     tf.clean()

    # def test_ticketfield_conforms_to_event_clean1(self):
    #     ''' Checkuje jestli je ticketfield ve shode s 
    #     nastavenim udalosti'''
    #     tf = TicketField(name='obed1',
    #                      price=100,
    #                      count=5,
    #                      ticket=self.ticket)
    #     tf.clean()

    # def test_ticketfield_conforms_to_event_clean2(self):
    #     tf = TicketField(name='neco',
    #                      price=100,
    #                      count=5,
    #                      ticket=self.ticket)
    #     self.assertRaises(ValidationError, tf.clean)

    # def test_ticketfield_conforms_to_event_clean3(self):
    #     tf = TicketField(name='obed1',
    #                      price=200,
    #                      count=5,
    #                      ticket=self.ticket)
    #     self.assertRaises(ValidationError, tf.clean)

    # def test_ticketfield_conforms_to_event_clean4(self):
    #     tf = TicketField(name='ob',
    #                      price=20,
    #                      count=5,
    #                      ticket=self.ticket)
    #     self.assertRaises(ValidationError, tf.clean)

    # def test_ticketfield_not_more_than_count_clean1(self):
    #     tf = TicketField(name='obed1',
    #                      price=100,
    #                      count=6,
    #                      ticket=self.ticket)
    #     self.assertRaises(ValidationError, tf.clean)

    # def test_ticketfield_not_more_than_count_clean2(self):
    #     tf1 = TicketField(name='obed1',
    #                       price=100,
    #                       count=4,
    #                       ticket=self.ticket)
    #     tf1.clean()
    #     tf2 = TicketField(name='obed1',
    #                       price=100,
    #                       count=2,
    #                       ticket=self.ticket)
    #     self.assertRaises(ValidationError, tf2.clean)

    # def test_count_check(self):
    #     ''' bug, co mi vyskakuje v adminsitraci haze to chybu
    #     "vic polozek nez listku", ale obed je zvolen jen jeden
    #     i kdyz listky jsou dva'''
    #     tf1 = TicketField(name='obed1',
    #                       price=100,
    #                       count=1,
    #                       ticket=self.ticket2)
    #     tf1.clean()
