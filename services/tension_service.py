class TensionService:

    def calcular_valor_en_rango(self, sistolica, diastolica):
        return 90 <= sistolica <= 140 and 60 <= diastolica <= 90

    def clasificar_tension(self, sistolica, diastolica):
        if sistolica < 90 or diastolica < 60:
            return "Hipotensión"

        if sistolica >= 180 or diastolica >= 120:
            return "Crisis hipertensiva"

        if sistolica >= 140 or diastolica >= 90:
            return "Hipertensión Etapa 2"

        if 130 <= sistolica <= 139 or 80 <= diastolica <= 89:
            return "Hipertensión Etapa 1"

        if 120 <= sistolica <= 129 and diastolica < 80:
            return "Elevada"

        return "Normal"