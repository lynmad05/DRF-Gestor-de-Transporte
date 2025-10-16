from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RutaViewSet, ConductorViewSet

router = DefaultRouter()
router.register(r'rutas', RutaViewSet)
router.register(r'conductores', ConductorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
