from tkinter import ttk

from views.components.botones import (
    boton_gris
)


class DetallePaciente(ttk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, style="App.TFrame")

        self.app = app

        self.crear_titulo()
        self.crear_tarjeta()
        self.crear_botones()

    def crear_titulo(self):

        self.label_titulo = ttk.Label(
            self,
            text="Detalle del Paciente",
            style="Title.TLabel"
        )

        self.label_titulo.pack(
            pady=25
        )

    def crear_tarjeta(self):

        self.frame_card = ttk.Frame(
            self,
            style="Card.TFrame",
            padding=35
        )

        self.frame_card.pack(
            pady=20
        )

        # NOMBRE

        self.label_nombre_titulo = ttk.Label(
            self.frame_card,
            text="Nombre:",
            style="Form.TLabel"
        )

        self.label_nombre = ttk.Label(
            self.frame_card,
            text="",
            style="Info.TLabel"
        )

        # APELLIDO

        self.label_apellido_titulo = ttk.Label(
            self.frame_card,
            text="Apellido:",
            style="Form.TLabel"
        )

        self.label_apellido = ttk.Label(
            self.frame_card,
            text="",
            style="Info.TLabel"
        )

        # GENERO

        self.label_genero_titulo = ttk.Label(
            self.frame_card,
            text="Género:",
            style="Form.TLabel"
        )

        self.label_genero = ttk.Label(
            self.frame_card,
            text="",
            style="Info.TLabel"
        )

        # FECHA

        self.label_fecha_titulo = ttk.Label(
            self.frame_card,
            text="Fecha nacimiento:",
            style="Form.TLabel"
        )

        self.label_fecha = ttk.Label(
            self.frame_card,
            text="",
            style="Info.TLabel"
        )

        # MEDICO

        self.label_medico_titulo = ttk.Label(
            self.frame_card,
            text="Médico responsable:",
            style="Form.TLabel"
        )

        self.label_medico = ttk.Label(
            self.frame_card,
            text="",
            style="Info.TLabel"
        )

        # GRID

        self.label_nombre_titulo.grid(
            row=0,
            column=0,
            padx=15,
            pady=10,
            sticky="e"
        )

        self.label_nombre.grid(
            row=0,
            column=1,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.label_apellido_titulo.grid(
            row=1,
            column=0,
            padx=15,
            pady=10,
            sticky="e"
        )

        self.label_apellido.grid(
            row=1,
            column=1,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.label_genero_titulo.grid(
            row=2,
            column=0,
            padx=15,
            pady=10,
            sticky="e"
        )

        self.label_genero.grid(
            row=2,
            column=1,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.label_fecha_titulo.grid(
            row=3,
            column=0,
            padx=15,
            pady=10,
            sticky="e"
        )

        self.label_fecha.grid(
            row=3,
            column=1,
            padx=15,
            pady=10,
            sticky="w"
        )

        self.label_medico_titulo.grid(
            row=4,
            column=0,
            padx=15,
            pady=10,
            sticky="e"
        )

        self.label_medico.grid(
            row=4,
            column=1,
            padx=15,
            pady=10,
            sticky="w"
        )

    def crear_botones(self):

        self.frame_botones = ttk.Frame(
            self,
            style="App.TFrame"
        )

        self.frame_botones.pack(
            pady=20
        )

        self.boton_volver = boton_gris(
            self.frame_botones,
            "Volver",
            lambda: self.app.mostrar_vista(
                "lista_pacientes"
            )
        )

        self.boton_volver.grid(
            row=0,
            column=0,
            padx=10
        )

    def cargar_paciente(self, paciente):

        self.label_nombre.config(
            text=paciente.get(
                "nombre",
                "-"
            )
        )

        self.label_apellido.config(
            text=paciente.get(
                "apellido",
                "-"
            )
        )

        self.label_genero.config(
            text=paciente.get(
                "género",
                "-"
            )
        )

        fecha = paciente.get(
            "fechaNacimiento"
        )

        if fecha:

            fecha_texto = fecha.strftime(
                "%d/%m/%Y"
            )

        else:

            fecha_texto = "-"

        self.label_fecha.config(
            text=fecha_texto
        )

        self.label_medico.config(
            text=paciente.get(
                "medico_cabecera",
                "Sin asignar"
            )
        )