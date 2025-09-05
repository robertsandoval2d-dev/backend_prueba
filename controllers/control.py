from models.profesor import Profesor
from models.alumno import Alumno

class Control:
    def __init__(self):
        self.profesores = []
        self.alumnos = []
        self.next_id_prof = 1
        self.next_id_alum = 1

    # ------- PROFESORES -------
    def listar_profesores(self):
        return self.profesores

    def crear_profesor(self, nombre, edad):
        profe = Profesor(self.next_id_prof, nombre, edad)
        self.profesores.append(profe)
        self.next_id_prof += 1
        return profe

    def eliminar_profesor(self, id):
        self.profesores = [p for p in self.profesores if p.id != id]
        return {"status": "ok", "message": f"Profesor {id} eliminado"}

    # ------- ALUMNOS -------
    def listar_alumnos(self):
        return self.alumnos

    def crear_alumno(self, nombre, edad):
        alum = Alumno(self.next_id_alum, nombre, edad)
        self.alumnos.append(alum)
        self.next_id_alum += 1
        return alum