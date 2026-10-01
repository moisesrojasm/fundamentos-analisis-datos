# Rango, rango semi-intercuartílico, desviación media, 
# varianza, desviación estándar,
# teorema de Chebyshev, z-score, coeficiente de variación

def rango(datos_frecuencias):
    Li = datos_frecuencias["Limites Inf"]
    Ls = datos_frecuencias["Limites Sup"]

    return Ls[-1] - Li[0]

def rango_si(datos_tendencias):
    cuartil3 = datos_tendencias["Cuartil 3"]
    cuartil1 = datos_tendencias["Cuartil 1"]

    return (cuartil3 - cuartil1) / 2

def desv_media(datos_frecuencias, datos_tendencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    N = datos_frecuencias["N"]
    media = datos_tendencias["Media Aritmetica"]

    suma = 0
    for i in range(len(fi)):
        suma += fi[i] * abs(xi[i] - media)

    return suma / N

def varianza(datos_frecuencias, datos_tendencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    N = datos_frecuencias["N"]
    media = datos_tendencias["Media Aritmetica"]

    suma = 0
    for i in range(len(fi)):
        suma += fi[i] * ((xi[i] - media) ** 2)

    return suma / N

def desv_estandar(datos_frecuencias, datos_tendencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    N = datos_frecuencias["N"]
    media = datos_tendencias["Media Aritmetica"]

    suma = 0
    for i in range(len(fi)):
        suma += fi[i] * ((xi[i] - media) ** 2)

    return (suma / N) ** (1/2)

def teorema_chebyshev(k):
    if k <= 1:
        return None 
    
    return 1 - (1 / (k ** 2))

def z_score(x, datos_frecuencias, datos_tendencias):
    media = datos_tendencias["Media Aritmetica"]
    sigma = desv_estandar(datos_frecuencias, datos_tendencias)
    
    return (x - media) / sigma

def coeficiente_variacion(datos_frecuencias, datos_tendencias):
    media = datos_tendencias["Media Aritmetica"]
    sigma = desv_estandar(datos_frecuencias, datos_tendencias)
    
    return (sigma / media) * 100