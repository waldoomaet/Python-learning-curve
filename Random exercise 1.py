# Escriba un programa usando funciones, que muestre en pantalla todos
# los números múltiplos de 13 que estén entre 1 y 999; y que al
# final, muestre un mensaje con la suma de todos los múltiplos de 13
# que sean impares.


def multiplos():
    suma = 0
    print("Los multiplos de 13 son: ")
    for count in range(1, 999):
        if count % 13 == 0:
            print(count)
            if count % 2 == 1:
                suma = suma + count
    print("La suma de los múltiplos impares de 13, es = " + str(suma))


multiplos()