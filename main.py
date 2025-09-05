from fastapi import FastAPI
from controllers.control import Control

app = FastAPI()
control = Control()

@app.get("/")
def root():
    return {"status": "ok", "message": "Servidor funcionando"}

# -------- PROFESORES --------
@app.get("/profesores")
def listar_profesores():
    return [{"id": p.id, "nombre": p.nombre, "edad": p.edad} for p in control.listar_profesores()]

@app.post("/profesores")
def crear_profesor(nombre: str, edad: int):
    profe = control.crear_profesor(nombre, edad)
    return {"id": profe.id, "nombre": profe.nombre, "edad": profe.edad}

@app.delete("/profesores/{id}")
def eliminar_profesor(id: int):
    return control.eliminar_profesor(id)

# -------- ALUMNOS --------
@app.get("/alumnos")
def listar_alumnos():
    return [{"id": a.id, "nombre": a.nombre, "edad": a.edad} for a in control.listar_alumnos()]

@app.post("/alumnos")
def crear_alumno(nombre: str, edad: int):
    alum = control.crear_alumno(nombre, edad)
    return {"id": alum.id, "nombre": alum.nombre, "edad": alum.edad}