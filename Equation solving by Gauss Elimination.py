def entreRenglonesOp(ecuacion1, ecuacion2, pivote):
    newEcuation = []
    for count in range(len(ecuacion1)):
        newEcuation.append(ecuacion2[count] - (pivote * ecuacion1[count]))
    return newEcuation

def divElementalOp(ecuacion, escalar):
    newEcuacion = []
    for element in ecuacion:
        newEcuacion.append(element / escalar)
    return newEcuacion


def getPivote(ecuacion):
    for element in ecuacion:
        if element != 0:
            return element


#########################
### Inicio del codigo
#########################

ecuaciones = []
ecuacionCount = int(input("Indique la cantidad de ecuaciones: "))
for ecuacion in range(ecuacionCount):
    ecuacionList = []
    print(f"Ecuacion {ecuacion + 1}: ")
    for variable in range(ecuacionCount):
        inp = float(input(f"Indique el valor del coeficiente de la variable {variable + 1}: "))
        ecuacionList.append(inp)
    inp = float(input(f"Indique el valor de la constante de la ecuacion {ecuacion + 1}: "))
    ecuacionList.append(inp)
    ecuaciones.append(ecuacionList)
print('')  # Solo es por estetica


for count in range(ecuacionCount - 1):
    ecuacionPrin = ecuaciones[count]
    pivotePrin = getPivote(ecuacionPrin)
    ecuacionPrin = divElementalOp(ecuacionPrin, pivotePrin)
    ecuaciones[count] = ecuacionPrin
    for countplus1 in range(count + 1, ecuacionCount):
        pivoteActual = getPivote(ecuaciones[countplus1])
        ecuaciones[countplus1] = entreRenglonesOp(ecuacionPrin, ecuaciones[countplus1], pivoteActual)


ecuaciones.reverse()
for count in range(ecuacionCount):
    pos = ecuacionCount - 1 - count
    coeficiente = ecuaciones[count].pop(-2 - count)
    valor = ecuaciones[count].pop(-1)
    for elements in ecuaciones[count]:
        valor -= elements
    print(f"El valor de la variable {ecuacionCount - count} es: {(1 / coeficiente) * valor}")
    for countplus1 in range(count + 1, ecuacionCount):
        ecuaciones[countplus1][pos] = ecuaciones[countplus1][pos] * ((1 / coeficiente) * valor)
