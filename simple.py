
import random
                                # Primer Ejercicio
# -----------------------------------------------------------------------------------------------------
                                            # PT1

# defino la funcion para generar el diccionario
def generate_Dict(num):
    # dentro de mi funcion creo una variable que sera una lista 
    my_list = list()

    # recorro la lista con un loop donde agregara un dict a la lista en cada iteracion 
    for i in range(1, num + 1): #declaro el range como num + 1 para cuando se ejecute la func se muestre con una mejor experiencia
        my_list.append({"id":i, "age": random.randint(1,100)})

    # por ultimo retorno la lista a la funcion
    return my_list


# guardo la funcion asignada a una variable 
my_dict_list = generate_Dict(10)
print('Lista desordenada')
print(my_dict_list)
                                             # PT2

# creo la funcion que mandara a la terminal el mayor y el menor de la lista
def catch_old_young(param):
    # asigno a una nueva variable la lista ordenada por el parametro de age, y en orden de mayor a menor
    new_dict = sorted(param, key=lambda item:item["age"], reverse=True)
    print()
    print('lista ordenada de mayor a menor')
    print(new_dict)
    # imprimo los valores del menor y el mayor
    print()
    print('Persona de más edad y la menor edad')
    print(new_dict[0], new_dict[-1])
    # retorno el valor de la nueva lista ahora ordenada
    return new_dict

catch_old_young(my_dict_list)
# ------------------------------------------------------------------------------------------------