# Data Model — Taller 2 IoT

Este documento refleja el esquema desplegado en PostgreSQL, base `appdb`,
esquema `public`.

## Tabla: sensores

| Campo | Tipo | Nulo | Restricción |
|---|---|---|---|
| id | SERIAL | No | PK |
| codigo | VARCHAR(20) | No | UNIQUE |
| nombre | VARCHAR(100) | No | |
| categoria | VARCHAR(30) | No | CHECK: `AIRE`, `GAS`, `AGUA` o `AMBIENTE` |
| ubicacion | VARCHAR(100) | No | |
| activo | BOOLEAN | No | DEFAULT TRUE |
| fecha_registro | TIMESTAMPTZ | No | DEFAULT NOW() |

## Tabla: sensor_magnitudes

| Campo | Tipo | Nulo | Restricción |
|---|---|---|---|
| id | SERIAL | No | PK |
| sensor_id | INTEGER | No | FK → `sensores(id)` |
| magnitud | VARCHAR(50) | No | |
| unidad | VARCHAR(20) | No | |
| valor_minimo | NUMERIC(12,4) | No | CHECK conjunto: menor que `valor_maximo` |
| valor_maximo | NUMERIC(12,4) | No | CHECK conjunto: mayor que `valor_minimo` |

Restricciones adicionales:

- `UNIQUE(sensor_id, magnitud)`
- `CHECK (valor_minimo < valor_maximo)`
- La FK `sensor_id` utiliza `ON UPDATE CASCADE ON DELETE RESTRICT`.

## Tabla: mediciones

| Campo | Tipo | Nulo | Restricción |
|---|---|---|---|
| id | BIGSERIAL | No | PK |
| sensor_magnitud_id | INTEGER | No | FK → `sensor_magnitudes(id)` |
| valor | NUMERIC(12,4) | No | |
| timestamp_utc | TIMESTAMPTZ | No | |
| fecha_recepcion | TIMESTAMPTZ | No | DEFAULT NOW() |

La FK `sensor_magnitud_id` utiliza `ON UPDATE CASCADE ON DELETE RESTRICT`. Esto
evita eliminar una magnitud que tenga mediciones históricas asociadas.

### Índices de `mediciones`

| Índice | Columnas | Tipo |
|---|---|---|
| `mediciones_pkey` | `id` | Único, creado por la PK |
| `idx_mediciones_sensor_magnitud` | `sensor_magnitud_id` | B-tree |
| `idx_mediciones_timestamp_utc` | `timestamp_utc` | B-tree |
| `idx_mediciones_magnitud_timestamp` | `sensor_magnitud_id, timestamp_utc` | B-tree compuesto |

## Relaciones

- `sensores` 1:N `sensor_magnitudes`
- `sensor_magnitudes` 1:N `mediciones`

Las dos relaciones impiden el borrado de la fila padre mediante `ON DELETE
RESTRICT`, protegiendo la configuración y el histórico.

## Estado de los datos iniciales

- 15 sensores.
- 40 magnitudes asociadas.
- Todos los sensores tienen al menos una magnitud.
- 0 mediciones iniciales; estas serán almacenadas posteriormente por la
  aplicación desarrollada por los estudiantes.
