import re
from django.forms import ValidationError
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Mesa, Menu, Reserva
from .serializers import MesaSerializer, MenuSerializer, ReservaSerializer

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
    permission_classes = [AllowAny]

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]
    def get_serializer_context(self):
        return {'request': self.request}

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [AllowAny]

    def validate_phone(self, phone):
        phone_regex = r'^[0-9]{10}$'  # Regex para 10 dígitos
        if not re.match(phone_regex, phone):
            raise ValidationError("El número de teléfono debe contener exactamente 10 dígitos.")

    def validate_email(self, email):
        email_regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'  # Regex para validar formato de email
        if not re.match(email_regex, email):
            raise ValidationError("Por favor, introduce un correo electrónico válido.")

    def perform_create(self, serializer):
        # Validación del teléfono
        self.validate_phone(self.request.data.get('telefono'))
        
        # Validación del email
        self.validate_email(self.request.data.get('email'))

        # Verificación de reservas duplicadas
        fecha = self.request.data.get('fecha')
        hora = self.request.data.get('hora')
        mesa_id = self.request.data.get('mesa')

        if Reserva.objects.filter(fecha=fecha, hora=hora, mesa_id=mesa_id).exists():
            # Enviar un ValidationError que será manejado por DRF
            raise ValidationError({"error": "Ya existe una reserva para esta fecha, hora y mesa."})

        # Guardar la reserva si las validaciones pasan
        serializer.save()


