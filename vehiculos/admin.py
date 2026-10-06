from django.contrib import admin
from .models import Conductor
from .models import Taller
from .models import TipoMantencion
from .models import Vehiculo
from .models import AsignacionVehiculo
from .models import Mantencion
from .models import Incidencia
from .models import HistorialEstadoVehiculo
# Register your models here.

admin.site.register(Conductor)
admin.site.register(Taller)
admin.site.register(TipoMantencion)
admin.site.register(Vehiculo)
admin.site.register(AsignacionVehiculo)
admin.site.register(Mantencion)
admin.site.register(Incidencia)
admin.site.register(HistorialEstadoVehiculo)