class TensionRepository:
    def __init__(self, db):
        self.db = db

    def obtener_todas(self):
        return list(self.db.tensiones.find())

    def obtener_por_id(self, id_tension):
        return self.db.tensiones.find_one({"_id": id_tension})

    def insertar(self, tension):
        self.db.tensiones.insert_one(tension)

    def eliminar_por_id(self, id_tension):
        self.db.tensiones.delete_one({"_id": id_tension})