import random

                                            # ejercicio 2
# ----------------------------------------------------------------------------------

# instanciamos las listas
row = 5
column = 5
# match = list()

# estas listas msotraran un conjunto de listas correspondientes a las filas y columnas
row_list= list()
column_list = list()
print()
print('Aqui se mostrará  la matriz 5 x 5')
# loop para crear la matriz 5x5 con numeros aleatorios
# r crea las row y por cada iteracion creara 5 columnas
for r in range(row):
    # creo otra lista que contendra los numeros de cada row en listas separadas
    random_row = list()
    # c crea los numeros aleatorios para rellenar 
    for c in range(column):
        random_number = random.randint(0,5)

        random_row.append(random_number)
        print(random_number, end=' ')
   

    # bien
    row_list.append(random_row)

    print()
 
    
print()
# creo un loop para  obtener todos los numeros de cada columna alineadas verticalmente
for d in range(len(row_list)):

    random_colum = list()
    # creo un loop interno para acceder a los numeros corresponientes en columna de cada fila
    for f in range(len(row_list)):
        random_colum.append(row_list[f][d])
    
    
    column_list.append(random_colum)

# para comprobar que funcione hago print de la listas de columnas y filas
print('listas de las rows:')
print(row_list)
print()
print('listas de las columns:')
print(column_list)

# creo una nueva lista que contendra un dict con las coordenadas cartecianas de una coincidencia de 4 numeros iguales consecutivos en una columna
match_colum = list()

for w in range(len(column_list)):
    # selecciono cada pocicion de todas las listas de columnas con la pocision determinada por "w"
    inner_list = column_list[w]
    
    if inner_list[0] == inner_list[1] and  inner_list[2] == inner_list[0] and inner_list[0] == inner_list[3]:
        match_colum.append({"ejeX" : w + 1, "ejeY" : [2, 5]})
    elif inner_list[-1] == inner_list[-2] and  inner_list[-3] == inner_list[-1] and inner_list[-1] == inner_list[-4]:
        match_colum.append({"ejeX" : w + 1, "ejeY" : [1, 4]})


# repito el procedimiento anterior pero ahora con los row
match_row = list()

for h in range(len(row_list)):
    # selecciono cada pocicion de todas las listas de columnas con la pocision determinada por "h"
    inner_list = row_list[h]

    if inner_list[0] == inner_list[1] and  inner_list[2] == inner_list[0] and inner_list[0] == inner_list[3]:
        match_row.append({"ejeY" : 6 - h - 1, "ejeX" : [1, 4]})
    elif inner_list[-1] == inner_list[-2] and  inner_list[-3] == inner_list[-1] and inner_list[-1] == inner_list[-4]:
        match_row.append({"ejeY" : 6 - h - 1, "ejeX" : [2, 5]})

print()
print('Coincidencia de 4 numeros en rows')
print(match_row)
print()
print('Coincidencia de 4 numeros en columnas')
print(match_colum)





