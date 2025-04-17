from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, DestinoViewSet, TransporteViewSet, CategoriaViewSet, ViagemViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')
router.register(r'destinos', DestinoViewSet, basename='destino')
router.register(r'transportes', TransporteViewSet, basename='transporte')
router.register(r'categorias', CategoriaViewSet, basename='categoria')
router.register(r'viagens', ViagemViewSet, basename='viagem')

# Configuração do Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API de Viagens",
      default_version='v1',
      description="API para gerenciar usuários, destinos, transportes, categorias e viagens.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="fcasagrandi38@gmail.com"),
      license=openapi.License(name="Licença Stark Industries"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include(router.urls)),
]
