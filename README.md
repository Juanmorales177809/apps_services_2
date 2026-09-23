# Clase 6 - FASTAPI

## Objetivo de la clase

Construir una API para gestionar estudiantes utilizando FastAPI y Pydantic. Se implementarán las operaciones HTTP fundamentales para crear, consultar, actualizar y eliminar datos almacenados temporalmente en memoria.

## Generalidades de FastAPI

FastAPI es un framework moderno de Python para construir APIs web. Permite definir rutas con decoradores, validar automáticamente los datos recibidos y generar documentación interactiva con OpenAPI y Swagger UI.

Como complemento sobre la historia y evolución de FastAPI, consulte el siguiente video:

[Historia de FastAPI](https://www.youtube.com/watch?v=mpR8ngthqiE)

## Modelo de datos con Pydantic

El proyecto utiliza un modelo Pydantic para validar la información de cada estudiante:

```python
class Estudiante(BaseModel):
    nombre: str
    edad: int
    programa: str
```

Cada estudiante debe tener un nombre de texto, una edad numérica y el nombre de un programa académico.

Los estudiantes se guardan en la variable `dataset_estudiantes`, que es una lista principal. Cada estudiante se representa como una lista secundaria:

```python
dataset_estudiantes = [
    ["Ana Gómez", 20, "Ingeniería de Sistemas"],
    ["Carlos Pérez", 22, "Diseño Industrial"]
]
```

Esta información se almacena únicamente en memoria. Por lo tanto, se pierde cuando se detiene o reinicia el servidor.

## Iniciar el servidor

Active el entorno virtual e instale las dependencias:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

En Windows puede utilizar:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Ejecute la aplicación con Uvicorn:

```bash
uvicorn main:app --reload
```

El servidor quedará disponible en `http://127.0.0.1:8000`.

## Documentación Swagger

FastAPI genera automáticamente la documentación interactiva en:

```text
http://127.0.0.1:8000/docs
```

Para probar una operación:

1. Seleccione la operación que desea ejecutar.
2. Haga clic en **Try it out**.
3. Escriba los datos solicitados.
4. Haga clic en **Execute**.
5. Revise el código y el cuerpo de la respuesta.

## Peticiones de la API

### GET `/`

Esta es la ruta inicial de la aplicación. Sirve para comprobar que el servidor está funcionando.

Respuesta:

```json
{
  "message": "Hola mundo"
}
```

### POST `/estudiantes`

Agrega un nuevo estudiante al dataset. El cuerpo de la petición debe incluir todos los campos definidos en el modelo `Estudiante`.

Ejemplo de solicitud:

```json
{
  "nombre": "Ana Gómez",
  "edad": 20,
  "programa": "Ingeniería de Sistemas"
}
```

Internamente, el estudiante se convierte en una lista y se agrega al dataset:

```text
["Ana Gómez", 20, "Ingeniería de Sistemas"]
```

Respuesta esperada:

```json
{
  "message": "Estudiante agregado correctamente",
  "estudiante": ["Ana Gómez", 20, "Ingeniería de Sistemas"],
  "dataset": [
    ["Ana Gómez", 20, "Ingeniería de Sistemas"]
  ]
}
```

Cada vez que se ejecuta el POST, el dataset completo también se imprime en la consola del servidor.

### PUT `/estudiantes/{indice}`

Reemplaza completamente un estudiante existente. El parámetro `indice` indica la posición del estudiante dentro del dataset. El primer estudiante tiene índice `0`, el segundo índice `1`, y así sucesivamente.

Ejemplo para reemplazar el primer estudiante:

```text
PUT /estudiantes/0
```

Cuerpo de la solicitud:

```json
{
  "nombre": "Ana Rodríguez",
  "edad": 21,
  "programa": "Ingeniería de Software"
}
```

El PUT exige los tres campos y reemplaza completamente la lista que se encuentra en la posición indicada.

### PATCH `/estudiantes/{indice}`

Actualiza parcialmente un estudiante. A diferencia de PUT, solo es necesario enviar los campos que se desean modificar.

Ejemplo para cambiar únicamente el programa del primer estudiante:

```text
PATCH /estudiantes/0
```

Cuerpo de la solicitud:

```json
{
  "programa": "Ingeniería de Datos"
}
```

También se pueden actualizar varios campos:

```json
{
  "nombre": "Ana Rodríguez",
  "edad": 22
}
```

Los campos no enviados conservan su valor original. Este comportamiento se logra con el modelo `EstudianteActualizacion` y `exclude_unset=True`.

### DELETE `/estudiantes/{indice}`

Elimina el estudiante ubicado en la posición indicada.

Ejemplo para eliminar el primer estudiante:

```text
DELETE /estudiantes/0
```

La lista se elimina del dataset y los estudiantes que estaban después de ella ocupan una nueva posición.

## Validación y errores

Pydantic valida automáticamente los datos recibidos. Por ejemplo, `edad` debe ser un número entero y los campos de texto deben enviarse como cadenas.

Si se utiliza un índice que no existe, la API responde:

```json
{
  "error": "El estudiante no existe"
}
```

Después de cada POST, PUT, PATCH o DELETE, el contenido actualizado del dataset se imprime en la consola del servidor.

## Resumen de operaciones

| Método | Ruta | Función |
|---|---|---|
| GET | `/` | Verificar que el servidor funciona |
| POST | `/estudiantes` | Agregar un estudiante |
| PUT | `/estudiantes/{indice}` | Reemplazar todos los datos |
| PATCH | `/estudiantes/{indice}` | Actualizar algunos datos |
| DELETE | `/estudiantes/{indice}` | Eliminar un estudiante |

## Actividad propuesta

Amplíe la API para consultar un estudiante por su identificador.

1. Agregue el campo `id` al modelo `Estudiante`.
2. Modifique la estructura del dataset para guardar el identificador de cada estudiante.
3. Cree una operación `GET /estudiantes/{id}` que busque y retorne únicamente el estudiante solicitado.
4. Pruebe la operación desde Swagger UI con estudiantes existentes y con un ID que no exista.
5. Documente el nuevo endpoint en el README.
6. Publique los cambios en su repositorio de la clase.

La respuesta para un ID existente debe incluir los datos del estudiante. Para un ID inexistente, la API debe responder un mensaje indicando que el estudiante no fue encontrado.
