import uuid
from datetime import datetime

from schemas.paciente_schema import PacienteSchema


class PacienteService:

    def __init__(self, paciente_repository):
        self.paciente_repository = paciente_repository

    def obtener_pacientes(self):
        return self.paciente_repository.obtener_todos()

    def crear_paciente(self, datos):

        paciente_validado = PacienteSchema(**datos)

        nuevo_paciente = {

            "_id": str(uuid.uuid4()),

            "nombre": paciente_validado.nombre,

            "apellido": paciente_validado.apellido,

            "género": paciente_validado.género,

            "fechaNacimiento": datetime.strptime(
                paciente_validado.fechaNacimiento,
                "%Y-%m-%d"
            ),

            "médico_cabecera": paciente_validado.médico_cabecera
        }

        self.paciente_repository.insertar(
            nuevo_paciente
        )

    def eliminar_paciente(self, id_paciente):

        self.paciente_repository.eliminar_por_id(
            id_paciente
        )