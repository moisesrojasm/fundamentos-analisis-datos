import math

try:
    from . import frecuencias
    from . import tablas
except ImportError:
    import frecuencias
    import tablas


def media_aritmetica(tabla):
    suma = 0.0
    for fila in tabla["clases"]:
        suma = suma + fila["fi"] * fila["xi"]
    return suma / tabla["n"]


def media_geometrica(tabla):
    suma = 0.0
    for fila in tabla["clases"]:
        if fila["fi"] > 0 and fila["xi"] > 0:
            suma = suma + fila["fi"] * math.log10(fila["xi"])
    return 10 ** (suma / tabla["n"])


def media_armonica(tabla):
    suma = 0.0
    for fila in tabla["clases"]:
        if fila["xi"] != 0:
            suma = suma + fila["fi"] / fila["xi"]
    return tabla["n"] / suma


def raiz_cuadratica_media(tabla):
    suma = 0.0
    for fila in tabla["clases"]:
        suma = suma + fila["fi"] * (fila["xi"] ** 2)
    return math.sqrt(suma / tabla["n"])


def mediana(tabla):
    n = tabla["n"]
    clases = tabla["clases"]
    c = tabla["amplitud"]

    posicion = n / 2
    i = frecuencias.clase_del_acumulado(tabla, posicion)

    if i == 0:
        f_anterior = 0
    else:
        f_anterior = clases[i - 1]["Fi"]

    li = clases[i]["li"]
    f_med = clases[i]["fi"]
    if f_med == 0:
        return li
    return li + ((posicion - f_anterior) / f_med) * c


def moda(tabla):
    clases = tabla["clases"]
    c = tabla["amplitud"]

    i = 0
    for j in range(len(clases)):
        if clases[j]["fi"] > clases[i]["fi"]:
            i = j

    f_modal = clases[i]["fi"]
    if i == 0:
        f_anterior = 0
    else:
        f_anterior = clases[i - 1]["fi"]
    if i == len(clases) - 1:
        f_posterior = 0
    else:
        f_posterior = clases[i + 1]["fi"]

    d1 = f_modal - f_anterior
    d2 = f_modal - f_posterior

    if (d1 + d2) == 0:
        return clases[i]["xi"]
    return clases[i]["li"] + (d1 / (d1 + d2)) * c


def cuantil(tabla, k, q):
    n = tabla["n"]
    clases = tabla["clases"]
    c = tabla["amplitud"]

    posicion = (k * n) / q
    i = frecuencias.clase_del_acumulado(tabla, posicion)

    if i == 0:
        f_anterior = 0
    else:
        f_anterior = clases[i - 1]["Fi"]

    li = clases[i]["li"]
    f = clases[i]["fi"]
    if f == 0:
        return li
    return li + ((posicion - f_anterior) / f) * c


def cuartiles(tabla):
    return {"Q1": cuantil(tabla, 1, 4),
            "Q2": cuantil(tabla, 2, 4),
            "Q3": cuantil(tabla, 3, 4)}


def deciles(tabla):
    resultado = {}
    for k in range(1, 10):
        resultado["D" + str(k)] = cuantil(tabla, k, 10)
    return resultado


def percentiles(tabla, lista=None):
    if lista is None:
        lista = [10, 25, 50, 75, 90]
    resultado = {}
    for k in lista:
        resultado["P" + str(k)] = cuantil(tabla, k, 100)
    return resultado


def resumen(tabla):
    return {
        "Media aritmetica": media_aritmetica(tabla),
        "Media geometrica": media_geometrica(tabla),
        "Media armonica": media_armonica(tabla),
        "Raiz cuadratica media (RCM)": raiz_cuadratica_media(tabla),
        "Mediana": mediana(tabla),
        "Moda": moda(tabla)
    }


def resumen_cuantiles(tabla):
    datos = {}
    datos.update(cuartiles(tabla))
    datos.update(deciles(tabla))
    datos.update(percentiles(tabla))
    return datos


if __name__ == "__main__":
    prueba = [12.4, 15.1, 18.9, 11.0, 14.2, 19.5, 13.3, 16.8, 17.2, 12.9,
              15.5, 18.1, 11.7, 14.9, 16.2]
    t = frecuencias.construir_tabla(prueba, "continuo")
    tablas.imprimir_resumen("MEDIDAS DE TENDENCIA CENTRAL", resumen(t))
    print()
    tablas.imprimir_resumen("CUANTILES", resumen_cuantiles(t))
