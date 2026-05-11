import tkinter as tk
from tkinter import ttk, messagebox

from config.styles import (
    COLOR_FONDO,
    COLOR_BLANCO,
    COLOR_TENSION,
    FUENTE_TITULO,
    FUENTE_FORMULARIO,
    FUENTE_FORMULARIO_NEGRITA
)

from widgets.botones import BotonTension, BotonGris


class CrearTension(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg=COLOR_FONDO)

        self.controller = controller
        self.mapa_pacientes = {}

        self.crear_titulo()
        self.crear_formulario()
        self.crear_botones()

    def crear_titulo(self):
        titulo = tk.Label(
            self,
            text="Registro de Tensión Arterial",
            font=FUENTE_TITULO,
            fg=COLOR_TENSION,
            bg=COLOR_FONDO
        )

        titulo.pack(pady=30)

    def crear_formulario(self):
        self.card = tk.Frame(
            self,
            bg=COLOR_BLANCO,
            bd=1,
            relief="solid"
        )

        self.card.pack(pady=10, ipadx=30, ipady=20)

        form_frame = tk.Frame(
            self.card,
            bg=COLOR_BLANCO
        )

        form_frame.pack(padx=30, pady=20)

        tk.Label(
            form_frame,
            text="Paciente:",
            font=FUENTE_FORMULARIO_NEGRITA,
            bg=COLOR_BLANCO
        ).grid(row=0, column=0, padx=15, pady=15, sticky="e")

        self.combo_paciente = ttk.Combobox(
            form_frame,
            width=30,
            state="readonly",
            font=FUENTE_FORMULARIO
        )

        self.combo_paciente.grid(row=0, column=1, pady=15)

        tk.Label(
            form_frame,
            text="Sistólica:",
            font=FUENTE_FORMULARIO_NEGRITA,
            bg=COLOR_BLANCO
        ).grid(row=1, column=0, padx=15, pady=15, sticky="e")

        self.entry_sistolica = tk.Entry(
            form_frame,
            width=33,
            font=FUENTE_FORMULARIO
        )

        self.entry_sistolica.grid(row=1, column=1, pady=15)

        tk.Label(
            form_frame,
            text="Diastólica:",
            font=FUENTE_FORMULARIO_NEGRITA,
            bg=COLOR_BLANCO
        ).grid(row=2, column=0, padx=15, pady=15, sticky="e")

        self.entry_diastolica = tk.Entry(
            form_frame,
            width=33,
            font=FUENTE_FORMULARIO
        )

        self.entry_diastolica.grid(row=2, column=1, pady=15)

        tk.Label(
            form_frame,
            text="Valoración:",
            font=FUENTE_FORMULARIO_NEGRITA,
            bg=COLOR_BLANCO
        ).grid(row=3, column=0, padx=15, pady=15, sticky="e")

        self.combo_valoracion = ttk.Combobox(
            form_frame,
            values=[
                "Normal",
                "Normal-alta",
                "Hipertensión Etapa 1",
                "Hipertensión Etapa 2",
                "Hipertensión severa",
                "Hipertensión sistólica",
                "Hipotensión"
            ],
            width=30,
            state="readonly",
            font=FUENTE_FORMULARIO
        )

        self.combo_valoracion.grid(row=3, column=1, pady=15)
        self.combo_valoracion.set("Normal")

    def crear_botones(self):
        botones = tk.Frame(
            self.card,
            bg=COLOR_BLANCO
        )

        botones.pack(pady=20)

        BotonTension(
            botones,
            text="💾 Guardar registro",
            command=self.guardar_tension,
            width=20
        ).grid(row=0, column=0, padx=15)

        BotonGris(
            botones,
            text="⬅️ Cancelar",
            command=lambda: self.controller.show_frame("menu"),
            width=18
        ).grid(row=0, column=1, padx=15)

    def actualizar_datos(self):
        pacientes = self.controller.paciente_service.obtener_pacientes()

        nombres = []
        self.mapa_pacientes.clear()

        for paciente in pacientes:
            nombre_completo = (
                f"{paciente.get('nombre', '')} "
                f"{paciente.get('apellido', '')}"
            ).strip()

            if nombre_completo:
                nombres.append(nombre_completo)
                self.mapa_pacientes[nombre_completo] = paciente.get("_id")

        self.combo_paciente["values"] = nombres

        if nombres:
            self.combo_paciente.set(nombres[0])

    def guardar_tension(self):
        nombre_seleccionado = self.combo_paciente.get()

        id_paciente = self.mapa_pacientes.get(
            nombre_seleccionado,
            ""
        )

        datos = {
            "id_paciente": id_paciente,
            "sistólica": self.entry_sistolica.get().strip(),
            "diastólica": self.entry_diastolica.get().strip(),
            "valoración": self.combo_valoracion.get()
        }

        try:
            self.controller.tension_service.crear_tension(datos)

            messagebox.showinfo(
                "Registro guardado",
                "La tensión arterial ha sido registrada correctamente"
            )

            self.limpiar_formulario()
            self.controller.show_frame("menu")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def limpiar_formulario(self):
        self.entry_sistolica.delete(0, tk.END)
        self.entry_diastolica.delete(0, tk.END)
        self.combo_valoracion.set("Normal")