from tkinter import ttk

from views.components.botones import (
    boton_primario,
    boton_exito,
    boton_tension
)


class MenuPrincipal(ttk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, style="App.TFrame")

        self.app = app

        self.crear_titulo()
        self.crear_panel()

    def crear_titulo(self):
        self.label_titulo = ttk.Label(
            self,
            text="Sistema de Gestión Clínica",
            style="Title.TLabel"
        )

        self.label_titulo.pack(pady=(40, 10))

    def crear_panel(self):
        self.panel = ttk.Frame(
            self,
            style="Card.TFrame",
            padding=30
        )

        self.panel.pack(pady=30)

        self.label_pacientes = ttk.Label(
            self.panel,
            text="Gestión de Pacientes",
            style="Subtitle.TLabel"
        )

        self.label_pacientes.pack(pady=(0, 15))

        self.boton_ver_pacientes = boton_primario(
            self.panel,
            "Ver Pacientes",
            lambda: self.app.mostrar_vista("lista_pacientes"),
            ancho=28
        )

        self.boton_alta_paciente = boton_exito(
            self.panel,
            "Dar de Alta Paciente",
            lambda: self.app.mostrar_vista("crear_paciente"),
            ancho=28
        )

        self.boton_ver_pacientes.pack(pady=8)
        self.boton_alta_paciente.pack(pady=8)

        self.separador = ttk.Separator(
            self.panel,
            orient="horizontal"
        )

        self.separador.pack(fill="x", pady=25)

        self.label_tensiones = ttk.Label(
            self.panel,
            text="Control de Tensión Arterial",
            style="Subtitle.TLabel"
        )

        self.label_tensiones.pack(pady=(0, 15))

        self.boton_ver_tensiones = boton_tension(
            self.panel,
            "Ver Tensiones",
            lambda: self.app.mostrar_vista("lista_tensiones"),
            ancho=28
        )

        self.boton_crear_tension = boton_tension(
            self.panel,
            "Registrar Tensión",
            lambda: self.app.mostrar_vista("crear_tension"),
            ancho=28
        )

        self.boton_ver_tensiones.pack(pady=8)
        self.boton_crear_tension.pack(pady=8)