from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register("conductores", views.ConductorViewSet)
router.register("talleres", views.TallerViewSet)
router.register("tipos-mantencion", views.TipoMantencionViewSet)
router.register("vehiculos", views.VehiculoViewSet)
router.register("asignaciones", views.AsignacionVehiculoViewSet)
router.register("mantenciones", views.MantencionViewSet)
router.register("incidencias", views.IncidenciaViewSet)
router.register("historial-estados", views.HistorialEstadoVehiculoViewSet)

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("api/", include(router.urls)),
]
