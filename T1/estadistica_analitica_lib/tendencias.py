# Promedio: aritmético, geométrico, armónico
# Mediana, moda y RCM
# Cuantiles: cuartiles, deciles y percentiles

import math

def media_aritmetica(datos_frecuencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    N = datos_frecuencias["N"]

    suma = 0
    for i in range(len(fi)):
        suma += (fi[i] * xi[i])

    return suma / N

def media_geometrica(datos_frecuencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    N = datos_frecuencias["N"]

    suma = 0
    for i in range(len(fi)):    
        suma += (fi[i] * math.log10(xi[i]))

    return 10 ** (suma / N)

def media_armonica(datos_frecuencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    N = datos_frecuencias["N"]

    suma = 0
    for i in range(len(fi)):
        suma += (fi[i] / xi[i])

    return N / suma

def mediana(datos_frecuencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    Fi = datos_frecuencias["Frecuencias Acum Fi"]
    Li = datos_frecuencias["Limites Inf"]
    N = datos_frecuencias["N"]
    amplitud = datos_frecuencias["Amplitud"]

    for i in range(len(Fi)):
        if Fi[i] >= (N/2):
            ind_mediana = i
            if ind_mediana == 0:
                frec_acum_ant = 0
            else:
                frec_acum_ant = Fi[ind_mediana - 1]
            break

    lim_inf = Li[ind_mediana]
    frec_abs = fi[ind_mediana]

    mediana = lim_inf + ((N/2 - frec_acum_ant) / frec_abs) * amplitud

    return mediana

def moda(datos_frecuencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    Li = datos_frecuencias["Limites Inf"]
    amplitud = datos_frecuencias["Amplitud"]

    ind_moda = fi.index(max(fi))

    if ind_moda == 0:
        fi_ant = 0
    else:
        fi_ant = fi[ind_moda - 1]

    if ind_moda == len(fi) - 1:
        fi_pos = 0
    else:
        fi_pos = fi[ind_moda + 1]

    delta1 = fi[ind_moda] - fi_ant
    delta2 = fi[ind_moda] - fi_pos

    moda = Li[ind_moda] + (delta1 / (delta1 + delta2)) * amplitud

    return moda

def rcm(datos_frecuencias):
    fi = datos_frecuencias["Frecuencias Abs fi"]
    xi = datos_frecuencias["Marcas Clase xi"]
    N = datos_frecuencias["N"]

    suma = 0
    for i in range(len(fi)):
        suma += (fi[i] * xi[i] ** 2)

    return math.sqrt(suma / N)

def cuantil(datos_frecuencias, k, q):
    # k orden del cuantil
    # q num particiones
    N = datos_frecuencias["N"]
    Fi = datos_frecuencias["Frecuencias Acum Fi"]
    fi = datos_frecuencias["Frecuencias Abs fi"]
    Li = datos_frecuencias["Limites Inf"]
    amplitud = datos_frecuencias["Amplitud"]
    
    posicion = (k * N) / q
    
    clase_cuantil = 0
    for i in range(len(Fi)):
        if Fi[i] >= posicion:
            clase_cuantil = i
            break
            
    Li = Li[clase_cuantil]
    f = fi[clase_cuantil]
    
    if clase_cuantil == 0:
        Fi_ant = 0
    else:
        Fi_ant = Fi[clase_cuantil - 1]
        
    return Li + (((posicion - Fi_ant) / f) * amplitud)

def conjunto_cuantiles(datos_frecuencias):
    resultados = {}
    
    # k = 1,2,3
    for k in range(1, 4):
        resultados[f"Cuartil {k}"] = cuantil(datos_frecuencias, k, 4)
        
    # k = 1 a 9)
    for k in range(1, 10):
        resultados[f"Decil {k}"] = cuantil(datos_frecuencias, k, 10)
        
    # k = 1 a 99
    percentiles_elegidos = [10, 25, 50, 75, 90, 99]
    for k in percentiles_elegidos:
         resultados[f"Percentil {k}"] = cuantil(datos_frecuencias, k, 100)
         
    return resultados