# [numero de usuario][numero de mensaje][Componente del mensaje (0 --> Mesnaje, 1 --> Estado)]
# 0 --> No leido
# 1 --> Leido
# 2 --> Borrado


def printMensajes(user):
    lista = usuarios[user]
    notMessage = True
    for count in range(len(lista)):
        if lista[count][1] == 0:
            print(f"{count + 1}) (NO LEIDO) {lista[count][0]}")
            notMessage = False
        if lista[count][1] == 1:
            print(f"{count + 1}) (LEIDO) {lista[count][0]}")
            notMessage = False
    if notMessage:
        print("\nUsted no tiene mensajes nuevos!\n")


def printBorrados(user):
    lista = usuarios[user]
    notMessage = True
    for count in range(len(lista)):
        if lista[count][1] == 2:
            print(f"{count + 1}) (BORRADO) {lista[count][0]}")
            notMessage = False
    if notMessage:
        print("\nUsted no tiene mensajes borrados!\n")


def sendMesaje(user):
    recipient = 0
    if user == 0:
        recipient = 1
    message = input("Mensaje: ")
    usuarios[recipient].append([message, 0])


def marcarLeido(user, messageId):
    if messageId < len(usuarios[user]):
        if usuarios[user][messageId]:
            if usuarios[user][messageId][1] != 1:
                usuarios[user][messageId][1] = 1
                print(f"Listo! Mensaje {messageId + 1} marcado como leido")
            else:
                print("Mensaje ya marcado como leido!")
        else:
            print("No existe mensaje con ese ID")
    else:
        print("No existe mensaje con ese ID")


def borrarMensaje(user, messageId):
    if messageId < len(usuarios[user]):
        if usuarios[user][messageId]:
            if usuarios[user][messageId][1] != 2:
                usuarios[user][messageId][1] = 2
                print(f"Listo! Mensaje {messageId + 1} borrado")
                return
        else:
            print("No existe mensaje con ese ID")
    else:
        print("No existe mensaje con ese ID")


def printStatistics(user):
    recipient = 0
    if user == 0:
        recipient = 1
    enviados = len(usuarios[recipient])
    total = len(usuarios[user])  # usuarios[noUser][0][4]
    leidos = 0
    noLeidos = 0
    borrados = 0
    for element in usuarios[user]:
        if element[1] == 0:
            noLeidos += 1
        elif element[1] == 1:
            leidos += 1
        else:
            borrados += 1
    print(f"Mensajes leidos ==> {leidos}")
    print(f"Mensajes no leidos ==> {noLeidos}")
    print(f"Mensajes borrados ==> {borrados}")
    print(f"Mensajes enviados ==> {enviados}")
    print(f"Total mensaje recibidos ==> {total}")


usuarios = [[], []]
menuPrincipal = ["Leer mensajes", "Ver mensajes borrados", "Marcar como leido", "Borrar mensaje", "Enviar mensaje",
                 "Estadisticas (log de actividades)", "Salir", ]
while True:
    noUser = int(input("Ingrese el numero del usuario: "))
    if noUser == 0 or noUser == 1:
        ################# Menu printing ###################
        print("\n")
        for count in range(len(menuPrincipal)):
            print(f"{count + 1}) {menuPrincipal[count]}")
        ####################################
        salir = False
        while not salir:
            inp = input("\nQue desea hacer: ")
            if inp == '1':
                printMensajes(noUser)
            elif inp == '2':
                printBorrados(noUser)
            elif inp == '3':
                Id = int(input("Ingrese el ID del mensaje: "))
                marcarLeido(noUser, Id - 1)
            elif inp == '4':
                Id = int(input("Ingrese el ID del mensaje: "))
                borrarMensaje(noUser, Id - 1)
            elif inp == '5':
                sendMesaje(noUser)
            elif inp == '6':
                printStatistics(noUser)
            elif inp == '7':
                salir = True
            else:
                print("Entrada invalida")
    else:
        print("Entrada invalida!")
