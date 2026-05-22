from views.menu import MenuPrincipal

from views.pacientes.lista_pacientes import ListaPacientes
from views.pacientes.crear_paciente import CrearPaciente
from views.pacientes.editar_paciente import EditarPaciente

from views.tensiones.lista_tensiones import ListaTensiones
from views.tensiones.crear_tension import CrearTension
from views.pacientes.detalle_paciente import DetallePaciente
from views.tensiones.editar_tension import EditarTension
from views.tensiones.detalle_tension import DetalleTension
from views.tensiones.estadisticas_tensiones import EstadisticasTensiones

class Router:

    @staticmethod
    def obtener_vistas():

        return {

            "menu": MenuPrincipal,

            "lista_pacientes": ListaPacientes,

            "estadisticas_tensiones": EstadisticasTensiones,

            "crear_paciente": CrearPaciente,

            "editar_paciente": EditarPaciente,

            "detalle_paciente": DetallePaciente,

            "lista_tensiones": ListaTensiones,

            "detalle_tension": DetalleTension,

            "crear_tension": CrearTension,

            "editar_tension": EditarTension

        }
    