import random
from estadistica_analitica_lib import frecuencias, tendencias, dispersion, forma

def mostrar_tabla_resultados(resumen: dict) -> None:
    print("+" + "-"*34 + "+" + "-"*24 + "+")
    print(f"| {'Métrica':<32} | {'Resultado':<22} |")
    print("+" + "-"*34 + "+" + "-"*24 + "+")
    
    for llave, valor in resumen.items():
        if type(valor) == float:
            print(f"| {llave:<32} | {valor:<22.4f} |")
            
        elif type(valor) == list:
            texto = str(valor)
            if len(texto) > 22:
                texto = texto[:19] + "..."
            print(f"| {llave:<32} | {texto:<22} |")
            
        else:
            print(f"| {llave:<32} | {str(valor):<22} |")
            
    print("+" + "-"*34 + "+" + "-"*24 + "+")

if __name__ == "__main__":
    print("- Sistema de Análisis Estadístico -")
    
    datos_flotantes = []
    datos_enteros = []
    
    for _ in range(100):
        datos_flotantes.append(random.uniform(10.0, 100.0))
        datos_enteros.append(random.randint(10, 100))
        
    print("Se han generado 100 datos continuos y 100 datos discretos\n")
    
    while True:
        opcion = input("Elige el tipo de datos (1 = Continuos, 2 = Discretos): ")
        
        if opcion == "1":
            datos_elegidos = datos_flotantes
            break
        elif opcion == "2":
            datos_elegidos = datos_enteros
            break
        else:
            print("Ingresa una opción válida")

    # Modulo Frecuencias
    dict_frec = frecuencias.datos_tabla_frecuencias(datos_elegidos)
    
    # Modulo Tendencias
    dict_tend = {}
    dict_tend["Media Aritmetica"] = tendencias.media_aritmetica(dict_frec)
    dict_tend["Media Geometrica"] = tendencias.media_geometrica(dict_frec)
    dict_tend["Media Armonica"] = tendencias.media_armonica(dict_frec)
    dict_tend["Mediana"] = tendencias.mediana(dict_frec)
    dict_tend["Moda"] = tendencias.moda(dict_frec)
    dict_tend["RCM"] = tendencias.rcm(dict_frec)
    dict_tend.update(tendencias.conjunto_cuantiles(dict_frec))
    
    # Modulo Dispersión
    dict_disp = {}
    dict_disp["Rango"] = dispersion.rango(dict_frec)
    dict_disp["Rango Semi-Intercuartilico"] = dispersion.rango_si(dict_tend)
    dict_disp["Desviacion Media"] = dispersion.desv_media(dict_frec, dict_tend)
    dict_disp["Varianza"] = dispersion.varianza(dict_frec, dict_tend)
    dict_disp["Desviacion Estandar"] = dispersion.desv_estandar(dict_frec, dict_tend)
    dict_disp["Chebyshev (k=2)"] = dispersion.teorema_chebyshev(2)
    dict_disp["Coeficiente Variacion (%)"] = dispersion.coeficiente_variacion(dict_frec, dict_tend)
    
    # Marca de clase para el Z-score
    primer_marca = dict_frec["Marcas Clase xi"][0]
    dict_disp["Z-Score (Clase 1)"] = dispersion.z_score(primer_marca, dict_frec, dict_tend)

    # Modulo Forma
    dict_forma = {}
    dict_forma["Fisher-Pearson"] = forma.coef_fp_momentos(dict_frec, dict_tend)
    dict_forma["Asimetria Pearson 1"] = forma.coef_asim_p1(dict_tend, dict_disp)
    dict_forma["Asimetria Pearson 2"] = forma.coef_asim_p2(dict_tend, dict_disp)
    dict_forma["Sesgo Cuantiles"] = forma.coef_sesgo_cuantiles(dict_tend)
    dict_forma["Exceso Curtosis"] = forma.exceso_curtosis(dict_frec, dict_tend)
    dict_forma["Curtosis Percentilica"] = forma.curtosis_percentilica(dict_tend)
    
    resultados_totales = {}
    resultados_totales["Total Datos (N)"] = dict_frec["N"]
    resultados_totales["Total Clases"] = dict_frec["Total Clases"]
    resultados_totales["Amplitud"] = dict_frec["Amplitud"]
    
    resultados_totales.update(dict_tend)
    resultados_totales.update(dict_disp)
    resultados_totales.update(dict_forma)
    
    print("\n- Resultados -")
    mostrar_tabla_resultados(resultados_totales)