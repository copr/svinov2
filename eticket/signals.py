from django.db.models.signals import post_save
from django.dispatch import receiver
from eticket.models import Ticket

# @receiver(post_save, sender=Ticket)
# def sendSummaryEmail(sender, instance, created, **kwargs):
 #   if created:
#        print("tady se posle mail se shrnutim objednavky")

@receiver(post_save, sender=Ticket)
def sendConfimationEmail(sender, instance, **kwargs):
    if instance.state_of_payment == 1:
        print("tady se posle mail, informujici o castecne zaplaceni")
    if instance.state_of_payment == 2:
        print("tady se posle mail, potvrzujici zaplaceni a s danovym dokladem")
