import math

try:
    from . import tablas
except ImportError:
    import tablas


def regla_sturges(n):
    """Numero de clases."""
    k = 1 + 3.322 * math.log10(n)
    return int(round(k))


def _redondear_arriba(valor, decimales):
    factor = 10 ** decimales
    return math.ceil(valor * factor) / factor


def construir_tabla(datos, tipo="continuo", num_clases=None, decimales=2):
    if len(datos) == 0:
        raise ValueError("La lista de datos esta vacia")

    datos = sorted(datos)
    n = len(datos)
    minimo = datos[0]
    maximo = datos[-1]
    rango = maximo - minimo

    if num_clases is None:
        k = regla_sturges(n)
    else:
        k = num_clases

    clases = []

    if tipo == "discreto":
        c = math.ceil((rango + 1) / k)
        k = math.ceil((rango + 1) / c)
        inicio = int(minimo)
        for j in range(k):
            li_ap = inicio + j * c
            ls_ap = li_ap + c - 1
            li_real = li_ap - 0.5
            ls_real = ls_ap + 0.5
            xi = (li_ap + ls_ap) / 2
            fi = 0
            for x in datos:
                if li_ap <= x <= ls_ap:
                    fi = fi + 1
            clases.append({
                "clase": j + 1,
                "li_ap": li_ap, "ls_ap": ls_ap,
                "li": li_real, "ls": ls_real,
                "xi": xi, "fi": fi
            })
    else:
        c = _redondear_arriba(rango / k, decimales)
        for j in range(k):
            li = minimo + j * c
            ls = li + c
            xi = (li + ls) / 2
            fi = 0
            for x in datos:
                if j == k - 1:
                    if li <= x <= ls:
                        fi = fi + 1
                else:
                    if li <= x < ls:
                        fi = fi + 1
            clases.append({
                "clase": j + 1,
                "li_ap": li, "ls_ap": ls,
                "li": li, "ls": ls,
                "xi": xi, "fi": fi
            })

    acumulada = 0
    relativa_acumulada = 0.0
    for fila in clases:
        acumulada = acumulada + fila["fi"]
        hi = fila["fi"] / n
        relativa_acumulada = relativa_acumulada + hi
        fila["Fi"] = acumulada
        fila["hi"] = hi
        fila["Hi"] = relativa_acumulada

    tabla = {
        "tipo": tipo,
        "datos": datos,
        "n": n,
        "minimo": minimo,
        "maximo": maximo,
        "rango": rango,
        "total_clases": k,
        "amplitud": c,
        "clases": clases
    }
    return tabla

def marcas_clase(tabla):
    return [fila["xi"] for fila in tabla["clases"]]


def frecuencias_absolutas(tabla):
    return [fila["fi"] for fila in tabla["clases"]]


def frecuencias_acumuladas(tabla):
    return [fila["Fi"] for fila in tabla["clases"]]


def clase_del_acumulado(tabla, posicion):
    clases = tabla["clases"]
    for i in range(len(clases)):
        if clases[i]["Fi"] >= posicion:
            return i
    return len(clases) - 1


def resumen(tabla):
    return {
        "Tipo de variable": tabla["tipo"],
        "Total de datos (N)": tabla["n"],
        "Valor minimo": float(tabla["minimo"]),
        "Valor maximo": float(tabla["maximo"]),
        "Rango de datos": float(tabla["rango"]),
        "Total de clases (K)": tabla["total_clases"],
        "Amplitud de clase (c)": float(tabla["amplitud"])
    }


def imprimir_distribucion(tabla):
    filas = []
    for fila in tabla["clases"]:
        if tabla["tipo"] == "discreto":
            intervalo = f"{fila['li_ap']} - {fila['ls_ap']}"
            reales = f"{fila['li']:.1f} - {fila['ls']:.1f}"
        else:
            intervalo = f"{fila['li_ap']:.2f} - {fila['ls_ap']:.2f}"
            reales = intervalo
        filas.append([
            fila["clase"], intervalo, reales,
            f"{fila['xi']:.3f}", fila["fi"], fila["Fi"],
            f"{fila['hi']:.4f}", f"{fila['Hi']:.4f}"
        ])

    tablas.imprimir_tabla(
        "TABLA DE DISTRIBUCION DE FRECUENCIAS",
        ["No.", "Intervalo", "Limites reales", "xi", "fi", "Fi", "hi", "Hi"],
        filas
    )


if __name__ == "__main__":
    prueba = [12.4, 15.1, 18.9, 11.0, 14.2, 19.5, 13.3, 16.8, 17.2, 12.9,
              15.5, 18.1, 11.7, 14.9, 16.2]
    t = construir_tabla(prueba, "continuo")
    imprimir_distribucion(t)
    print()
    tablas.imprimir_resumen("DATOS GENERALES", resumen(t))
