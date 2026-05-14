from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import Optional


class PacienteSchema(BaseModel):
    nombre: str
    apellido: str
    género: str
    fechaNacimiento: str
    medico_cabecera: Optional[str] = ""

    @field_validator("nombre", "apellido")
    @classmethod
    def validar_texto_no_vacio(cls, value):
        if not value or not value.strip():
            raise ValueError("El campo no puede estar vacío")
        return value.strip()

    @field_validator("género")
    @classmethod
    def validar_genero(cls, value):
        opciones_validas = ["femenino", "masculino", "otro"]

        if value not in opciones_validas:
            raise ValueError("El género debe ser femenino, masculino u otro")

        return value

    @field_validator("fechaNacimiento")
    @classmethod
    def validar_fecha(cls, value):
        try:
            fecha = datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValueError("La fecha debe tener formato YYYY-MM-DD")

        hoy = datetime.now()

        if fecha > hoy:
            raise ValueError("La fecha de nacimiento no puede ser futura")

        edad_maxima = 120

        if hoy.year - fecha.year > edad_maxima:
            raise ValueError("La fecha de nacimiento no es válida")

        return value