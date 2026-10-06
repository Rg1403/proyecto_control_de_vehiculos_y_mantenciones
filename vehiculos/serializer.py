from rest_framework import serializers
from .models import Conductor
from .models import Taller
from .models import TipoMantencion
from .models import Vehiculo
from .models import AsignacionVehiculo
from .models import Mantencion
from .models import Incidencia
from .models import HistorialEstadoVehiculo


class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conductor
        fields = "__all__"


class TallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taller
        fields = "__all__"


class TipoMantencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMantencion
        fields = "__all__"


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = "__all__"


class AsignacionVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsignacionVehiculo
        fields = "__all__"


class MantencionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantencion
        fields = "__all__"


class IncidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidencia
        fields = "__all__"


class HistorialEstadoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEstadoVehiculo
        fields = "__all__"
        