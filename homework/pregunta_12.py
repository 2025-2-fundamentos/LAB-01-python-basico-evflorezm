"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contenga como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
   
    with open("./files/input/data.csv", "r") as file:
        data = file.readlines()

    
    result = {}

    
    for line in data:
        columns = line.strip().split("\t")
        col1 = columns[0]  #
        col5_items = columns[4].split(",") 
        col5_sum = sum(int(item.split(":")[1]) for item in col5_items)

        
        if col1 in result:
            result[col1] += col5_sum
        else:
            result[col1] = col5_sum

    return result


print(pregunta_12())