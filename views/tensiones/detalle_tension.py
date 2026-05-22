from tkinter import ttk

from views.components.botones import (
    boton_gris
)


class DetalleTension(ttk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, style="App.TFrame")

        self.app = app

        self.crear_titulo()
        self.crear_tarjeta()
        self.crear_botones()

    def crear_titulo(self):

        self.label_titulo = ttk.Label(
            self,
            text="Detalle de Tensión",
            style="TensionTitle.TLabel"
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

        # PACIENTE

        self.label_paciente_titulo = ttk.Label(
            self.frame_card,
            text="Paciente:",
            style="Form.TLabel"
        )

        self.label_paciente = ttk.Label(
            self.frame_card,
            text="",
            style="Info.TLabel"
        )

        # SISTOLICA

        self.label_sistolica_titulo = ttk.Label(
            self.frame_card,
            text="Sistólica:",
            style="Form.TLabel"
        )

        self.label_sistolica = ttk.Label(
            self.frame_card,
            text="",
            style="Info.TLabel"
        )

        # DIASTOLICA

        self.label_diastolica_titulo = ttk.Label(
            self.frame_card,
            text="Diastólica:",
            style="Form.TLabel"
        )

        self.label_diastolica = ttk.Label(
            self.frame_card,
            text="",
            style="Info.TLabel"
        )

        # VALORACION

        self.label_valoracion_titulo = ttk.Label(
            self.frame_card,
            text="Valoración:",
            style="Form.TLabel"
        )

        self.label_valoracion = ttk.Label(
            self.frame_card,
            text="",
            style="Info.TLabel"
        )

        # ESTADO

        self.label_estado_titulo = ttk.Label(
            self.frame_card,
            text="Estado:",
            style="Form.TLabel"
        )

        self.label_estado = ttk.Label(
            self.frame_card,
            text="",
            style="Info.TLabel"
        )

        # GRID

        self.label_paciente_titulo.grid(row=0, column=0, padx=15, pady=10, sticky="e")
        self.label_paciente.grid(row=0, column=1, padx=15, pady=10, sticky="w")

        self.label_sistolica_titulo.grid(row=1, column=0, padx=15, pady=10, sticky="e")
        self.label_sistolica.grid(row=1, column=1, padx=15, pady=10, sticky="w")

        self.label_diastolica_titulo.grid(row=2, column=0, padx=15, pady=10, sticky="e")
        self.label_diastolica.grid(row=2, column=1, padx=15, pady=10, sticky="w")

        self.label_valoracion_titulo.grid(row=3, column=0, padx=15, pady=10, sticky="e")
        self.label_valoracion.grid(row=3, column=1, padx=15, pady=10, sticky="w")

        self.label_estado_titulo.grid(row=4, column=0, padx=15, pady=10, sticky="e")
        self.label_estado.grid(row=4, column=1, padx=15, pady=10, sticky="w")

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
                "lista_tensiones"
            )
        )

        self.boton_volver.grid(
            row=0,
            column=0,
            padx=10
        )

    def cargar_tension(
        self,
        tension,
        nombre_paciente
    ):

        valores = tension.get(
            "valores",
            {}
        )

        self.label_paciente.config(
            text=nombre_paciente
        )

        self.label_sistolica.config(
            text=valores.get(
                "sistolica",
                "-"
            )
        )

        self.label_diastolica.config(
            text=valores.get(
                "diastolica",
                "-"
            )
        )

        self.label_valoracion.config(
            text=tension.get(
                "valoracion",
                "-"
            )
        )

        self.label_estado.config(
            text=tension.get(
                "estado",
                "-"
            )
        )