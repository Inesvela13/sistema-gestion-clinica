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
    
    def calcular_media_tensiones(
        self,
        tensiones
    ):

        sistolicas = []
        diastolicas = []

        for tension in tensiones:

            valores = tension.get(
                "valores",
                {}
            )

            sistolica = valores.get(
                "sistolica"
            )

            diastolica = valores.get(
                "diastolica"
            )

            if sistolica:

                sistolicas.append(
                    sistolica
                )

            if diastolica:

                diastolicas.append(
                    diastolica
                )

        media_sistolica = 0
        media_diastolica = 0

        if sistolicas:

            media_sistolica = round(
                sum(sistolicas) /
                len(sistolicas),
                1
            )

        if diastolicas:

            media_diastolica = round(
                sum(diastolicas) /
                len(diastolicas),
                1
            )

        return {

            "media_sistolica":
                media_sistolica,

            "media_diastolica":
                media_diastolica
        }

    def obtener_ultima_tension(
        self,
        tensiones
    ):

        if not tensiones:
            return None

        tensiones_ordenadas = sorted(

            tensiones,

            key=lambda tension:
                tension.get("fecha"),

            reverse=True
        )

        return tensiones_ordenadas[0]