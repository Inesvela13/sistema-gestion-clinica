from tkinter import ttk, messagebox

from views.components.botones import boton_exito, boton_gris


class CrearPaciente(ttk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, style="App.TFrame")

        self.app = app

        self.crear_titulo()
        self.crear_formulario()
        self.crear_botones()

    def crear_titulo(self):
        self.label_titulo = ttk.Label(
            self,
            text="Alta de Nuevo Paciente",
            style="Title.TLabel"
        )

        self.label_titulo.pack(pady=25)

    def crear_formulario(self):
        self.formulario = ttk.Frame(
            self,
            style="Card.TFrame",
            padding=30
        )

        self.formulario.pack(pady=10)

        self.label_nombre = ttk.Label(
            self.formulario,
            text="Nombre:",
            style="Form.TLabel"
        )

        self.entry_nombre = ttk.Entry(
            self.formulario,
            width=32
        )

        self.label_apellido = ttk.Label(
            self.formulario,
            text="Apellido:",
            style="Form.TLabel"
        )

        self.entry_apellido = ttk.Entry(
            self.formulario,
            width=32
        )

        self.label_genero = ttk.Label(
            self.formulario,
            text="Género:",
            style="Form.TLabel"
        )

        self.combo_genero = ttk.Combobox(
            self.formulario,
            values=["femenino", "masculino", "otro"],
            state="readonly",
            width=30
        )

        self.label_fecha = ttk.Label(
            self.formulario,
            text="Fecha nacimiento:",
            style="Form.TLabel"
        )

        self.entry_fecha = ttk.Entry(
            self.formulario,
            width=32
        )

        self.label_medico = ttk.Label(
            self.formulario,
            text="Médico responsable:",
            style="Form.TLabel"
        )

        self.entry_medico = ttk.Entry(
            self.formulario,
            width=32
        )

        self.label_nombre.grid(row=0, column=0, padx=15, pady=12, sticky="e")
        self.entry_nombre.grid(row=0, column=1, padx=15, pady=12)

        self.label_apellido.grid(row=1, column=0, padx=15, pady=12, sticky="e")
        self.entry_apellido.grid(row=1, column=1, padx=15, pady=12)

        self.label_genero.grid(row=2, column=0, padx=15, pady=12, sticky="e")
        self.combo_genero.grid(row=2, column=1, padx=15, pady=12)

        self.label_fecha.grid(row=3, column=0, padx=15, pady=12, sticky="e")
        self.entry_fecha.grid(row=3, column=1, padx=15, pady=12)

        self.label_medico.grid(row=4, column=0, padx=15, pady=12, sticky="e")
        self.entry_medico.grid(row=4, column=1, padx=15, pady=12)

        self.combo_genero.set("femenino")
        self.entry_fecha.insert(0, "1990-01-01")

    def crear_botones(self):
        self.frame_botones = ttk.Frame(
            self,
            style="App.TFrame"
        )

        self.frame_botones.pack(pady=20)

        self.boton_guardar = boton_exito(
            self.frame_botones,
            "Guardar paciente",
            self.guardar_paciente
        )

        self.boton_cancelar = boton_gris(
            self.frame_botones,
            "Cancelar",
            lambda: self.app.mostrar_vista("menu")
        )

        self.boton_guardar.grid(row=0, column=0, padx=10)
        self.boton_cancelar.grid(row=0, column=1, padx=10)

    def guardar_paciente(self):
        datos = {
            "nombre": self.entry_nombre.get().strip(),
            "apellido": self.entry_apellido.get().strip(),
            "género": self.combo_genero.get(),
            "fechaNacimiento": self.entry_fecha.get().strip(),
            "medico_cabecera": self.entry_medico.get().strip()
        }

        try:
            self.app.paciente_controller.crear_paciente(datos)

            messagebox.showinfo(
                "Paciente registrado",
                "El paciente ha sido dado de alta correctamente"
            )

            self.limpiar_formulario()
            self.app.mostrar_vista("lista_pacientes")

        except Exception as error:
            messagebox.showerror("Error", str(error))

    def limpiar_formulario(self):
        self.entry_nombre.delete(0, "end")
        self.entry_apellido.delete(0, "end")
        self.entry_fecha.delete(0, "end")
        self.entry_medico.delete(0, "end")

        self.combo_genero.set("femenino")
        self.entry_fecha.insert(0, "1990-01-01")