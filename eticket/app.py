from django.apps import AppConfig

class EticketConfig(AppConfig):
    name = 'eticket'
    def ready(self):
        import eticket.signals  # uvidime
