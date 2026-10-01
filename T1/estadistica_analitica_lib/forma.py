# Momento central, 
# coeficiente Fisher-Pearson momentos
# coeficiente asimetría Pearson 1
# coeficiente asimetría Pearson 2
# coeficiente de sesgo cuantiles
# exceso curtosis 
# curtosis percentílica 

import math

def momento_central(r, datos_frecuencias, datos_tendencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    media = datos_tendencias["Media Aritmetica"]
    N = datos_frecuencias["N"]

    suma = 0
    for i in range(len(fi)):
        suma += fi[i] * ((xi[i] - media) ** r)

    return suma / N

def coef_fp_momentos(datos_frecuencias, datos_tendencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    media = datos_tendencias["Media Aritmetica"]
    N = datos_frecuencias["N"]

    suma1 = suma2 = 0
    for i in range(len(fi)):
        suma1 += (fi[i] * (xi[i] - media) ** 3) / N
        suma2 += (fi[i] * (xi[i] - media) ** 2) / N

    return suma1 / suma2 ** (3/2)

def coef_asim_p1(datos_tendencias, datos_dispersion):
    media = datos_tendencias["Media Aritmetica"]
    moda = datos_tendencias["Moda"]
    sigma = datos_dispersion["Desviacion Estandar"]

    return (media - moda) / sigma

def coef_asim_p2(datos_tendencias, datos_dispersion):
    media = datos_tendencias["Media Aritmetica"]
    mediana = datos_tendencias["Mediana"]
    sigma = datos_dispersion["Desviacion Estandar"]
    
    return (3 * (media - mediana)) / sigma

def coef_sesgo_cuantiles(datos_tendencias):
    q1 = datos_tendencias["Cuartil 1"]
    q2 = datos_tendencias["Cuartil 2"]
    q3 = datos_tendencias["Cuartil 3"]
    
    return (q3 + q1 - 2 * q2) / (q3 - q1)

def exceso_curtosis(datos_frecuencias, datos_tendencias):
    m4 = momento_central(4, datos_frecuencias, datos_tendencias)
    m2 = momento_central(2, datos_frecuencias, datos_tendencias)
    
    return (m4 / (m2 ** 2)) - 3

def curtosis_percentilica(datos_tendencias):
    p90 = datos_tendencias["Percentil 90"]
    p75 = datos_tendencias["Percentil 75"]
    p25 = datos_tendencias["Percentil 25"]
    p10 = datos_tendencias["Percentil 10"]
    
    return (p90 - p10) / (p75 - p25)