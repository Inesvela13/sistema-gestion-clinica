import uuid
from datetime import datetime

from schemas.tension_schema import TensionSchema


class TensionService:

    def __init__(self, tension_repository, paciente_repository):

        self.tension_repository = tension_repository
        self.paciente_repository = paciente_repository

    # =========================================
    # OBTENER TENSIONES
    # =========================================

    def obtener_tensiones(self):

        return self.tension_repository.obtener_todas()

    # =========================================
    # CREAR TENSIÓN
    # =========================================

    def crear_tension(self, datos):

        # =========================
        # CONVERTIR A ENTEROS
        # =========================

        datos["sistolica"] = int(
            datos["sistolica"]
        )

        datos["diastolica"] = int(
            datos["diastolica"]
        )

        # =========================
        # VALIDAR DATOS
        # =========================

        tension_validada = TensionSchema(
            **datos
        )

        # =========================
        # COMPROBAR PACIENTE
        # =========================

        paciente = self.paciente_repository.obtener_por_id(
            tension_validada.id_paciente
        )

        if not paciente:

            raise ValueError(
                "El paciente seleccionado no existe"
            )

        # =========================
        # CREAR DOCUMENTO
        # =========================

        nueva_tension = {

            "_id": str(uuid.uuid4()),

            "id_paciente": tension_validada.id_paciente,

            "valores": {

                "sistolica": tension_validada.sistolica,

                "diastolica": tension_validada.diastolica
            },

            "fecha": datetime.utcnow(),

            "valoracion": tension_validada.valoracion,

            "estado": "final",

            "valor_en_rango": self.comprobar_valor_en_rango(
                tension_validada.sistolica,
                tension_validada.diastolica
            )
        }

        # =========================
        # INSERTAR EN MONGODB
        # =========================

        self.tension_repository.insertar(
            nueva_tension
        )

    # =========================================
    # ELIMINAR TENSIÓN
    # =========================================

    def eliminar_tension(self, id_tension):

        self.tension_repository.eliminar_por_id(
            id_tension
        )

    # =========================================
    # COMPROBAR RANGO NORMAL
    # =========================================

    def comprobar_valor_en_rango(
        self,
        sistolica,
        diastolica
    ):

        return (
            90 <= sistolica <= 140
            and
            60 <= diastolica <= 90
        )