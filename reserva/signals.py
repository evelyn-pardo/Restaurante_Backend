from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Reserva

@receiver(post_save, sender=Reserva)
def enviar_email_confirmacion(sender, instance, created, **kwargs):
    if created:
        asunto = "Confirmación de reserva"
        mensaje = f"Estimado/a {instance.nombre} {instance.apellido},\n\n" \
                  f"Su reserva para el {instance.fecha} a las {instance.hora} ha sido confirmada.\n\n" \
                  f"Gracias por elegirnos."
        destinatario = [instance.email]
        
        send_mail(
            asunto,
            mensaje,
            'tucorreo@gmail.com',  # Correo remitente
            destinatario,
            fail_silently=False,
        )
