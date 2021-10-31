# Esto indica la cantidad de elementos que seran introducidos por el usuario
cantidadElementos = int(input("Introduzca la cantidad tipos de frutas: "))

# Esta variable almacena el conjunto de la fruta y su cantidad 
frutas = []

# Esta variable es con el fin de sumar todas las cantidades
# de frutas para posteriormente obtener el promedio
conteo = 0

# Basado en dicha cantidad de elementos,
# se haran dicha cantidad de iteraciones 
for count in range(cantidadElementos):
	
	# Toma el nombre de la fruta (count + 1 es solo con fines decorativos)
	fruta = input(f"Introduzca el nombre de la fruta numero {count + 1}: ")
	
	# Toma la cantidad de dicha fruta
	cantidad = int(input(f"Introduzca la cantidad de dicha fruta: "))
	conteo += cantidad
	
	# Almacena el conjunto de la fruta y su cantidad como una lista
	frutas.append([fruta, cantidad])
	
# Calculo del promedio
average = conteo/cantidadElementos

# Impresion del promedio
print(f"\nEl promedio es de: {average}.\n")

for elemento in frutas:
	fruta = elemento[0]
	cantidad = elemento[1]
	
	# Si la cantidad de dicha fruta es menor al promedio
	if cantidad < average:
		# Se muestra por pantalla la fruta
		print(f"La cantidad de {fruta}(s) es menor que el promedio (total es de {cantidad}).")