import numpy as np
import pandas as pd
from unidecode import unidecode

# -----------------------------------------------------------------------------
# Función: Comprueba si la palabra pasada por parámetro contiene algún tipo
#          de acento.
#
# Parámetros:
#               - word : Palabra a comprobar si tiene acento
# -----------------------------------------------------------------------------
def contains_accent(word):
    tildes = 'áéíóúàèìòùäëïöüâêîôû'
    for letra in word: #Recorremos la palabra
        if letra in tildes: #Comprobamos si la letra es alguna de las tildes
            return 1
    return 0

 # -----------------------------------------------------------------------------
 # Función: Comprueba si la palabra pasada por parámetro contiene el termino
 #          pasado por parametro.
 #
 # Parámetros:
 #               - data : Columna a recorrer, para comprobar el termino.
 #               - search_term : Termino a comprobar.
 # -----------------------------------------------------------------------------

def contains_(data,search_term):
    have_ =[]
    for i in range(len(data)): #Recorremos la columna
        have_.append(int(search_term in data.iloc[i])) #Comprobamos si el termino
                                                       #esta en la palabra
    return have_

 # -----------------------------------------------------------------------------
 # Función: Cuenta la cantidad de veces que aparece por cada palabra de una
 #          columna los terminos de la secuencia pasada por parametro.
 #
 # Parámetros:
 #               - data : Columna a recorrer.
 #               - search_term : Secuencia a contar los terminos.
 # -----------------------------------------------------------------------------

def count_chars(data,search_term):
    have_ =[]
    for i in range(len(data)):
        count = 0
        for term in search_term:
            count+=data.iloc[i].count(term)
        have_.append(count)
    return have_

 # -----------------------------------------------------------------------------
 # Función: Cuenta la cantidad de conjuntos de letras seguidas que contiene
 #          una palabra.
 #
 # Parámetros:
 #               - data : Columna a recorrer.
 #               - search_term : Secuencia que contiene los terminos validos
 #                               para el conjunto
 # -----------------------------------------------------------------------------
def count_sets_(data,search_terms):
    sets_=[]
    for i in range(len(data)):
        count_general=0
        count = -1
        for letra in data.iloc[i]:
            #unidecode() quita los acentos y comprobamos si es de los terminos validos
            if unidecode(letra.lower()) in search_terms:
                count=count + 1
            else:
                if count>0:
                    count_general = count_general + 1
                count = -1
        if count>0:
            count_general = count_general + 1
        sets_.append(count_general)
    return sets_

 # -----------------------------------------------------------------------------
 # Función: Busca en una palabra la maxima distancia entre los elementos de
 #          una secuencia.
 #
 # Parámetros:
 #               - data : Columna a recorrer.
 #               - vowel : Booleano que indica si se quiere buscar la distancia
 #                         entre vocales (vowel=true) o entre consonnates
 #                         (vowel=false)
 #                               
 # -----------------------------------------------------------------------------
    
def distance_between_chars_(data,vowel):
    if(vowel):
        search_terms = 'aeiou'
    else:
        search_terms = 'bcdfghjklmnñpqrstvwxyz'
    max_ = []
    for i in range(len(data)):
        max=-1
        count=-1
        for letra in data.iloc[i]:
            if unidecode(letra.lower()) in search_terms:
                if count==-1:
                    count=count+1
                else:
                    if count>max:
                        max=count
                    count=0
            else:
                if count>-1:
                    count = count + 1
        if(max==-1):
            max=0
        max_.append(max)
    return max_

 # -----------------------------------------------------------------------------
 # Función: Calcula el porcentaje de ceros de las columnas introducidas por
 #          por parametro.
 #
 # Parámetros:
 #               - data : Dataset
 #               - columns: vector con el nombre de las columnas a calcular su porcentaje.
 #                               
 # -----------------------------------------------------------------------------
def porcentaje(data,columns):
    dataResult = pd.DataFrame()
    porcentajes2 = []
    for columna in columns:
        col=data[columna]
        num0=len(col)-np.count_nonzero(col)
        porcentajes2.append(((num0) / len(col)) * 100)
        dataResult[columna] = porcentajes2
        porcentajes2.clear()
    return dataResult

