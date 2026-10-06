from django.db import models
from django.conf import settings

# Create your models here.
str_nombre = "Nombre"
str_telefono = "Teléfono"
str_email = "Email"
str_habilitado = "Habilitado"
str_fecha_creacion = "Fecha Creación"
str_fecha_actualizacion = "Fecha Actualización"


class Conductor(models.Model):
    rut = models.CharField("RUT", max_length=12, null=False)
    nombre = models.CharField(str_nombre, max_length=100, null=False)
    telefono = models.CharField(str_telefono, max_length=20, null=True)
    correo = models.EmailField(str_email, null=True)
    licencia = models.CharField("Clase de Licencia", max_length=20, null=False)
    habilitado = models.BooleanField(
        str_habilitado, default=True, null=False
    )
    created_at = models.DateTimeField(
        str_fecha_creacion, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        str_fecha_actualizacion, auto_now=True
    )

    class Meta:
        db_table_comment = "Datos de conductores de la flota."


class Taller(models.Model):
    rut = models.CharField("RUT", max_length=12, null=False)
    nombre = models.CharField(str_nombre, max_length=100, null=False)
    direccion = models.CharField("Dirección", max_length=200, null=False)
    telefono = models.CharField(str_telefono, max_length=20, null=True)
    correo = models.EmailField(str_email, null=True)
    habilitado = models.BooleanField(
        str_habilitado, default=True, null=False
    )
    created_at = models.DateTimeField(
        str_fecha_creacion, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        str_fecha_actualizacion, auto_now=True
    )

    class Meta:
        db_table_comment = "Datos de talleres que realizan mantenciones."


class TipoMantencion(models.Model):
    nombre = models.CharField(str_nombre, max_length=100, null=False)
    descripcion = models.TextField("Descripción", null=True)
    habilitado = models.BooleanField(
        str_habilitado, default=True, null=False
    )
    created_at = models.DateTimeField(
        str_fecha_creacion, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        str_fecha_actualizacion, auto_now=True
    )

    class Meta:
        db_table_comment = "Tipos de mantenciones de vehículos."

class Vehiculo(models.Model):
    patente = models.CharField("Patente", max_length=10, null=False)
    marca = models.CharField("Marca", max_length=50, null=False)
    modelo = models.CharField("Modelo", max_length=50, null=False)
    anio = models.IntegerField("Año", null=False)
    kilometraje = models.IntegerField(
        "Kilometraje", default=0, null=False
    )
    estado = models.CharField(
        "Estado", max_length=30, default="Disponible", null=False
    )
    habilitado = models.BooleanField(
        str_habilitado, default=True, null=False
    )
    created_at = models.DateTimeField(
        str_fecha_creacion, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        str_fecha_actualizacion, auto_now=True
    )

    class Meta:
        db_table_comment = "Datos de vehículos de la flota."

class AsignacionVehiculo(models.Model):
    vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.CASCADE, null=False
    )
    conductor = models.ForeignKey(
        Conductor, on_delete=models.CASCADE, null=False
    )
    fecha_inicio = models.DateField("Fecha Inicio", null=False)
    fecha_termino = models.DateField("Fecha Término", null=True)
    observaciones = models.TextField("Observaciones", null=True)
    habilitado = models.BooleanField(
        str_habilitado, default=True, null=False
    )
    created_at = models.DateTimeField(
        str_fecha_creacion, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        str_fecha_actualizacion, auto_now=True
    )

    class Meta:
        db_table_comment = (
            "Historial de asignaciones de vehículos a conductores."
        )

class Mantencion(models.Model):
    vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.CASCADE, null=False
    )
    taller = models.ForeignKey(
        Taller, on_delete=models.CASCADE, null=False
    )
    tipo_mantencion = models.ForeignKey(
        TipoMantencion, on_delete=models.CASCADE, null=False
    )
    fecha_inicio = models.DateField("Fecha Inicio", null=False)
    fecha_termino = models.DateField("Fecha Término", null=True)
    kilometraje = models.IntegerField("Kilometraje", null=False)
    descripcion = models.TextField("Descripción", null=False)
    costo = models.DecimalField(
        "Costo", max_digits=12, decimal_places=2, null=False
    )
    estado = models.CharField(
        "Estado", max_length=30, default="Pendiente", null=False
    )
    habilitado = models.BooleanField(
        str_habilitado, default=True, null=False
    )
    created_at = models.DateTimeField(
        str_fecha_creacion, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        str_fecha_actualizacion, auto_now=True
    )

    class Meta:
        db_table_comment = "Historial de mantenciones de vehículos."

class Incidencia(models.Model):
    vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.CASCADE, null=False
    )
    conductor = models.ForeignKey(
        Conductor, on_delete=models.CASCADE, null=False
    )
    fecha_reporte = models.DateTimeField(
        "Fecha Reporte", auto_now_add=True
    )
    descripcion = models.TextField("Descripción", null=False)
    estado = models.CharField(
        "Estado", max_length=30, default="Pendiente", null=False
    )
    fecha_resolucion = models.DateTimeField(
        "Fecha Resolución", null=True
    )
    observaciones = models.TextField("Observaciones", null=True)
    habilitado = models.BooleanField(
        str_habilitado, default=True, null=False
    )
    created_at = models.DateTimeField(
        str_fecha_creacion, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        str_fecha_actualizacion, auto_now=True
    )

    class Meta:
        db_table_comment = (
            "Incidencias de vehículos reportadas por conductores."
        )

class HistorialEstadoVehiculo(models.Model):
    vehiculo = models.ForeignKey(
        Vehiculo, on_delete=models.CASCADE, null=False
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=False
    )
    estado_anterior = models.CharField(
        "Estado Anterior", max_length=30, null=False
    )
    estado_nuevo = models.CharField(
        "Estado Nuevo", max_length=30, null=False
    )
    motivo = models.TextField("Motivo", null=False)
    fecha_cambio = models.DateTimeField(
        "Fecha Cambio", auto_now_add=True
    )
    created_at = models.DateTimeField(
        str_fecha_creacion, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        str_fecha_actualizacion, auto_now=True
    )

    class Meta:
        db_table_comment = (
            "Historial de cambios de estado de vehículos."
        )