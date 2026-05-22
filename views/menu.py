from tkinter import ttk

from views.components.botones import (
    boton_primario,
    boton_exito,
    boton_tension,
    boton_secundario
)


class MenuPrincipal(ttk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, style="App.TFrame")

        self.app = app

        self.crear_layout()

    def crear_layout(self):

        self.sidebar = ttk.Frame(
            self,
            style="Sidebar.TFrame",
            width=260
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.contenido = ttk.Frame(
            self,
            style="Content.TFrame"
        )

        self.contenido.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.crear_sidebar()

        self.crear_dashboard()

    def crear_sidebar(self):

        self.label_logo = ttk.Label(
            self.sidebar,
            text="Sistema de\nGestión Clínica",
            style="SidebarTitle.TLabel",
            justify="center"
        )

        self.label_logo.pack(
            pady=(40, 30)
        )

        self.label_usuario = ttk.Label(
            self.sidebar,
            text="Usuario\nAdministrador",
            style="SidebarText.TLabel",
            justify="center"
        )

        self.label_usuario.pack(
            side="bottom",
            pady=40
        )

    def crear_dashboard(self):

        self.header = ttk.Frame(
            self.contenido,
            style="Content.TFrame"
        )

        self.header.pack(
            fill="x",
            pady=(35, 20)
        )

        self.label_titulo = ttk.Label(
            self.header,
            text="Panel Principal",
            style="DashboardTitle.TLabel"
        )

        self.label_titulo.pack()

        self.label_subtitulo = ttk.Label(
            self.header,
            text=(
                "Seleccione una opción para gestionar "
                "pacientes y tensiones arteriales"
            ),
            style="DashboardSubtitle.TLabel"
        )

        self.label_subtitulo.pack(
            pady=10
        )

        self.cards = ttk.Frame(
            self.contenido,
            style="Content.TFrame"
        )

        self.cards.pack(
            pady=20
        )

        self.crear_card_pacientes()

        self.crear_card_tensiones()

    def crear_card_pacientes(self):

        self.card_pacientes = ttk.Frame(
            self.cards,
            style="Card.TFrame",
            padding=35
        )

        self.card_pacientes.grid(
            row=0,
            column=0,
            padx=25
        )

        self.label_pacientes = ttk.Label(
            self.card_pacientes,
            text="Gestión de Pacientes",
            style="CardTitle.TLabel"
        )

        self.label_pacientes.pack(
            pady=(0, 25)
        )

        self.boton_ver_pacientes = boton_primario(
            self.card_pacientes,
            "Ver Pacientes",
            lambda: self.app.mostrar_vista(
                "lista_pacientes"
            ),
            ancho=24
        )

        self.boton_ver_pacientes.pack(
            pady=10
        )

        self.boton_nuevo_paciente = boton_exito(
            self.card_pacientes,
            "Dar de Alta Paciente",
            lambda: self.app.mostrar_vista(
                "crear_paciente"
            ),
            ancho=24
        )

        self.boton_nuevo_paciente.pack(
            pady=10
        )

    def crear_card_tensiones(self):

        self.card_tensiones = ttk.Frame(
            self.cards,
            style="Card.TFrame",
            padding=35
        )

        self.card_tensiones.grid(
            row=0,
            column=1,
            padx=25
        )

        self.label_tensiones = ttk.Label(
            self.card_tensiones,
            text="Control de Tensión Arterial",
            style="CardTitlePink.TLabel"
        )

        self.label_tensiones.pack(
            pady=(0, 25)
        )

        self.boton_ver_tensiones = boton_tension(
            self.card_tensiones,
            "Ver Tensiones",
            lambda: self.app.mostrar_vista(
                "lista_tensiones"
            ),
            ancho=24
        )

        self.boton_ver_tensiones.pack(
            pady=10
        )

        self.boton_registrar_tension = boton_secundario(
            self.card_tensiones,
            "Registrar Tensión",
            lambda: self.app.mostrar_vista(
                "crear_tension"
            ),
            ancho=24
        )

        self.boton_registrar_tension.pack(
            pady=10
        )

        self.boton_estadisticas = boton_secundario(
            self.card_tensiones,
            "Estadísticas",
            lambda: self.app.mostrar_vista(
                "estadisticas_tensiones"
            ),
            ancho=24
        )

        self.boton_estadisticas.pack(
            pady=10
        )