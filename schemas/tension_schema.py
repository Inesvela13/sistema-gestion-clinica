from pydantic import BaseModel, field_validator


class TensionSchema(BaseModel):
    id_paciente: str
    sistólica: int
    diastólica: int
    valoración: str

    @field_validator("id_paciente")
    @classmethod
    def validar_id_paciente(cls, value):
        if not value or not value.strip():
            raise ValueError("Debes seleccionar un paciente")
        return value

    @field_validator("sistólica")
    @classmethod
    def validar_sistolica(cls, value):
        if value < 50 or value > 250:
            raise ValueError("La sistólica debe estar entre 50 y 250")
        return value

    @field_validator("diastólica")
    @classmethod
    def validar_diastolica(cls, value):
        if value < 30 or value > 150:
            raise ValueError("La diastólica debe estar entre 30 y 150")
        return value

    @field_validator("valoración")
    @classmethod
    def validar_valoracion(cls, value):
        if not value.strip():
            raise ValueError("La valoración no puede estar vacía")
        return value