from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()
dataset_estudiantes: list[list] = []


class Estudiante(BaseModel):
    nombre: str
    edad: int
    programa: str


@app.get("/")
def read_root():
    return {"message": "Hola mundo"}


@app.post("/estudiantes")
def agregar_estudiante(estudiante: Estudiante):
    estudiante_como_lista = [
        estudiante.nombre,
        estudiante.edad,
        estudiante.programa,
    ]
    dataset_estudiantes.append(estudiante_como_lista)

    print("Dataset de estudiantes:")
    for registro in dataset_estudiantes:
        print(registro)

    return {
        "message": "Estudiante agregado correctamente",
        "estudiante": estudiante_como_lista,
        "dataset": dataset_estudiantes,
    }


class EstudianteActualizacion(BaseModel):
    nombre: Optional[str] = None
    edad: Optional[int] = None
    programa: Optional[str] = None


def imprimir_dataset():
    print("Dataset de estudiantes:")
    for registro in dataset_estudiantes:
        print(registro)


@app.put("/estudiantes/{indice}")
def reemplazar_estudiante(indice: int, estudiante: Estudiante):
    if indice < 0 or indice >= len(dataset_estudiantes):
        return {"error": "El estudiante no existe"}

    dataset_estudiantes[indice] = [
        estudiante.nombre,
        estudiante.edad,
        estudiante.programa,
    ]
    imprimir_dataset()

    return {
        "message": "Estudiante reemplazado correctamente",
        "estudiante": dataset_estudiantes[indice],
        "dataset": dataset_estudiantes,
    }


@app.patch("/estudiantes/{indice}")
def actualizar_estudiante_parcial(
    indice: int, estudiante: EstudianteActualizacion
):
    if indice < 0 or indice >= len(dataset_estudiantes):
        return {"error": "El estudiante no existe"}

    datos_actualizados = estudiante.model_dump(exclude_unset=True)
    campos = {"nombre": 0, "edad": 1, "programa": 2}

    for campo, valor in datos_actualizados.items():
        dataset_estudiantes[indice][campos[campo]] = valor

    imprimir_dataset()

    return {
        "message": "Estudiante actualizado correctamente",
        "estudiante": dataset_estudiantes[indice],
        "dataset": dataset_estudiantes,
    }


@app.delete("/estudiantes/{indice}")
def eliminar_estudiante(indice: int):
    if indice < 0 or indice >= len(dataset_estudiantes):
        return {"error": "El estudiante no existe"}

    estudiante_eliminado = dataset_estudiantes.pop(indice)
    imprimir_dataset()

    return {
        "message": "Estudiante eliminado correctamente",
        "estudiante": estudiante_eliminado,
        "dataset": dataset_estudiantes,
    }
