from tkinter import ttk, messagebox

from views.components.botones import (
    boton_tension,
    boton_error,
    boton_gris,
    boton_primario,
    boton_secundario
)

from views.components.tablas import crear_tabla


class ListaTensiones(ttk.Frame):

    def __init__(self, parent, app):
        super().__init__(parent, style="App.TFrame")

        self.app = app
        self.ids_tensiones = {}

        self.crear_titulo()
        self.crear_tabla()
        self.crear_botones()

    def crear_titulo(self):

        self.label_titulo = ttk.Label(
            self,
            text="Registro de Tensiones",
            style="TensionTitle.TLabel"
        )

        self.label_titulo.pack(
            pady=25
        )

    def crear_tabla(self):

        columnas = (
            "Paciente",
            "Sistolica",
            "Diastolica",
            "Valoracion",
            "Estado",
            "Rango"
        )

        encabezados = {

            "Paciente": "Paciente",

            "Sistolica": "Sistólica",

            "Diastolica": "Diastólica",

            "Valoracion": "Valoración",

            "Estado": "Estado",

            "Rango": "En rango"
        }

        anchos = {

            "Paciente": 260,

            "Sistolica": 120,

            "Diastolica": 120,

            "Valoracion": 260,

            "Estado": 120,

            "Rango": 120
        }

        self.frame_tabla, self.tabla = crear_tabla(
            self,
            columnas,
            encabezados,
            anchos,
            alto=13
        )

        self.frame_tabla.pack(
            padx=40,
            pady=20
        )

    def crear_botones(self):

        self.frame_botones = ttk.Frame(
            self,
            style="App.TFrame"
        )

        self.frame_botones.pack(
            pady=15
        )

        self.boton_registrar = boton_tension(
            self.frame_botones,
            "Registrar tensión",
            lambda: self.app.mostrar_vista(
                "crear_tension"
            )
        )

        self.boton_detalle = boton_secundario(
            self.frame_botones,
            "Ver detalle",
            self.ver_detalle
        )

        self.boton_editar = boton_primario(
            self.frame_botones,
            "Editar tensión",
            self.editar_tension
        )

        self.boton_estadisticas = boton_secundario(
            self.frame_botones,
            "Estadísticas",
            self.ver_estadisticas
        )

        self.boton_baja = boton_error(
            self.frame_botones,
            "Dar de baja",
            self.eliminar_tension
        )

        self.boton_volver = boton_gris(
            self.frame_botones,
            "Volver",
            lambda: self.app.mostrar_vista(
                "menu"
            )
        )

        self.boton_registrar.grid(
            row=0,
            column=0,
            padx=10
        )

        self.boton_detalle.grid(
            row=0,
            column=1,
            padx=10
        )

        self.boton_editar.grid(
            row=0,
            column=2,
            padx=10
        )

        self.boton_estadisticas.grid(
            row=0,
            column=3,
            padx=10
        )

        self.boton_baja.grid(
            row=0,
            column=4,
            padx=10
        )

        self.boton_volver.grid(
            row=0,
            column=5,
            padx=10
        )

    def actualizar_datos(self):

        self.cargar_datos()

    def cargar_datos(self):

        self.limpiar_tabla()

        pacientes = (
            self.app.tension_controller
            .obtener_pacientes()
        )

        tensiones = (
            self.app.tension_controller
            .obtener_tensiones()
        )

        mapa_pacientes = {

            paciente.get("_id"): (

                f"{paciente.get('nombre', '')} "
                f"{paciente.get('apellido', '')}"

            ).strip()

            for paciente in pacientes
        }

        for tension in tensiones:

            id_paciente = tension.get(
                "id_paciente"
            )

            nombre_paciente = mapa_pacientes.get(
                id_paciente,
                "Paciente no encontrado"
            )

            valores = tension.get(
                "valores",
                {}
            )

            sistolica = valores.get(
                "sistolica",
                "-"
            )

            diastolica = valores.get(
                "diastolica",
                "-"
            )

            valoracion = tension.get(
                "valoracion",
                "-"
            )

            estado = tension.get(
                "estado",
                "-"
            )

            valor_en_rango = tension.get(
                "valor_en_rango",
                "-"
            )

            if valor_en_rango is True:

                texto_rango = "Sí"

            elif valor_en_rango is False:

                texto_rango = "No"

            else:

                texto_rango = "-"

            item = self.tabla.insert(
                "",
                "end",
                values=(

                    nombre_paciente,

                    sistolica,

                    diastolica,

                    valoracion,

                    estado,

                    texto_rango
                )
            )

            self.ids_tensiones[item] = (
                tension.get("_id")
            )

    def limpiar_tabla(self):

        for item in self.tabla.get_children():

            self.tabla.delete(item)

        self.ids_tensiones.clear()

    def ver_detalle(self):

        seleccionado = self.tabla.focus()

        if not seleccionado:

            messagebox.showwarning(
                "Aviso",
                "Seleccione un registro"
            )

            return

        id_tension = self.ids_tensiones[
            seleccionado
        ]

        tension = (
            self.app.tension_controller
            .tension_repository
            .obtener_por_id(id_tension)
        )

        pacientes = (
            self.app.tension_controller
            .obtener_pacientes()
        )

        nombre_paciente = "Paciente"

        for paciente in pacientes:

            if paciente.get("_id") == tension.get(
                "id_paciente"
            ):

                nombre_paciente = (
                    f"{paciente.get('nombre', '')} "
                    f"{paciente.get('apellido', '')}"
                ).strip()

                break

        vista_detalle = self.app.frames[
            "detalle_tension"
        ]

        vista_detalle.cargar_tension(
            tension,
            nombre_paciente
        )

        self.app.mostrar_vista(
            "detalle_tension"
        )

    def editar_tension(self):

        seleccionado = self.tabla.focus()

        if not seleccionado:

            messagebox.showwarning(
                "Aviso",
                "Seleccione un registro"
            )

            return

        id_tension = self.ids_tensiones[
            seleccionado
        ]

        tension = (

            self.app.tension_controller
            .tension_repository
            .obtener_por_id(id_tension)

        )

        vista_editar = self.app.frames[
            "editar_tension"
        ]

        vista_editar.cargar_tension(
            tension
        )

        self.app.mostrar_vista(
            "editar_tension"
        )

    def ver_estadisticas(self):

        vista_estadisticas = self.app.frames[
            "estadisticas_tensiones"
        ]

        vista_estadisticas.cargar_estadisticas()

        self.app.mostrar_vista(
            "estadisticas_tensiones"
        )

    def eliminar_tension(self):

        seleccionado = self.tabla.focus()

        if not seleccionado:

            messagebox.showwarning(
                "Aviso",
                "Seleccione un registro"
            )

            return

        id_tension = self.ids_tensiones[
            seleccionado
        ]

        paciente = self.tabla.item(
            seleccionado
        )["values"][0]

        confirmar = messagebox.askyesno(
            "Confirmar baja",
            f"¿Desea eliminar el registro de tensión de:\n\n{paciente}?"
        )

        if confirmar:

            self.app.tension_controller.eliminar_tension(
                id_tension
            )

            messagebox.showinfo(
                "Registro eliminado",
                "La tensión arterial ha sido eliminada correctamente"
            )

            self.cargar_datos()