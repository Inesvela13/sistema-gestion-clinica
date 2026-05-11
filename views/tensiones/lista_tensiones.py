import tkinter as tk
from tkinter import ttk, messagebox

from config.styles import (
    COLOR_FONDO,
    COLOR_TENSION,
    FUENTE_TITULO
)

from widgets.botones import BotonTension, BotonError, BotonGris


class ListaTensiones(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLOR_FONDO)

        self.controller = controller
        self.ids_tensiones = {}

        self.crear_titulo()
        self.crear_tabla()
        self.crear_botones()

    def crear_titulo(self):
        titulo = tk.Label(
            self,
            text="Registro de Tensiones",
            font=FUENTE_TITULO,
            fg=COLOR_TENSION,
            bg=COLOR_FONDO
        )

        titulo.pack(pady=25)

    def crear_tabla(self):
        tabla_frame = tk.Frame(
            self,
            bg=COLOR_FONDO
        )

        tabla_frame.pack(padx=30, pady=10)

        columnas = (
            "Paciente",
            "Sistolica",
            "Diastolica",
            "Valoracion",
            "Estado"
        )

        self.tree = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings",
            height=14
        )

        self.tree.heading("Paciente", text="Paciente")
        self.tree.heading("Sistolica", text="Sistólica")
        self.tree.heading("Diastolica", text="Diastólica")
        self.tree.heading("Valoracion", text="Valoración")
        self.tree.heading("Estado", text="Estado")

        self.tree.column("Paciente", width=260)
        self.tree.column("Sistolica", width=130, anchor="center")
        self.tree.column("Diastolica", width=130, anchor="center")
        self.tree.column("Valoracion", width=300)
        self.tree.column("Estado", width=130, anchor="center")

        self.tree.pack(side="left")

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(side="right", fill="y")

    def crear_botones(self):
        botones = tk.Frame(
            self,
            bg=COLOR_FONDO
        )

        botones.pack(pady=25)

        BotonTension(
            botones,
            text="➕ Registrar tensión",
            command=lambda: self.controller.show_frame("crear_tension"),
            width=20
        ).grid(row=0, column=0, padx=10)

        BotonError(
            botones,
            text="❌ Dar de baja",
            command=self.eliminar,
            width=18
        ).grid(row=0, column=1, padx=10)

        BotonGris(
            botones,
            text="⬅️ Volver",
            command=lambda: self.controller.show_frame("menu"),
            width=18
        ).grid(row=0, column=2, padx=10)

    def actualizar_datos(self):
        self.cargar()

    def cargar(self):
        self.limpiar_tabla()

        pacientes = self.controller.paciente_service.obtener_pacientes()
        tensiones = self.controller.tension_service.obtener_tensiones()

        mapa_pacientes = {
            paciente.get("_id"): (
                f"{paciente.get('nombre', '')} "
                f"{paciente.get('apellido', '')}"
            ).strip()
            for paciente in pacientes
        }

        for tension in tensiones:
            id_paciente = tension.get("id_paciente")

            nombre_paciente = mapa_pacientes.get(
                id_paciente,
                "Paciente no encontrado"
            )

            valores = tension.get("valores", {})

            sistolica = valores.get("sistólica", valores.get("sistolica", "-"))
            diastolica = valores.get("diastólica", valores.get("diastolica", "-"))

            item = self.tree.insert(
                "",
                "end",
                values=(
                    nombre_paciente,
                    sistolica,
                    diastolica,
                    tension.get("valoración", tension.get("valoracion", "-")),
                    tension.get("estado", "-")
                )
            )

            self.ids_tensiones[item] = tension.get("_id")

    def limpiar_tabla(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.ids_tensiones.clear()

    def eliminar(self):
        seleccionado = self.tree.focus()

        if not seleccionado:
            messagebox.showwarning(
                "Aviso",
                "Seleccione un registro"
            )
            return

        id_tension = self.ids_tensiones[seleccionado]

        paciente = self.tree.item(
            seleccionado
        )["values"][0]

        confirmar = messagebox.askyesno(
            "Confirmar baja",
            f"¿Desea eliminar el registro de tensión de:\n\n{paciente}?"
        )

        if confirmar:
            self.controller.tension_service.eliminar_tension(
                id_tension
            )

            messagebox.showinfo(
                "Registro eliminado",
                "La tensión arterial ha sido eliminada correctamente"
            )

            self.cargar()