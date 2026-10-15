from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import (
    Conductor,
    Taller,
    TipoMantencion,
    Vehiculo,
    AsignacionVehiculo,
    Mantencion,
    Incidencia,
    HistorialEstadoVehiculo,
)

from .serializer import (
    ConductorSerializer,
    TallerSerializer,
    TipoMantencionSerializer,
    VehiculoSerializer,
    AsignacionVehiculoSerializer,
    MantencionSerializer,
    IncidenciaSerializer,
    HistorialEstadoVehiculoSerializer,
)

# Create your views here.
def inicio(request):
    return render(request, 'vehiculos/inicio.html')

@login_required
def dashboard(request):
    return render(request, 'vehiculos/dashboard.html')

class PanelVehiculosView(LoginRequiredMixin, TemplateView):
    template_name = 'vehiculos/panel_vehiculos.html'

class ProtectedModelViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]


class ConductorViewSet(ProtectedModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer


# Talleres
class TallerViewSet(ProtectedModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer


# Tipos de mantención
class TipoMantencionViewSet(ProtectedModelViewSet):
    queryset = TipoMantencion.objects.all()
    serializer_class = TipoMantencionSerializer


# Vehículos
class VehiculoViewSet(ProtectedModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


# Asignaciones de vehículos
class AsignacionVehiculoViewSet(ProtectedModelViewSet):
    queryset = AsignacionVehiculo.objects.all()
    serializer_class = AsignacionVehiculoSerializer


# Mantenciones
class MantencionViewSet(ProtectedModelViewSet):
    queryset = Mantencion.objects.all()
    serializer_class = MantencionSerializer


# Incidencias
class IncidenciaViewSet(ProtectedModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer


# Historial de estados
class HistorialEstadoVehiculoViewSet(ProtectedModelViewSet):
    queryset = HistorialEstadoVehiculo.objects.all()
    serializer_class = HistorialEstadoVehiculoSerializer
