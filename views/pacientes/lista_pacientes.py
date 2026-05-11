import tkinter as tk
from tkinter import ttk, messagebox

from config.styles import (
    COLOR_FONDO,
    COLOR_PRIMARIO,
    FUENTE_TITULO,
    FUENTE_FORMULARIO,
    FUENTE_FORMULARIO_NEGRITA
)

from widgets.botones import (
    BotonExito,
    BotonError,
    BotonGris
)


class ListaPacientes(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLOR_FONDO)

        self.controller = controller

        self.ids_pacientes = {}

        self.crear_titulo()
        self.crear_buscador()
        self.crear_tabla()
        self.crear_botones()

    # =========================================
    # TÍTULO
    # =========================================

    def crear_titulo(self):

        titulo = tk.Label(
            self,
            text="Gestión de Pacientes",
            font=FUENTE_TITULO,
            bg=COLOR_FONDO,
            fg=COLOR_PRIMARIO
        )

        titulo.pack(pady=20)

    # =========================================
    # BUSCADOR
    # =========================================

    def crear_buscador(self):

        buscador_frame = tk.Frame(
            self,
            bg=COLOR_FONDO
        )

        buscador_frame.pack(
            fill="x",
            padx=30
        )

        tk.Label(
            buscador_frame,
            text="Buscar paciente:",
            font=FUENTE_FORMULARIO_NEGRITA,
            bg=COLOR_FONDO
        ).pack(side="left")

        self.entry_busqueda = tk.Entry(
            buscador_frame,
            font=FUENTE_FORMULARIO,
            width=30
        )

        self.entry_busqueda.pack(
            side="left",
            padx=10
        )

        self.entry_busqueda.bind(
            "<KeyRelease>",
            lambda evento: self.cargar()
        )

    # =========================================
    # TABLA
    # =========================================

    def crear_tabla(self):

        tabla_frame = tk.Frame(
            self,
            bg=COLOR_FONDO
        )

        tabla_frame.pack(
            padx=30,
            pady=20
        )

        columnas = (
            "Nombre",
            "Genero",
            "Fecha",
            "Medico"
        )

        self.tree = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings",
            height=12
        )

        # =========================
        # CABECERAS
        # =========================

        self.tree.heading(
            "Nombre",
            text="Nombre completo"
        )

        self.tree.heading(
            "Genero",
            text="Género"
        )

        self.tree.heading(
            "Fecha",
            text="Fecha nacimiento"
        )

        self.tree.heading(
            "Medico",
            text="Médico responsable"
        )

        # =========================
        # COLUMNAS
        # =========================

        self.tree.column(
            "Nombre",
            width=320
        )

        self.tree.column(
            "Genero",
            width=150,
            anchor="center"
        )

        self.tree.column(
            "Fecha",
            width=180,
            anchor="center"
        )

        self.tree.column(
            "Medico",
            width=260
        )

        self.tree.pack(side="left")

        # =========================
        # SCROLLBAR
        # =========================

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

    # =========================================
    # BOTONES
    # =========================================

    def crear_botones(self):

        botones = tk.Frame(
            self,
            bg=COLOR_FONDO
        )

        botones.pack(pady=20)

        # =========================
        # DAR DE ALTA
        # =========================

        BotonExito(
            botones,
            text="➕ Dar de alta",
            command=lambda: self.controller.show_frame(
                "crear_paciente"
            )
        ).grid(
            row=0,
            column=0,
            padx=10
        )

        # =========================
        # DAR DE BAJA
        # =========================

        BotonError(
            botones,
            text="❌ Dar de baja",
            command=self.eliminar
        ).grid(
            row=0,
            column=1,
            padx=10
        )

        # =========================
        # VOLVER
        # =========================

        BotonGris(
            botones,
            text="⬅️ Volver",
            command=lambda: self.controller.show_frame(
                "menu"
            )
        ).grid(
            row=0,
            column=2,
            padx=10
        )

    # =========================================
    # ACTUALIZAR DATOS
    # =========================================

    def actualizar_datos(self):

        self.cargar()

    # =========================================
    # CARGAR PACIENTES
    # =========================================

    def cargar(self):

        self.limpiar_tabla()

        texto_busqueda = self.entry_busqueda.get().lower()

        pacientes = self.controller.paciente_service.obtener_pacientes()

        for paciente in pacientes:

            nombre_completo = self.obtener_nombre_completo(
                paciente
            )

            if texto_busqueda not in nombre_completo.lower():
                continue

            genero = self.formatear_genero(
                paciente.get(
                    "género",
                    "No especificado"
                )
            )

            fecha = self.formatear_fecha(
                paciente.get(
                    "fechaNacimiento"
                )
            )

            medico = paciente.get(
                "medico_cabecera",
                "Sin asignar"
            )

            item = self.tree.insert(
                "",
                "end",
                values=(
                    nombre_completo,
                    genero,
                    fecha,
                    medico
                )
            )

            self.ids_pacientes[item] = paciente.get("_id")

    # =========================================
    # LIMPIAR TABLA
    # =========================================

    def limpiar_tabla(self):

        for row in self.tree.get_children():
            self.tree.delete(row)

        self.ids_pacientes.clear()

    # =========================================
    # NOMBRE COMPLETO
    # =========================================

    def obtener_nombre_completo(self, paciente):

        return (
            f"{paciente.get('nombre', '')} "
            f"{paciente.get('apellido', '')}"
        ).strip()

    # =========================================
    # FORMATEAR GÉNERO
    # =========================================

    def formatear_genero(self, genero):

        if not genero:
            return "No especificado"

        if genero.lower() == "femenino":
            return "👩 Femenino"

        if genero.lower() == "masculino":
            return "👨 Masculino"

        if genero.lower() == "otro":
            return "⚧ Otro"

        return genero.capitalize()

    # =========================================
    # FORMATEAR FECHA
    # =========================================

    def formatear_fecha(self, fecha):

        if not fecha:
            return ""

        return fecha.strftime("%d/%m/%Y")

    # =========================================
    # ELIMINAR PACIENTE
    # =========================================

    def eliminar(self):

        seleccionado = self.tree.focus()

        if not seleccionado:

            messagebox.showwarning(
                "Aviso",
                "Seleccione un paciente"
            )

            return

        id_paciente = self.ids_pacientes[
            seleccionado
        ]

        nombre = self.tree.item(
            seleccionado
        )["values"][0]

        confirmar = messagebox.askyesno(
            "Confirmar baja",
            f"¿Desea dar de baja al paciente?\n\n{nombre}\n\nEsta acción no se puede deshacer."
        )

        if confirmar:

            self.controller.paciente_service.eliminar_paciente(
                id_paciente
            )

            messagebox.showinfo(
                "Paciente eliminado",
                "El paciente ha sido dado de baja correctamente"
            )

            self.cargar()