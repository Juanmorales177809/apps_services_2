# Clase 5 - FASTAPI

## Objetivo de la clase

Comprender los conceptos fundamentales de FastAPI y crear el primer servicio web en Python, implementando una consulta GET, ejecutándola con Uvicorn y probándola desde Swagger UI.

## Generalidades de FastAPI

FastAPI es un framework moderno para construir APIs web con Python. Está basado en Starlette para las funcionalidades web y en Pydantic para la validación y serialización de datos.

Sus principales características son:

- Alto rendimiento y soporte para programación asíncrona.
- Validación automática de datos mediante tipos de Python.
- Generación automática de la especificación OpenAPI.
- Documentación interactiva con Swagger UI y ReDoc.
- Sintaxis clara y compatible con los estándares actuales de desarrollo de APIs.

### ¿Por qué FastAPI?

FastAPI permite desarrollar APIs rápidamente, con poco código y con validación integrada. Además, la documentación se genera automáticamente a partir de las rutas y los modelos definidos en la aplicación, lo que facilita las pruebas y el consumo del servicio por otros desarrolladores.

## Historia de FastAPI

Como complemento a la clase, consulte el siguiente video sobre la historia y evolución de FastAPI:

[Historia de FastAPI](https://www.youtube.com/watch?v=mpR8ngthqiE)

## ¿Cómo funciona FastAPI?

Una aplicación FastAPI se construye creando una instancia de `FastAPI` y definiendo rutas mediante decoradores, como `@app.get()`, `@app.post()` o `@app.put()`.

Cuando un cliente realiza una petición HTTP, FastAPI identifica la ruta y el método correspondiente, ejecuta la función asociada y convierte su resultado a una respuesta HTTP, normalmente en formato JSON.

En este proyecto, la aplicación se encuentra en `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola mundo"}
```

La expresión `@app.get("/")` indica que la función `read_root` atenderá peticiones GET realizadas sobre la ruta raíz `/`.

## Instalación en un entorno virtual

Desde la carpeta del proyecto, cree y active un entorno virtual:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux o macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Después, instale las dependencias:

```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` incluye FastAPI y Uvicorn. La carpeta `venv/` está incluida en `.gitignore`, por lo que no se subirá al repositorio.

## Desplegar el primer servidor con Uvicorn

Uvicorn es el servidor ASGI que ejecuta la aplicación FastAPI. Inicie el servidor con:

```bash
uvicorn main:app --reload
```

En este comando, `main` corresponde a `main.py`, `app` a la instancia `app = FastAPI()` y `--reload` reinicia automáticamente el servidor cuando detecta cambios.

El servidor estará disponible en:

```text
http://127.0.0.1:8000
```

Para detenerlo, presione `Ctrl + C`.

## Ingresar a Swagger UI y ejecutar la primera consulta

FastAPI genera automáticamente una interfaz de documentación interactiva con Swagger UI. Para acceder a ella, abra:

```text
http://127.0.0.1:8000/docs
```

Para ejecutar el GET de ejemplo:

1. Ubique la operación `GET /`.
2. Haga clic sobre la operación para expandirla.
3. Seleccione **Try it out**.
4. Haga clic en **Execute**.
5. Revise la respuesta en **Response body**.

La respuesta esperada es:

```json
{
  "message": "Hola mundo"
}
```

La consulta también puede realizarse desde el navegador en `http://127.0.0.1:8000/` o mediante `curl`:

```bash
curl http://127.0.0.1:8000/
```

La documentación alternativa con ReDoc está disponible en:

```text
http://127.0.0.1:8000/redoc
```
