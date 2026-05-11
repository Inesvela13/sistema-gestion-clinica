import tkinter as tk
from tkinter import ttk

from dependencias.database import Database

from repositories.paciente_repository import PacienteRepository
from repositories.tension_repository import TensionRepository

from services.paciente_service import PacienteService
from services.tension_service import TensionService

from views.pacientes.lista_pacientes import ListaPacientes
from views.pacientes.crear_paciente import CrearPaciente

from views.tensiones.lista_tensiones import ListaTensiones
from views.tensiones.crear_tension import CrearTension

from config.styles import (
    COLOR_FONDO,
    COLOR_BLANCO,
    COLOR_PRIMARIO,
    COLOR_PRIMARIO_OSCURO,
    COLOR_EXITO,
    COLOR_TENSION,
    COLOR_TENSION_OSCURO,
    COLOR_TEXTO,
    COLOR_TEXTO_SECUNDARIO,
    FUENTE_NORMAL,
    FUENTE_NORMAL_NEGRITA
)

from widgets.botones import BotonPrimario, BotonExito, BotonTension


class MenuPrincipal(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLOR_FONDO)

        self.controller = controller

        self.crear_titulo()
        self.crear_panel()

    def crear_titulo(self):
        titulo = tk.Label(
            self,
            text="Sistema de Gestión Clínica",
            font=("Segoe UI", 28, "bold"),
            fg=COLOR_PRIMARIO,
            bg=COLOR_FONDO
        )

        titulo.pack(pady=(40, 10))

        subtitulo = tk.Label(
            self,
            text="Panel principal de administración médica",
            font=("Segoe UI", 12),
            fg=COLOR_TEXTO_SECUNDARIO,
            bg=COLOR_FONDO
        )

        subtitulo.pack(pady=(0, 40))

    def crear_panel(self):
        panel = tk.Frame(
            self,
            bg=COLOR_BLANCO,
            bd=1,
            relief="solid"
        )

        panel.pack(pady=20, ipadx=40, ipady=30)

        tk.Label(
            panel,
            text="Gestión de Pacientes",
            font=("Segoe UI", 16, "bold"),
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO
        ).pack(pady=(10, 20))

        BotonPrimario(
            panel,
            text="👨‍⚕️ Ver Pacientes",
            command=lambda: self.controller.show_frame("lista_pacientes"),
            width=25
        ).pack(pady=10)

        BotonExito(
            panel,
            text="➕ Dar de Alta Paciente",
            command=lambda: self.controller.show_frame("crear_paciente"),
            width=25
        ).pack(pady=10)

        ttk.Separator(
            panel,
            orient="horizontal"
        ).pack(fill="x", pady=30)

        tk.Label(
            panel,
            text="Control de Tensión Arterial",
            font=("Segoe UI", 16, "bold"),
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO
        ).pack(pady=(0, 20))

        BotonTension(
            panel,
            text="❤️ Ver Tensiones",
            command=lambda: self.controller.show_frame("lista_tensiones"),
            width=25
        ).pack(pady=10)

        BotonTension(
            panel,
            text="📈 Registrar Tensión",
            command=lambda: self.controller.show_frame("crear_tension"),
            width=25
        ).pack(pady=10)


class App(tk.Tk):

    def __init__(self, paciente_service, tension_service):
        super().__init__()

        self.title("Sistema de Gestión Clínica")
        self.geometry("1200x720")
        self.minsize(1100, 650)
        self.configure(bg=COLOR_FONDO)

        self.paciente_service = paciente_service
        self.tension_service = tension_service

        self.configurar_estilos()
        self.crear_contenedor()
        self.crear_frames()

        self.show_frame("menu")

    def configurar_estilos(self):
        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Treeview",
            background=COLOR_BLANCO,
            foreground=COLOR_TEXTO,
            fieldbackground=COLOR_BLANCO,
            rowheight=35,
            borderwidth=0,
            font=FUENTE_NORMAL
        )

        style.configure(
            "Treeview.Heading",
            background=COLOR_PRIMARIO,
            foreground=COLOR_BLANCO,
            font=("Segoe UI", 11, "bold"),
            padding=10,
            relief="flat"
        )

        style.map(
            "Treeview",
            background=[("selected", "#90CAF9")],
            foreground=[("selected", COLOR_PRIMARIO_OSCURO)]
        )

        style.configure(
            "TCombobox",
            fieldbackground=COLOR_BLANCO,
            background=COLOR_BLANCO,
            foreground=COLOR_TEXTO
        )

    def crear_contenedor(self):
        self.container = tk.Frame(
            self,
            bg=COLOR_FONDO
        )

        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def crear_frames(self):
        self.frames = {}

        self.frames["menu"] = MenuPrincipal(
            self.container,
            self
        )

        self.frames["lista_pacientes"] = ListaPacientes(
            self.container,
            self
        )

        self.frames["crear_paciente"] = CrearPaciente(
            self.container,
            self
        )

        self.frames["lista_tensiones"] = ListaTensiones(
            self.container,
            self
        )

        self.frames["crear_tension"] = CrearTension(
            self.container,
            self
        )

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, nombre_frame):
        frame = self.frames[nombre_frame]

        if hasattr(frame, "actualizar_datos"):
            frame.actualizar_datos()

        frame.tkraise()


if __name__ == "__main__":

    db = Database()

    paciente_repository = PacienteRepository(db)
    tension_repository = TensionRepository(db)

    paciente_service = PacienteService(
        paciente_repository
    )

    tension_service = TensionService(
        tension_repository,
        paciente_repository
    )

    app = App(
        paciente_service,
        tension_service
    )

    app.mainloop()