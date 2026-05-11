import tkinter as tk
from tkinter import ttk, messagebox

from config.styles import (
    COLOR_FONDO,
    COLOR_BLANCO,
    COLOR_PRIMARIO,
    FUENTE_TITULO,
    FUENTE_FORMULARIO,
    FUENTE_FORMULARIO_NEGRITA
)

from widgets.botones import (
    BotonExito,
    BotonGris
)


class CrearPaciente(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLOR_FONDO)

        self.controller = controller

        self.crear_titulo()
        self.crear_formulario()
        self.crear_botones()

    # =========================================
    # TÍTULO
    # =========================================

    def crear_titulo(self):

        titulo = tk.Label(
            self,
            text="Alta de Nuevo Paciente",
            font=FUENTE_TITULO,
            fg=COLOR_PRIMARIO,
            bg=COLOR_FONDO
        )

        titulo.pack(pady=30)

    # =========================================
    # FORMULARIO
    # =========================================

    def crear_formulario(self):

        self.card = tk.Frame(
            self,
            bg=COLOR_BLANCO,
            bd=1,
            relief="solid"
        )

        self.card.pack(
            pady=10,
            ipadx=30,
            ipady=20
        )

        form_frame = tk.Frame(
            self.card,
            bg=COLOR_BLANCO
        )

        form_frame.pack(
            padx=30,
            pady=20
        )

        # =========================
        # NOMBRE
        # =========================

        tk.Label(
            form_frame,
            text="Nombre:",
            font=FUENTE_FORMULARIO_NEGRITA,
            bg=COLOR_BLANCO
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=15,
            sticky="e"
        )

        self.entry_nombre = tk.Entry(
            form_frame,
            width=30,
            font=FUENTE_FORMULARIO
        )

        self.entry_nombre.grid(
            row=0,
            column=1,
            pady=15
        )

        # =========================
        # APELLIDO
        # =========================

        tk.Label(
            form_frame,
            text="Apellido:",
            font=FUENTE_FORMULARIO_NEGRITA,
            bg=COLOR_BLANCO
        ).grid(
            row=1,
            column=0,
            padx=15,
            pady=15,
            sticky="e"
        )

        self.entry_apellido = tk.Entry(
            form_frame,
            width=30,
            font=FUENTE_FORMULARIO
        )

        self.entry_apellido.grid(
            row=1,
            column=1,
            pady=15
        )

        # =========================
        # GÉNERO
        # =========================

        tk.Label(
            form_frame,
            text="Género:",
            font=FUENTE_FORMULARIO_NEGRITA,
            bg=COLOR_BLANCO
        ).grid(
            row=2,
            column=0,
            padx=15,
            pady=15,
            sticky="e"
        )

        self.combo_genero = ttk.Combobox(
            form_frame,
            values=[
                "femenino",
                "masculino",
                "otro"
            ],
            width=27,
            state="readonly",
            font=FUENTE_FORMULARIO
        )

        self.combo_genero.grid(
            row=2,
            column=1,
            pady=15
        )

        self.combo_genero.set("femenino")

        # =========================
        # FECHA NACIMIENTO
        # =========================

        tk.Label(
            form_frame,
            text="Fecha nacimiento:",
            font=FUENTE_FORMULARIO_NEGRITA,
            bg=COLOR_BLANCO
        ).grid(
            row=3,
            column=0,
            padx=15,
            pady=15,
            sticky="e"
        )

        self.entry_fecha = tk.Entry(
            form_frame,
            width=30,
            font=FUENTE_FORMULARIO
        )

        self.entry_fecha.grid(
            row=3,
            column=1,
            pady=15
        )

        self.entry_fecha.insert(
            0,
            "1990-01-01"
        )

        # =========================
        # MÉDICO CABECERA
        # =========================

        tk.Label(
            form_frame,
            text="Médico responsable:",
            font=FUENTE_FORMULARIO_NEGRITA,
            bg=COLOR_BLANCO
        ).grid(
            row=4,
            column=0,
            padx=15,
            pady=15,
            sticky="e"
        )

        self.entry_medico = tk.Entry(
            form_frame,
            width=30,
            font=FUENTE_FORMULARIO
        )

        self.entry_medico.grid(
            row=4,
            column=1,
            pady=15
        )

    # =========================================
    # BOTONES
    # =========================================

    def crear_botones(self):

        botones = tk.Frame(
            self.card,
            bg=COLOR_BLANCO
        )

        botones.pack(pady=20)

        BotonExito(
            botones,
            text="💾 Guardar paciente",
            command=self.guardar_paciente,
            width=20
        ).grid(
            row=0,
            column=0,
            padx=15
        )

        BotonGris(
            botones,
            text="⬅️ Cancelar",
            command=lambda: self.controller.show_frame("menu"),
            width=18
        ).grid(
            row=0,
            column=1,
            padx=15
        )

    # =========================================
    # GUARDAR PACIENTE
    # =========================================

    def guardar_paciente(self):

        datos = {

            "nombre": self.entry_nombre.get().strip(),

            "apellido": self.entry_apellido.get().strip(),

            "género": self.combo_genero.get(),

            "fechaNacimiento": self.entry_fecha.get().strip(),

            "medico_cabecera": self.entry_medico.get().strip()
        }

        try:

            self.controller.paciente_service.crear_paciente(
                datos
            )

            messagebox.showinfo(
                "Paciente registrado",
                "El paciente ha sido dado de alta correctamente"
            )

            self.limpiar_formulario()

            self.controller.show_frame("menu")

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # =========================================
    # LIMPIAR FORMULARIO
    # =========================================

    def limpiar_formulario(self):

        self.entry_nombre.delete(0, tk.END)

        self.entry_apellido.delete(0, tk.END)

        self.entry_fecha.delete(0, tk.END)

        self.entry_medico.delete(0, tk.END)

        self.entry_fecha.insert(
            0,
            "1990-01-01"
        )

        self.combo_genero.set(
            "femenino"
        )