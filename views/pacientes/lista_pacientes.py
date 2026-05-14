from tkinter import ttk, messagebox

from views.components.botones import (
    boton_exito,
    boton_error,
    boton_gris
)

from views.components.tablas import crear_tabla


class ListaPacientes(ttk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, style="App.TFrame")

        self.app = app
        self.ids_pacientes = {}

        self.crear_titulo()
        self.crear_buscador()
        self.crear_tabla()
        self.crear_botones()

    def crear_titulo(self):
        self.label_titulo = ttk.Label(
            self,
            text="Gestión de Pacientes",
            style="Title.TLabel"
        )

        self.label_titulo.pack(pady=20)

    def crear_buscador(self):
        self.frame_buscador = ttk.Frame(
            self,
            style="App.TFrame"
        )

        self.frame_buscador.pack(fill="x", padx=40)

        self.label_buscar = ttk.Label(
            self.frame_buscador,
            text="Buscar paciente:"
        )

        self.entry_busqueda = ttk.Entry(
            self.frame_buscador,
            width=35
        )

        self.label_buscar.grid(row=0, column=0, padx=5, pady=5)
        self.entry_busqueda.grid(row=0, column=1, padx=5, pady=5)

        self.entry_busqueda.bind(
            "<KeyRelease>",
            lambda evento: self.cargar_datos()
        )

    def crear_tabla(self):
        columnas = (
            "Nombre",
            "Genero",
            "Fecha",
            "Medico"
        )

        encabezados = {
            "Nombre": "Nombre completo",
            "Genero": "Género",
            "Fecha": "Fecha nacimiento",
            "Medico": "Médico responsable"
        }

        anchos = {
            "Nombre": 300,
            "Genero": 150,
            "Fecha": 170,
            "Medico": 250
        }

        self.frame_tabla, self.tabla = crear_tabla(
            self,
            columnas,
            encabezados,
            anchos,
            alto=12
        )

        self.frame_tabla.pack(padx=40, pady=20)

    def crear_botones(self):
        self.frame_botones = ttk.Frame(
            self,
            style="App.TFrame"
        )

        self.frame_botones.pack(pady=15)

        self.boton_alta = boton_exito(
            self.frame_botones,
            "Dar de alta",
            lambda: self.app.mostrar_vista("crear_paciente")
        )

        self.boton_baja = boton_error(
            self.frame_botones,
            "Dar de baja",
            self.eliminar_paciente
        )

        self.boton_volver = boton_gris(
            self.frame_botones,
            "Volver",
            lambda: self.app.mostrar_vista("menu")
        )

        self.boton_alta.grid(row=0, column=0, padx=10)
        self.boton_baja.grid(row=0, column=1, padx=10)
        self.boton_volver.grid(row=0, column=2, padx=10)

    def actualizar_datos(self):
        self.cargar_datos()

    def cargar_datos(self):
        self.limpiar_tabla()

        texto_busqueda = self.entry_busqueda.get().lower()
        pacientes = self.app.paciente_controller.obtener_pacientes()

        for paciente in pacientes:
            nombre_completo = self.obtener_nombre_completo(paciente)

            if texto_busqueda not in nombre_completo.lower():
                continue

            genero = self.formatear_genero(
                paciente.get("género", paciente.get("genero", "No especificado"))
            )

            fecha = self.formatear_fecha(
                paciente.get("fechaNacimiento")
            )

            medico = paciente.get(
                "medico_cabecera",
                "Sin asignar"
            )

            item = self.tabla.insert(
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

    def limpiar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        self.ids_pacientes.clear()

    def obtener_nombre_completo(self, paciente):
        return (
            f"{paciente.get('nombre', '')} "
            f"{paciente.get('apellido', '')}"
        ).strip()

    def formatear_genero(self, genero):
        if not genero:
            return "No especificado"

        if genero.lower() == "femenino":
            return "Femenino"

        if genero.lower() == "masculino":
            return "Masculino"

        if genero.lower() == "otro":
            return "Otro"

        return genero.capitalize()

    def formatear_fecha(self, fecha):
        if not fecha:
            return ""

        return fecha.strftime("%d/%m/%Y")

    def eliminar_paciente(self):
        seleccionado = self.tabla.focus()

        if not seleccionado:
            messagebox.showwarning(
                "Aviso",
                "Seleccione un paciente"
            )
            return

        id_paciente = self.ids_pacientes[seleccionado]
        nombre = self.tabla.item(seleccionado)["values"][0]

        confirmar = messagebox.askyesno(
            "Confirmar baja",
            f"¿Desea dar de baja al paciente?\n\n{nombre}"
        )

        if confirmar:
            self.app.paciente_controller.eliminar_paciente(id_paciente)

            messagebox.showinfo(
                "Paciente eliminado",
                "El paciente ha sido dado de baja correctamente"
            )

            self.cargar_datos()