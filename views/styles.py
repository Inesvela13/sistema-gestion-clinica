from tkinter import ttk


COLOR_FONDO = "#F4F6F9"

COLOR_SIDEBAR = "#0D2C54"

COLOR_AZUL = "#1565C0"

COLOR_VERDE = "#2E7D32"

COLOR_ROSA = "#C2185B"

COLOR_GRIS = "#5F6368"

COLOR_BLANCO = "#FFFFFF"

FUENTE_TITULO = ("Segoe UI", 30, "bold")

FUENTE_SUBTITULO = ("Segoe UI", 13)

FUENTE_CARD = ("Segoe UI", 20, "bold")

FUENTE_BOTON = ("Segoe UI", 12, "bold")


def configurar_estilos():

    style = ttk.Style()

    style.theme_use("clam")

    # FONDOS

    style.configure(
        "App.TFrame",
        background=COLOR_FONDO
    )

    style.configure(
        "Sidebar.TFrame",
        background=COLOR_SIDEBAR
    )

    style.configure(
        "Content.TFrame",
        background=COLOR_FONDO
    )

    style.configure(
        "Card.TFrame",
        background=COLOR_BLANCO,
        relief="flat",
        borderwidth=0
    )

    # TITULOS

    style.configure(
        "SidebarTitle.TLabel",
        background=COLOR_SIDEBAR,
        foreground=COLOR_BLANCO,
        font=("Segoe UI", 24, "bold")
    )

    style.configure(
        "SidebarText.TLabel",
        background=COLOR_SIDEBAR,
        foreground=COLOR_BLANCO,
        font=("Segoe UI", 12)
    )

    style.configure(
        "DashboardTitle.TLabel",
        background=COLOR_FONDO,
        foreground="#1E3A5F",
        font=FUENTE_TITULO
    )

    style.configure(
        "DashboardSubtitle.TLabel",
        background=COLOR_FONDO,
        foreground="#616161",
        font=FUENTE_SUBTITULO
    )

    style.configure(
        "CardTitle.TLabel",
        background=COLOR_BLANCO,
        foreground=COLOR_AZUL,
        font=FUENTE_CARD
    )

    style.configure(
        "CardTitlePink.TLabel",
        background=COLOR_BLANCO,
        foreground=COLOR_ROSA,
        font=FUENTE_CARD
    )

    # BOTONES AZULES

    style.configure(
        "Primary.TButton",
        background=COLOR_AZUL,
        foreground=COLOR_BLANCO,
        font=FUENTE_BOTON,
        padding=14,
        borderwidth=0
    )

    style.map(
        "Primary.TButton",
        background=[("active", "#1976D2")]
    )

    # BOTONES VERDES

    style.configure(
        "Success.TButton",
        background=COLOR_VERDE,
        foreground=COLOR_BLANCO,
        font=FUENTE_BOTON,
        padding=14,
        borderwidth=0
    )

    style.map(
        "Success.TButton",
        background=[("active", "#388E3C")]
    )

    # BOTONES ROSAS

    style.configure(
        "Tension.TButton",
        background=COLOR_ROSA,
        foreground=COLOR_BLANCO,
        font=FUENTE_BOTON,
        padding=14,
        borderwidth=0
    )

    style.map(
        "Tension.TButton",
        background=[("active", "#D81B60")]
    )

    # BOTONES GRISES

    style.configure(
        "Secondary.TButton",
        background="#ECEFF1",
        foreground="#37474F",
        font=FUENTE_BOTON,
        padding=14,
        borderwidth=0
    )

    # LABELS GENERALES

    style.configure(
        "Form.TLabel",
        background=COLOR_FONDO,
        foreground="#263238",
        font=("Segoe UI", 12, "bold")
    )

    style.configure(
        "Info.TLabel",
        background=COLOR_BLANCO,
        foreground="#37474F",
        font=("Segoe UI", 12)
    )

    style.configure(
        "TensionTitle.TLabel",
        background=COLOR_FONDO,
        foreground=COLOR_ROSA,
        font=("Segoe UI", 26, "bold")
    )