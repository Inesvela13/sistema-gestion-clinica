from tkinter import ttk


def boton_primario(
    parent,
    texto,
    comando,
    ancho=24
):

    return ttk.Button(
        parent,
        text=texto,
        command=comando,
        width=ancho,
        style="Primary.TButton"
    )


def boton_exito(
    parent,
    texto,
    comando,
    ancho=24
):

    return ttk.Button(
        parent,
        text=texto,
        command=comando,
        width=ancho,
        style="Success.TButton"
    )


def boton_tension(
    parent,
    texto,
    comando,
    ancho=24
):

    return ttk.Button(
        parent,
        text=texto,
        command=comando,
        width=ancho,
        style="Tension.TButton"
    )


def boton_secundario(
    parent,
    texto,
    comando,
    ancho=24
):

    return ttk.Button(
        parent,
        text=texto,
        command=comando,
        width=ancho,
        style="Secondary.TButton"
    )


def boton_gris(
    parent,
    texto,
    comando,
    ancho=24
):

    return ttk.Button(
        parent,
        text=texto,
        command=comando,
        width=ancho,
        style="Secondary.TButton"
    )


def boton_error(
    parent,
    texto,
    comando,
    ancho=24
):

    return ttk.Button(
        parent,
        text=texto,
        command=comando,
        width=ancho,
        style="Tension.TButton"
    )