from pydantic import BaseModel, field_validator


class TensionSchema(BaseModel):
    id_paciente: str
    sistolica: int
    diastolica: int
    valoracion: str

    @field_validator("id_paciente")
    @classmethod
    def validar_id_paciente(cls, value):
        if not value or not value.strip():
            raise ValueError("Debe seleccionarse un paciente")
        return value

    @field_validator("sistolica")
    @classmethod
    def validar_sistolica(cls, value):
        if value < 50 or value > 250:
            raise ValueError("La tensión sistólica debe estar entre 50 y 250")
        return value

    @field_validator("diastolica")
    @classmethod
    def validar_diastolica(cls, value):
        if value < 30 or value > 150:
            raise ValueError("La tensión diastólica debe estar entre 30 y 150")
        return value

    @field_validator("valoracion")
    @classmethod
    def validar_valoracion(cls, value):
        if not value or not value.strip():
            raise ValueError("La valoración no puede estar vacía")
        return value