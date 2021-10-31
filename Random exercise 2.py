# Escriba el programa que haciendo uso de funciones, lea N números
# dados por el usuario, y luego muestra, el menor, el mayor y el
# promedio de estos números.


def menor_Mayor_Promedio(n):
    suma = 0
    numeros = []
    for count in range(n):
        numero = int(input("Numero " + str(count + 1) + ": "))
        numeros.append(numero)
        suma = suma + numero
    print("El minimo es: " + str(min(numeros)))
    print("El maximo es: " + str(max(numeros)))
    print("El promedio es: " + str(suma/n))


n = int(input("Indique cuantos numeros va a ingresar: "))
menor_Mayor_Promedio(n)

