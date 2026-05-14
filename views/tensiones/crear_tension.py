from tkinter import ttk, messagebox

from views.components.botones import boton_tension, boton_gris


class CrearTension(ttk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, style="App.TFrame")

        self.app = app
        self.mapa_pacientes = {}

        self.crear_titulo()
        self.crear_formulario()
        self.crear_botones()

    def crear_titulo(self):
        self.label_titulo = ttk.Label(
            self,
            text="Registro de Tensión Arterial",
            style="TensionTitle.TLabel"
        )

        self.label_titulo.pack(pady=25)

    def crear_formulario(self):
        self.formulario = ttk.Frame(
            self,
            style="Card.TFrame",
            padding=30
        )

        self.formulario.pack(pady=10)

        self.label_paciente = ttk.Label(
            self.formulario,
            text="Paciente:",
            style="Form.TLabel"
        )

        self.combo_paciente = ttk.Combobox(
            self.formulario,
            state="readonly",
            width=32
        )

        self.label_sistolica = ttk.Label(
            self.formulario,
            text="Sistólica:",
            style="Form.TLabel"
        )

        self.entry_sistolica = ttk.Entry(
            self.formulario,
            width=34
        )

        self.label_diastolica = ttk.Label(
            self.formulario,
            text="Diastólica:",
            style="Form.TLabel"
        )

        self.entry_diastolica = ttk.Entry(
            self.formulario,
            width=34
        )

        self.label_valoracion = ttk.Label(
            self.formulario,
            text="Valoración:",
            style="Form.TLabel"
        )

        self.combo_valoracion = ttk.Combobox(
            self.formulario,
            values=[
                "Normal",
                "Elevada",
                "Hipertensión Etapa 1",
                "Hipertensión Etapa 2",
                "Crisis hipertensiva",
                "Hipotensión"
            ],
            state="readonly",
            width=32
        )

        self.label_paciente.grid(row=0, column=0, padx=15, pady=12, sticky="e")
        self.combo_paciente.grid(row=0, column=1, padx=15, pady=12)

        self.label_sistolica.grid(row=1, column=0, padx=15, pady=12, sticky="e")
        self.entry_sistolica.grid(row=1, column=1, padx=15, pady=12)

        self.label_diastolica.grid(row=2, column=0, padx=15, pady=12, sticky="e")
        self.entry_diastolica.grid(row=2, column=1, padx=15, pady=12)

        self.label_valoracion.grid(row=3, column=0, padx=15, pady=12, sticky="e")
        self.combo_valoracion.grid(row=3, column=1, padx=15, pady=12)

        self.combo_valoracion.set("Normal")

    def crear_botones(self):
        self.frame_botones = ttk.Frame(
            self,
            style="App.TFrame"
        )

        self.frame_botones.pack(pady=20)

        self.boton_guardar = boton_tension(
            self.frame_botones,
            "Guardar tensión",
            self.guardar_tension
        )

        self.boton_cancelar = boton_gris(
            self.frame_botones,
            "Cancelar",
            lambda: self.app.mostrar_vista("menu")
        )

        self.boton_guardar.grid(row=0, column=0, padx=10)
        self.boton_cancelar.grid(row=0, column=1, padx=10)

    def actualizar_datos(self):
        pacientes = self.app.tension_controller.obtener_pacientes()

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
        nombre_paciente = self.combo_paciente.get()

        datos = {
            "id_paciente": self.mapa_pacientes.get(nombre_paciente, ""),
            "sistolica": self.entry_sistolica.get().strip(),
            "diastolica": self.entry_diastolica.get().strip(),
            "valoracion": self.combo_valoracion.get()
        }

        try:
            self.app.tension_controller.crear_tension(datos)

            messagebox.showinfo(
                "Registro guardado",
                "La tensión arterial ha sido registrada correctamente"
            )

            self.limpiar_formulario()
            self.app.mostrar_vista("lista_tensiones")

        except Exception as error:
            messagebox.showerror("Error", str(error))

    def limpiar_formulario(self):
        self.entry_sistolica.delete(0, "end")
        self.entry_diastolica.delete(0, "end")
        self.combo_valoracion.set("Normal")