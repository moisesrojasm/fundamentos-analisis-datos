# Frecuencia absoluta (fi), acumulada (Fi), relativa (hi), y relativa acumulada

import math

def datos_tabla_frecuencias(datos):
    N = len(datos)

    total_clases = round(1 + 3.322 * math.log10(N))

    rango = max(datos) - min(datos)

    amplitud = rango / total_clases

    limites_inf = []
    limites_sup = []
    marcas_clase = []

    frec_absolutas = []

    lim_actual = min(datos)
    for i in range(total_clases):
        limites_inf.append(lim_actual)
        limite_sig = lim_actual + amplitud
        limites_sup.append(limite_sig)

        abs = 0
        for dato in datos:
            if i == total_clases - 1:   # -1 porque i empieza desde 0 
                if lim_actual <= dato <= limite_sig:
                    abs += 1
            else:
                if lim_actual <= dato < limite_sig:
                    abs += 1

        frec_absolutas.append(abs)

        marca = (lim_actual + limite_sig) / 2
        marcas_clase.append(marca)

        lim_actual = limite_sig


    frec_acumulada = []
    frec_relativa = []
    frec_relativa_acum = []
    acumulada = relativa_acum = 0

    for frecuencia in frec_absolutas:
        acumulada += frecuencia
        frec_acumulada.append(acumulada)    # Fi

        relativa = frecuencia / N
        frec_relativa.append(relativa)  # hi

        relativa_acum += relativa
        frec_relativa_acum.append(relativa_acum) 

    return {
        "N" : N,
        "Total Clases": total_clases,
        "Rango" : rango,
        "Amplitud" : amplitud,
        "Limites Inf": limites_inf,
        "Limites Sup" : limites_sup,
        "Marcas Clase xi": marcas_clase,
        "Frecuencias Abs fi" : frec_absolutas,
        "Frecuencias Acum Fi" : frec_acumulada,
        "Frecuencias Rel hi" : frec_relativa,
        "Frecuencias Rel Acum" : frec_relativa_acum
    }