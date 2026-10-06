from django.shortcuts import render
from rest_framework import viewsets

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


class ConductorViewSet(viewsets.ModelViewSet):
    queryset = Conductor.objects.all()
    serializer_class = ConductorSerializer


class TallerViewSet(viewsets.ModelViewSet):
    queryset = Taller.objects.all()
    serializer_class = TallerSerializer


class TipoMantencionViewSet(viewsets.ModelViewSet):
    queryset = TipoMantencion.objects.all()
    serializer_class = TipoMantencionSerializer


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer


class AsignacionVehiculoViewSet(viewsets.ModelViewSet):
    queryset = AsignacionVehiculo.objects.all()
    serializer_class = AsignacionVehiculoSerializer


class MantencionViewSet(viewsets.ModelViewSet):
    queryset = Mantencion.objects.all()
    serializer_class = MantencionSerializer


class IncidenciaViewSet(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer


class HistorialEstadoVehiculoViewSet(viewsets.ModelViewSet):
    queryset = HistorialEstadoVehiculo.objects.all()
    serializer_class = HistorialEstadoVehiculoSerializer
    