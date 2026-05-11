import tkinter as tk

from config.styles import (
    FUENTE_NORMAL_NEGRITA,
    ANCHO_BOTON,
    ALTO_BOTON,
    COLOR_PRIMARIO,
    COLOR_EXITO,
    COLOR_ERROR,
    COLOR_GRIS,
    COLOR_TENSION
)


class BotonBase(tk.Button):
    def __init__(self, parent, text, command, color, width=ANCHO_BOTON):
        super().__init__(
            parent,
            text=text,
            command=command,
            bg=color,
            fg="white",
            font=FUENTE_NORMAL_NEGRITA,
            width=width,
            height=ALTO_BOTON,
            relief="flat",
            cursor="hand2"
        )


class BotonPrimario(BotonBase):
    def __init__(self, parent, text, command, width=ANCHO_BOTON):
        super().__init__(
            parent,
            text=text,
            command=command,
            color=COLOR_PRIMARIO,
            width=width
        )


class BotonExito(BotonBase):
    def __init__(self, parent, text, command, width=ANCHO_BOTON):
        super().__init__(
            parent,
            text=text,
            command=command,
            color=COLOR_EXITO,
            width=width
        )


class BotonError(BotonBase):
    def __init__(self, parent, text, command, width=ANCHO_BOTON):
        super().__init__(
            parent,
            text=text,
            command=command,
            color=COLOR_ERROR,
            width=width
        )


class BotonGris(BotonBase):
    def __init__(self, parent, text, command, width=ANCHO_BOTON):
        super().__init__(
            parent,
            text=text,
            command=command,
            color=COLOR_GRIS,
            width=width
        )


class BotonTension(BotonBase):
    def __init__(self, parent, text, command, width=ANCHO_BOTON):
        super().__init__(
            parent,
            text=text,
            command=command,
            color=COLOR_TENSION,
            width=width
        )