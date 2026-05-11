from pymongo import MongoClient

class Database:
    def __init__(self):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client["clinica"]

        self.pacientes = self.db["pacientes"]
        self.tensiones = self.db["tensiones"]


database = Database()