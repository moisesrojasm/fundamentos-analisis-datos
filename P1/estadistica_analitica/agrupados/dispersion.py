import math

try:
    from . import frecuencias
    from . import tendencias
    from . import tablas
except ImportError:
    import frecuencias
    import tendencias
    import tablas


def rango_limites(tabla):
    clases = tabla["clases"]
    return clases[-1]["ls"] - clases[0]["li"]


def rango_marcas(tabla):
    clases = tabla["clases"]
    return clases[-1]["xi"] - clases[0]["xi"]


def rango_intercuartilico(tabla):
    q = tendencias.cuartiles(tabla)
    return q["Q3"] - q["Q1"]


def rango_semi_intercuartilico(tabla):
    return rango_intercuartilico(tabla) / 2


def desviacion_media(tabla):
    media = tendencias.media_aritmetica(tabla)
    suma = 0.0
    for fila in tabla["clases"]:
        suma = suma + fila["fi"] * abs(fila["xi"] - media)
    return suma / tabla["n"]


def varianza(tabla):
    media = tendencias.media_aritmetica(tabla)
    suma = 0.0
    for fila in tabla["clases"]:
        suma = suma + fila["fi"] * ((fila["xi"] - media) ** 2)
    return suma / tabla["n"]


def desviacion_estandar(tabla):
    return math.sqrt(varianza(tabla))


def desviacion_estandar_abreviada(tabla):
    media = tendencias.media_aritmetica(tabla)
    suma = 0.0
    for fila in tabla["clases"]:
        suma = suma + fila["fi"] * (fila["xi"] ** 2)
    valor = (suma / tabla["n"]) - media ** 2
    if valor < 0:
        valor = 0.0
    return math.sqrt(valor)


def coeficiente_variacion(tabla):
    media = tendencias.media_aritmetica(tabla)
    if media == 0:
        return 0.0
    return (desviacion_estandar(tabla) / media) * 100


def puntaje_z(tabla, x):
    media = tendencias.media_aritmetica(tabla)
    sigma = desviacion_estandar(tabla)
    if sigma == 0:
        return 0.0
    return (x - media) / sigma


def z_marcas_clase(tabla):
    resultado = {}
    for fila in tabla["clases"]:
        etiqueta = f"z(xi={fila['xi']:.2f})"
        resultado[etiqueta] = puntaje_z(tabla, fila["xi"])
    return resultado


def chebyshev(k):
    if k <= 1:
        return 0.0
    return 1 - (1 / (k ** 2))


def intervalos_chebyshev(tabla, k=2):
    media = tendencias.media_aritmetica(tabla)
    sigma = desviacion_estandar(tabla)
    return {
        "k usado": k,
        "Limite inferior (mu - k*sigma)": media - k * sigma,
        "Limite superior (mu + k*sigma)": media + k * sigma,
        "Proporcion minima (Chebyshev)": chebyshev(k)
    }


def resumen(tabla):
    return {
        "Rango (limites reales)": rango_limites(tabla),
        "Rango (marcas de clase)": rango_marcas(tabla),
        "Rango intercuartilico (IQR)": rango_intercuartilico(tabla),
        "Rango semi-intercuartilico": rango_semi_intercuartilico(tabla),
        "Desviacion media": desviacion_media(tabla),
        "Varianza": varianza(tabla),
        "Desviacion estandar": desviacion_estandar(tabla),
        "Desviacion estandar (abreviado)": desviacion_estandar_abreviada(tabla),
        "Coeficiente de variacion (%)": coeficiente_variacion(tabla)
    }


if __name__ == "__main__":
    prueba = [12.4, 15.1, 18.9, 11.0, 14.2, 19.5, 13.3, 16.8, 17.2, 12.9,
              15.5, 18.1, 11.7, 14.9, 16.2]
    t = frecuencias.construir_tabla(prueba, "continuo")
    tablas.imprimir_resumen("MEDIDAS DE DISPERSION", resumen(t))
    print()
    tablas.imprimir_resumen("TEOREMA DE CHEBYSHEV", intervalos_chebyshev(t, 2))
