import tkinter as tk
from tkinter import ttk

from dependencias.database import Database

from repositories.paciente_repository import PacienteRepository
from repositories.tension_repository import TensionRepository

from services.tension_service import TensionService

from controllers.paciente_controller import PacienteController
from controllers.tension_controller import TensionController

from views.styles import configurar_estilos
from views.menu import MenuPrincipal

from views.pacientes.lista_pacientes import ListaPacientes
from views.pacientes.crear_paciente import CrearPaciente

from views.tensiones.lista_tensiones import ListaTensiones
from views.tensiones.crear_tension import CrearTension
from views.router import Router

class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Sistema de Gestión Clínica")
        self.geometry("1200x720")
        self.minsize(1100, 650)

        configurar_estilos()

        self.crear_dependencias()
        self.crear_contenedor()
        self.crear_vistas()

        self.mostrar_vista("menu")

    def crear_dependencias(self):
        self.database = Database()

        self.paciente_repository = PacienteRepository(
            self.database
        )

        self.tension_repository = TensionRepository(
            self.database
        )

        self.tension_service = TensionService()

        self.paciente_controller = PacienteController(
            self.paciente_repository
        )

        self.tension_controller = TensionController(
            self.paciente_repository,
            self.tension_repository,
            self.tension_service
        )

    def crear_contenedor(self):
        self.contenedor = ttk.Frame(
            self,
            style="App.TFrame"
        )

        self.contenedor.pack(
            fill="both",
            expand=True
        )

        self.contenedor.grid_rowconfigure(
            0,
            weight=1
        )

        self.contenedor.grid_columnconfigure(
            0,
            weight=1
        )

    def crear_vistas(self):

        self.frames = {}

        vistas = Router.obtener_vistas()

        for nombre, clase_vista in vistas.items():

            frame = clase_vista(
                self.contenedor,
                self
            )

            self.frames[nombre] = frame

            frame.grid(
                row=0,
                column=0,
                sticky="nsew"
            )
    def mostrar_vista(self, nombre_vista):
        frame = self.frames[nombre_vista]

        if hasattr(frame, "actualizar_datos"):
            frame.actualizar_datos()

        frame.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()