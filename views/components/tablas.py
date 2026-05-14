from tkinter import ttk


def crear_tabla(parent, columnas, encabezados, anchos, alto=12):
    frame_tabla = ttk.Frame(parent, style="App.TFrame")

    tabla = ttk.Treeview(
        frame_tabla,
        columns=columnas,
        show="headings",
        height=alto
    )

    for columna in columnas:
        tabla.heading(columna, text=encabezados[columna])
        tabla.column(
            columna,
            width=anchos.get(columna, 150),
            anchor="center"
        )

    scrollbar = ttk.Scrollbar(
        frame_tabla,
        orient="vertical",
        command=tabla.yview
    )

    tabla.configure(
        yscrollcommand=scrollbar.set
    )

    tabla.grid(row=0, column=0, sticky="nsew")
    scrollbar.grid(row=0, column=1, sticky="ns")

    frame_tabla.grid_columnconfigure(0, weight=1)
    frame_tabla.grid_rowconfigure(0, weight=1)

    return frame_tabla, tabla