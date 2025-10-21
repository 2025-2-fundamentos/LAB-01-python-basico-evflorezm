"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_11():
    """
    Retorne un diccionario que contenga la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabéticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    """

    with open("./files/input/data.csv", "r") as file:
        data = file.readlines()


    letter_sums = {}


    for line in data:

        columns = line.strip().split("\t")
        col2_value = int(columns[1])  
        col4_letters = columns[3].split(",")  

        
        for letter in col4_letters:
            if letter in letter_sums:
                letter_sums[letter] += col2_value
            else:
                letter_sums[letter] = col2_value

 
    result = dict(sorted(letter_sums.items()))

    return result


print(pregunta_11())

