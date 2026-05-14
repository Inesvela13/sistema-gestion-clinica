from tkinter import ttk


def boton_primario(parent, texto, comando, ancho=20):
    return ttk.Button(
        parent,
        text=texto,
        command=comando,
        width=ancho,
        style="Primary.TButton"
    )


def boton_exito(parent, texto, comando, ancho=20):
    return ttk.Button(
        parent,
        text=texto,
        command=comando,
        width=ancho,
        style="Success.TButton"
    )


def boton_error(parent, texto, comando, ancho=20):
    return ttk.Button(
        parent,
        text=texto,
        command=comando,
        width=ancho,
        style="Danger.TButton"
    )


def boton_gris(parent, texto, comando, ancho=20):
    return ttk.Button(
        parent,
        text=texto,
        command=comando,
        width=ancho,
        style="Grey.TButton"
    )


def boton_tension(parent, texto, comando, ancho=20):
    return ttk.Button(
        parent,
        text=texto,
        command=comando,
        width=ancho,
        style="Tension.TButton"
    )