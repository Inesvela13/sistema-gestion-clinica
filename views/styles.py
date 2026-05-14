from tkinter import ttk

COLOR_FONDO = "#F5F7FA"
COLOR_BLANCO = "#FFFFFF"
COLOR_PRIMARIO = "#1565C0"
COLOR_PRIMARIO_OSCURO = "#0D47A1"
COLOR_EXITO = "#2E7D32"
COLOR_ERROR = "#C62828"
COLOR_GRIS = "#757575"
COLOR_TENSION = "#AD1457"
COLOR_TEXTO = "#37474F"
COLOR_TEXTO_SECUNDARIO = "#607D8B"

FUENTE_TITULO = ("Segoe UI", 22, "bold")
FUENTE_SUBTITULO = ("Segoe UI", 14, "bold")
FUENTE_NORMAL = ("Segoe UI", 10)
FUENTE_NORMAL_NEGRITA = ("Segoe UI", 10, "bold")
FUENTE_FORMULARIO = ("Segoe UI", 11)
FUENTE_FORMULARIO_NEGRITA = ("Segoe UI", 11, "bold")


def configurar_estilos():
    style = ttk.Style()
    style.theme_use("clam")

    style.configure(
        "App.TFrame",
        background=COLOR_FONDO
    )

    style.configure(
        "Card.TFrame",
        background=COLOR_BLANCO,
        relief="solid",
        borderwidth=1
    )

    style.configure(
        "Title.TLabel",
        background=COLOR_FONDO,
        foreground=COLOR_PRIMARIO,
        font=FUENTE_TITULO
    )

    style.configure(
        "TensionTitle.TLabel",
        background=COLOR_FONDO,
        foreground=COLOR_TENSION,
        font=FUENTE_TITULO
    )

    style.configure(
        "Form.TLabel",
        background=COLOR_BLANCO,
        foreground=COLOR_TEXTO,
        font=FUENTE_FORMULARIO_NEGRITA
    )

    style.configure(
        "Subtitle.TLabel",
        background=COLOR_BLANCO,
        foreground=COLOR_TEXTO,
        font=FUENTE_SUBTITULO
    )

    style.configure(
        "TEntry",
        font=FUENTE_FORMULARIO,
        padding=5
    )

    style.configure(
        "TCombobox",
        font=FUENTE_FORMULARIO,
        padding=5
    )

    style.configure(
        "Primary.TButton",
        background=COLOR_PRIMARIO,
        foreground=COLOR_BLANCO,
        font=FUENTE_NORMAL_NEGRITA,
        padding=8
    )

    style.configure(
        "Success.TButton",
        background=COLOR_EXITO,
        foreground=COLOR_BLANCO,
        font=FUENTE_NORMAL_NEGRITA,
        padding=8
    )

    style.configure(
        "Danger.TButton",
        background=COLOR_ERROR,
        foreground=COLOR_BLANCO,
        font=FUENTE_NORMAL_NEGRITA,
        padding=8
    )

    style.configure(
        "Grey.TButton",
        background=COLOR_GRIS,
        foreground=COLOR_BLANCO,
        font=FUENTE_NORMAL_NEGRITA,
        padding=8
    )

    style.configure(
        "Tension.TButton",
        background=COLOR_TENSION,
        foreground=COLOR_BLANCO,
        font=FUENTE_NORMAL_NEGRITA,
        padding=8
    )

    style.configure(
        "Treeview",
        background=COLOR_BLANCO,
        fieldbackground=COLOR_BLANCO,
        foreground=COLOR_TEXTO,
        rowheight=34,
        font=FUENTE_NORMAL
    )

    style.configure(
        "Treeview.Heading",
        background=COLOR_PRIMARIO,
        foreground=COLOR_BLANCO,
        font=("Segoe UI", 11, "bold"),
        padding=8
    )

    style.map(
        "Treeview",
        background=[("selected", "#90CAF9")],
        foreground=[("selected", COLOR_PRIMARIO_OSCURO)]
    )