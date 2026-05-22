class PacienteRepository:

    def __init__(self, db):
        self.db = db

    def obtener_todos(self):
        return list(self.db.pacientes.find())

    def insertar(self, paciente):
        self.db.pacientes.insert_one(paciente)

    def eliminar_por_id(self, id_paciente):
        self.db.pacientes.delete_one(
            {"_id": id_paciente}
        )

    def actualizar_por_id(
        self,
        id_paciente,
        datos
    ):

        self.db.pacientes.update_one(
            {"_id": id_paciente},
            {"$set": datos}
        )

    def obtener_por_id(self, id_paciente):

        return self.db.pacientes.find_one(
            {"_id": id_paciente}
        )