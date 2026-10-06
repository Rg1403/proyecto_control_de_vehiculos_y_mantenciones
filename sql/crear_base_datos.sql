CREATE DATABASE control_vehiculos
CHARACTER SET utf8mb4;

CREATE USER 'vehiculos_app'@'%'
IDENTIFIED BY 'CAMBIA_ESTA_CLAVE';

GRANT ALL PRIVILEGES ON control_vehiculos.*
TO 'vehiculos_app'@'%';

FLUSH PRIVILEGES;