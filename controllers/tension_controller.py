import uuid
from datetime import datetime

from schemas.tension_schema import TensionSchema


class TensionController:

    def __init__(
        self,
        paciente_repository,
        tension_repository,
        tension_service
    ):
        self.paciente_repository = paciente_repository
        self.tension_repository = tension_repository
        self.tension_service = tension_service

    def obtener_pacientes(self):
        return self.paciente_repository.obtener_todos()

    def obtener_tensiones(self):
        return self.tension_repository.obtener_todas()

    def crear_tension(self, datos):
        datos["sistolica"] = int(datos["sistolica"])
        datos["diastolica"] = int(datos["diastolica"])

        tension_validada = TensionSchema(**datos)

        paciente = self.paciente_repository.obtener_por_id(
            tension_validada.id_paciente
        )

        if not paciente:
            raise ValueError("El paciente seleccionado no existe")

        valor_en_rango = self.tension_service.calcular_valor_en_rango(
            tension_validada.sistolica,
            tension_validada.diastolica
        )

        if not tension_validada.valoracion:
            valoracion = self.tension_service.clasificar_tension(
                tension_validada.sistolica,
                tension_validada.diastolica
            )
        else:
            valoracion = tension_validada.valoracion

        nueva_tension = {
            "_id": str(uuid.uuid4()),
            "id_paciente": tension_validada.id_paciente,
            "valores": {
                "sistolica": tension_validada.sistolica,
                "diastolica": tension_validada.diastolica
            },
            "estado": "final",
            "fecha": datetime.utcnow(),
            "valoracion": valoracion,
            "valor_en_rango": valor_en_rango
        }

        self.tension_repository.insertar(nueva_tension)

    def eliminar_tension(self, id_tension):
        self.tension_repository.eliminar_por_id(id_tension)

    def actualizar_tension(
        self,
        id_tension,
        datos
    ):

        datos["sistolica"] = int(
            datos["sistolica"]
        )

        datos["diastolica"] = int(
            datos["diastolica"]
        )

        tension_validada = TensionSchema(
            **datos
        )

        valor_en_rango = (
            self.tension_service
            .calcular_valor_en_rango(
                tension_validada.sistolica,
                tension_validada.diastolica
            )
        )

        datos_actualizados = {

            "id_paciente": (
                tension_validada.id_paciente
            ),

            "valores": {

                "sistolica": (
                    tension_validada.sistolica
                ),

                "diastolica": (
                    tension_validada.diastolica
                )
            },

            "valoracion": (
                tension_validada.valoracion
            ),

            "valor_en_rango": (
                valor_en_rango
            )
        }

        self.tension_repository.actualizar_por_id(
            id_tension,
            datos_actualizados
        )