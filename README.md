# Clase 4 — Datos e interacción entre aplicaciones

## Propósito

En esta práctica van a leer un dataset CSV de estudiantes, transformarlo a una estructura propia y generar un archivo JSON.

El flujo completo es:

```text
estudiantes.csv → estructuras de Python → transformación → estudiantes_resumen.json
```

Al finalizar, podrán identificar cómo una aplicación recibe datos externos, los interpreta, selecciona la información necesaria y produce una representación que otra aplicación podría consumir.

## Estructura del proyecto

```text
clase-03-datos/
├── datos/
│   └── estudiantes.csv
├── salida/
│   └── estudiantes_resumen.json
├── transformar_estudiantes.py
└── README.md
```

Cree las carpetas `datos/` y `salida/` si aún no existen. Ubique el archivo `estudiantes.csv` dentro de `datos/`.

## Requisitos

- Python 3 instalado.
- Editor de código, preferiblemente Visual Studio Code.
- Git configurado con tu cuenta de GitHub.

Esta práctica utiliza únicamente módulos de la biblioteca estándar de Python:

- `csv`: permite leer archivos CSV.
- `json`: permite serializar y deserializar datos JSON.
- `pathlib`: permite construir rutas de archivos de forma segura.

No es necesario instalar paquetes con `pip`.

## Paso 1 — Verificar Python

Crea el archivo `transformar_estudiantes.py` en la carpeta raíz del proyecto y agrega:

```python
print("Hola, Aplicaciones y Servicios Web")
```

## Paso 2 — Leer el CSV


## Paso 3 — Transformar un estudiante


Hacer estos cambios:

| Dato de entrada | Dato de salida |
|---|---|
| `codigo` | `id` |
| `nombre` + `apellido` | `nombre_completo` |
| `semestre` como texto | `semestre` como entero |
| `promedio` como texto | `promedio` como decimal |
| `activo` con `true` o `false` | `estado` con `Activo` o `Inactivo` |
| `correo` | No se incluye en la salida |

## Paso 4 — Crear una función de transformación

Reemplaza el bloque de transformación del paso anterior por una función:


## Paso 5 — Transformar todos los registros y guardarlos en una lista


## Paso 6 — Serializar y guardar el JSON

Agrega el import al inicio del archivo:

```python
import json
```

Luego agrega la función de serialización:

```python
def serializar_estudiantes(ruta: Path, estudiantes: list[dict]) -> None:
    """Serializa una lista de diccionarios Python a un archivo JSON UTF-8."""
    ruta.parent.mkdir(exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(estudiantes, archivo, indent=2, ensure_ascii=False)
```

Al final del archivo, define la ruta de salida y llama la función:

```python
RUTA_JSON = BASE_DIR / "salida" / "estudiantes_resumen.json"

serializar_estudiantes(RUTA_JSON, estudiantes_transformados)
print(f"Archivo JSON generado: {RUTA_JSON}")
```

Abre el archivo `salida/estudiantes_resumen.json` y comprueba que:

- Contiene un arreglo JSON válido.
- Los nombres con tildes se visualizan correctamente.
- Los valores de `semestre` y `promedio` no tienen comillas.
- El campo `correo` no aparece.

## Paso 7 — Deserializar el JSON generado

Agrega esta función:

```python
def deserializar_estudiantes(ruta: Path) -> list[dict]:
    """Deserializa un archivo JSON a una lista de diccionarios Python."""
    with open(ruta, encoding="utf-8") as archivo:
        return json.load(archivo)
```

Y úsala al final:

```python
estudiantes_recuperados = deserializar_estudiantes(RUTA_JSON)

print("\nDatos recuperados desde el JSON:")
print(estudiantes_recuperados[0])
print(f"Total recuperado: {len(estudiantes_recuperados)}")
```

## Flujo final esperado

Tu programa debe completar este recorrido:

```text
1. Leer estudiantes.csv con csv.DictReader.
2. Convertir cada fila del CSV a un diccionario Python.
3. Transformar los registros al formato del panel académico.
4. Serializar la lista transformada en estudiantes_resumen.json.
5. Deserializar el JSON generado.
6. Mostrar el primer estudiante recuperado y el total de registros.
```

## Entregables

Para completar la práctica debes incluir:

- `datos/estudiantes.csv`.
- `transformar_estudiantes.py` funcionando.
- `salida/estudiantes_resumen.json` generado por tu programa.
- Un Pull Request hacia la rama `main`.

## Entrega en GitHub

Cuando el programa funcione, ejecuta:

```bash
git status
git checkout -b clase-4
git add datos .
git commit -m "feat: transforma estudiantes CSV a JSON"
git push -u origin clase-4
```

