from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib.auth import views as auth_views

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

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    path("dashboard/", views.dashboard, name="dashboard"),

    path(
        "vehiculos-panel/",
        views.PanelVehiculosView.as_view(),
        name="vehiculos_panel",
    ),

    path("api/", include(router.urls)),
]
