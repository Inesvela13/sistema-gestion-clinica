from tkinter import ttk, messagebox

from views.components.botones import (
    boton_primario,
    boton_gris
)


class EditarPaciente(ttk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, style="App.TFrame")

        self.app = app
        self.id_paciente = None

        self.crear_titulo()
        self.crear_formulario()
        self.crear_botones()

    def crear_titulo(self):
        self.label_titulo = ttk.Label(
            self,
            text="Editar Paciente",
            style="Title.TLabel"
        )

        self.label_titulo.pack(pady=25)

    def crear_formulario(self):

        self.frame_formulario = ttk.Frame(
            self,
            style="Card.TFrame",
            padding=30
        )

        self.frame_formulario.pack(pady=10)

        # NOMBRE

        self.label_nombre = ttk.Label(
            self.frame_formulario,
            text="Nombre:",
            style="Form.TLabel"
        )

        self.entry_nombre = ttk.Entry(
            self.frame_formulario,
            width=35
        )

        # APELLIDO

        self.label_apellido = ttk.Label(
            self.frame_formulario,
            text="Apellido:",
            style="Form.TLabel"
        )

        self.entry_apellido = ttk.Entry(
            self.frame_formulario,
            width=35
        )

        # GENERO

        self.label_genero = ttk.Label(
            self.frame_formulario,
            text="Género:",
            style="Form.TLabel"
        )

        self.combo_genero = ttk.Combobox(
            self.frame_formulario,
            values=[
                "male",
                "female",
                "other",
                "unknown"
            ],
            state="readonly",
            width=32
        )

        # FECHA

        self.label_fecha = ttk.Label(
            self.frame_formulario,
            text="Fecha nacimiento:",
            style="Form.TLabel"
        )

        self.entry_fecha = ttk.Entry(
            self.frame_formulario,
            width=35
        )

        # GRID

        self.label_nombre.grid(row=0, column=0, padx=15, pady=12, sticky="e")
        self.entry_nombre.grid(row=0, column=1, padx=15, pady=12)

        self.label_apellido.grid(row=1, column=0, padx=15, pady=12, sticky="e")
        self.entry_apellido.grid(row=1, column=1, padx=15, pady=12)

        self.label_genero.grid(row=2, column=0, padx=15, pady=12, sticky="e")
        self.combo_genero.grid(row=2, column=1, padx=15, pady=12)

        self.label_fecha.grid(row=3, column=0, padx=15, pady=12, sticky="e")
        self.entry_fecha.grid(row=3, column=1, padx=15, pady=12)

    def crear_botones(self):

        self.frame_botones = ttk.Frame(
            self,
            style="App.TFrame"
        )

        self.frame_botones.pack(pady=20)

        self.boton_guardar = boton_primario(
            self.frame_botones,
            "Guardar cambios",
            self.guardar_cambios
        )

        self.boton_cancelar = boton_gris(
            self.frame_botones,
            "Cancelar",
            lambda: self.app.mostrar_vista("lista_pacientes")
        )

        self.boton_guardar.grid(row=0, column=0, padx=10)
        self.boton_cancelar.grid(row=0, column=1, padx=10)

    def cargar_paciente(self, paciente):

        self.id_paciente = paciente.get("_id")

        self.entry_nombre.delete(0, "end")
        self.entry_apellido.delete(0, "end")
        self.entry_fecha.delete(0, "end")

        self.entry_nombre.insert(
            0,
            paciente.get("nombre", "")
        )

        self.entry_apellido.insert(
            0,
            paciente.get("apellido", "")
        )

        self.combo_genero.set(
            paciente.get("género", "unknown")
        )

        fecha = paciente.get("fechaNacimiento")

        if fecha:
            self.entry_fecha.insert(
                0,
                fecha.strftime("%Y-%m-%d")
            )

    def guardar_cambios(self):

        datos = {
            "nombre": self.entry_nombre.get().strip(),
            "apellido": self.entry_apellido.get().strip(),
            "género": self.combo_genero.get(),
            "fechaNacimiento": self.entry_fecha.get().strip()
        }

        try:

            self.app.paciente_controller.actualizar_paciente(
                self.id_paciente,
                datos
            )

            messagebox.showinfo(
                "Paciente actualizado",
                "Los datos del paciente se actualizaron correctamente"
            )

            self.app.mostrar_vista(
                "lista_pacientes"
            )

        except Exception as error:

            messagebox.showerror(
                "Error",
                str(error)
            )