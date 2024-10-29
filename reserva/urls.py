from django.urls import path, include
from rest_framework import routers

from restaurante import settings
from .views import MesaViewSet, MenuViewSet, ReservaViewSet
from django.conf.urls.static import static

# Crear un enrutador y registrar los viewsets
router = routers.DefaultRouter()
router.register(r'mesa', MesaViewSet, basename='mesa')   # Eliminar 'api/' del registro
router.register(r'menu', MenuViewSet, basename='menu')   # Eliminar 'api/' del registro
router.register(r'reservas', ReservaViewSet, basename='reservas')  # Eliminar 'api/' del registro

# Las URLs de la API se determinan automáticamente en función del enrutador
urlpatterns = [
    path('api/', include(router.urls)),  # Prefijo 'api/' para todas las rutas
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)