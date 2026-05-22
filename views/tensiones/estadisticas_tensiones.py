from tkinter import ttk

from views.components.botones import (
    boton_gris
)


class EstadisticasTensiones(ttk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, style="App.TFrame")

        self.app = app

        self.crear_titulo()
        self.crear_tarjeta()
        self.crear_boton()

    def crear_titulo(self):

        self.label_titulo = ttk.Label(
            self,
            text="Estadísticas de Tensiones",
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

        # MEDIA SISTOLICA

        self.label_media_sis_titulo = ttk.Label(
            self.frame_card,
            text="Media Sistólica:",
            style="Form.TLabel"
        )

        self.label_media_sis = ttk.Label(
            self.frame_card,
            text="",
            style="Info.TLabel"
        )

        # MEDIA DIASTOLICA

        self.label_media_dia_titulo = ttk.Label(
            self.frame_card,
            text="Media Diastólica:",
            style="Form.TLabel"
        )

        self.label_media_dia = ttk.Label(
            self.frame_card,
            text="",
            style="Info.TLabel"
        )

        # ULTIMA TENSION

        self.label_ultima_titulo = ttk.Label(
            self.frame_card,
            text="Última Tensión:",
            style="Form.TLabel"
        )

        self.label_ultima = ttk.Label(
            self.frame_card,
            text="",
            style="Info.TLabel"
        )

        # GRID

        self.label_media_sis_titulo.grid(
            row=0,
            column=0,
            padx=15,
            pady=12,
            sticky="e"
        )

        self.label_media_sis.grid(
            row=0,
            column=1,
            padx=15,
            pady=12,
            sticky="w"
        )

        self.label_media_dia_titulo.grid(
            row=1,
            column=0,
            padx=15,
            pady=12,
            sticky="e"
        )

        self.label_media_dia.grid(
            row=1,
            column=1,
            padx=15,
            pady=12,
            sticky="w"
        )

        self.label_ultima_titulo.grid(
            row=2,
            column=0,
            padx=15,
            pady=12,
            sticky="e"
        )

        self.label_ultima.grid(
            row=2,
            column=1,
            padx=15,
            pady=12,
            sticky="w"
        )

    def crear_boton(self):

        self.frame_boton = ttk.Frame(
            self,
            style="App.TFrame"
        )

        self.frame_boton.pack(
            pady=20
        )

        self.boton_volver = boton_gris(
            self.frame_boton,
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

    def cargar_estadisticas(self):

        tensiones = (
            self.app.tension_controller
            .obtener_tensiones()
        )

        medias = (
            self.app.tension_controller
            .tension_service
            .calcular_media_tensiones(
                tensiones
            )
        )

        ultima = (
            self.app.tension_controller
            .tension_service
            .obtener_ultima_tension(
                tensiones
            )
        )

        self.label_media_sis.config(
            text=f"{medias['media_sistolica']} mmHg"
        )

        self.label_media_dia.config(
            text=f"{medias['media_diastolica']} mmHg"
        )

        if ultima:

            valores = ultima.get(
                "valores",
                {}
            )

            texto_ultima = (
                f"{valores.get('sistolica', '-')}/"
                f"{valores.get('diastolica', '-')}"
            )

        else:

            texto_ultima = "Sin registros"

        self.label_ultima.config(
            text=texto_ultima
        )