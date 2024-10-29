from django.apps import AppConfig
from django.apps import AppConfig

class ReservaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reserva'



class ReservaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reserva'

    def ready(self):
        import reserva.signals  # Importa las señales
