
from rest_framework import serializers
from .models import Mesa, Menu, Reserva

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = '__all__'  

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.foto and request:
            return request.build_absolute_uri(obj.foto.url)
        return ''
    
class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

    def validate(self, data):
        # Verificación de reservas duplicadas
        fecha = data.get('fecha')
        hora = data.get('hora')
        mesa_id = data.get('mesa')

        if Reserva.objects.filter(fecha=fecha, hora=hora, mesa_id=mesa_id).exists():
            raise serializers.ValidationError("Ya existe una reserva para esta fecha, hora y mesa.Elija otra mesa")

        return data

    def validate_telefono(self, value):
        if len(value) != 10:
            raise serializers.ValidationError("Por favor, ingrese un número de teléfono válido que contenga exactamente 10 dígitos.")
        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("El correo electrónico es obligatorio.")
        return value