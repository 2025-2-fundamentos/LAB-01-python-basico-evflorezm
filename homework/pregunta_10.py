"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_10():
    """
    Retorne una lista de tuplas que contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """

    with open("./files/input/data.csv", "r") as file:
        data = file.readlines()
    result = []

    for line in data:
        
        columns = line.strip().split("\t")
        letter = columns[0]  
        col4_elements = len(columns[3].split(",")) 
        col5_elements = len(columns[4].split(","))  
        result.append((letter, col4_elements, col5_elements))

    return result

print(pregunta_10())
