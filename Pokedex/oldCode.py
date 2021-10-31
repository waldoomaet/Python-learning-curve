#
# Objetivo: extraer nombre, tipo, altura, peso y linea evolutiva de un pokemon
#

import urllib2

# -------------------------------------- Declaraciones ---------------------------------------#

pokemon = []
types = ['Normal', 'Lucha', 'Volador', 'Veneno', 'Tierra',
         'Roca', 'Insecto', 'Fantasma', 'Acero', 'Fuego',
         'Agua', 'Planta', 'Electrico', 'Psiquico', 'Hielo',
         'Dragon', 'Siniestro', 'Hada']

name = 0
_type = 1
color = 4
height = 5
weight = 6
description = 7
weakness = 8
stength = 9
evolution = 11
pok_num = 0


# -------------------------------------- Codigo ----------------------------------------------#

def getInfo(pok_num):
    site = "http://www.pokexperto.net/index2.php?seccion=nds/nationaldex/pkmn&pk=" + str(pok_num + 1)
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site, headers=hdr)
    webUrl = urllib2.urlopen(req)
    return webUrl.read()


def getInfoWS(pok_num):
    site = "http://www.pokexperto.net/index2.php?seccion=nds/nationaldex/estrategia&pk=" + str(pok_num + 1)
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib2.Request(site, headers=hdr)
    webUrl = urllib2.urlopen(req)
    return webUrl.read()


def findName(info):
    ubication1 = info.find('title')
    ubication1 = info.find(' ', ubication1)
    ubication2 = info.find(' ', ubication1 + 1)
    pokemon[pok_num].append(info[ubication1 + 1:ubication2])


def findType(info):
    ubication1 = info.find('<tr><td>Tipos:</td><td nowrap>')
    ubication_1 = info.find('<tr><td>Tipo:</td><td nowrap>')

    if ubication1 != -1:
        num_type = 1
        ubication1 = info.find('alt', ubication1)
    else:
        num_type = 0
        ubication1 = info.find('alt', ubication_1)

    ubication1 = info.find('"', ubication1)
    ubication2 = info.find('"', ubication1 + 1)

    if num_type:
        ubication3 = info.find('alt', ubication2)
        ubication3 = info.find('"', ubication3)
        ubication4 = info.find('"', ubication3 + 1)
        pokemon[pok_num].append(2)
        pokemon[pok_num].append(info[ubication1 + 1:ubication2])
        pokemon[pok_num].append(info[ubication3 + 1:ubication4])
    else:
        pokemon[pok_num].append(1)
        pokemon[pok_num].append(info[ubication1 + 1:ubication2])
        pokemon[pok_num].append('No tiene')


def findColor(info):
    ubication1 = info.find('<tr><td>Color') + len('<tr><td>Color')
    ubication1 = info.find('>', ubication1)
    ubication1 = info.find('>', ubication1 + 1)
    ubication2 = info.find('<', ubication1)
    pokemon[pok_num].append(info[ubication1 + 1:ubication2])


def findHeight(info):
    ubication1 = info.find('Altura')
    ubication1 = info.find('>', ubication1)
    ubication1 = info.find('>', ubication1 + 1)
    ubication2 = info.find('<', ubication1)
    pokemon[pok_num].append(info[ubication1 + 1:ubication2])


def findWeight(info):
    ubication1 = info.find('Peso')
    ubication1 = info.find('>', ubication1)
    ubication1 = info.find('>', ubication1 + 1)
    ubication2 = info.find('<', ubication1)
    pokemon[pok_num].append(info[ubication1 + 1:ubication2])


def findDescription(info):
    ubication1 = info.find('Información sobre ' + pokemon[pok_num][0])
    longg = len('<p>')
    ubication1 = info.find('<p>', ubication1)
    ubication1 = info.find('<p>', ubication1 + 1) + longg
    ubication2 = info.find('<p>', ubication1 + 1)
    description = info[ubication1:ubication2]
    description = description[:description.find('\r\n\t\t\t\t')]
    error = description.find('<strong>' + pokemon[pok_num][0] + '</strong>')
    if error != -1:
        longg = len('<strong>' + pokemon[pok_num][0] + '</strong>')
        finError = error + longg
        description = description[:error] + pokemon[pok_num][0] + description[finError:]
    pokemon[pok_num].append(description)


def findWeakness(info):
    ws = []
    ubication = info.find('Resistencias y Debilidades')
    if pokemon[pok_num][1] == 1:
        ws1 = info.find('<td><img src="3ds/sprites/tipos/' + pokemon[pok_num][2] + '.png" /></td>', ubication)
    else:
        ws1 = info.find(
            '<td nowrap><img src="3ds/sprites/tipos/' + pokemon[pok_num][2] + '.png" /> <img src="3ds/sprites/tipos/' +
            pokemon[pok_num][3] + '.png" /></td>', ubication)
    for x in range(0, 18):
        ws1 = info.find('>x', ws1)
        ws2 = info.find('<', ws1)
        ws3 = info[ws1 + 1:ws2]
        if ws3 == 'x&frac12;':
            ws3 = 'x/2'
        elif ws3 == 'x&frac14;':
            ws3 = 'x/4'
        ws.append(ws3)
        ws1 = ws2
    pokemon[pok_num].append(ws)


def findStrength(info):
    ws = []
    wss = []
    ubication = info.find('STAB, bonus por atacar con ataques del tipo del Pokémon')
    ws1 = info.find('<td><img src="3ds/sprites/tipos/' + pokemon[pok_num][2] + '.png" /></td>', ubication)
    ws11 = info.find('<td><img src="3ds/sprites/tipos/' + pokemon[pok_num][3] + '.png" /></td>', ubication)
    for x in range(0, 18):
        ws1 = info.find('>x', ws1)
        ws2 = info.find('<', ws1)
        ws3 = info[ws1 + 1:ws2]
        if ws3 == 'x&frac12;':
            ws3 = 'x/2'
        elif ws3 == 'x&frac14;':
            ws3 = 'x/4'
        ws.append(ws3)
        ws1 = ws2
        if pokemon[pok_num][1] == 2:
            ws11 = info.find('>x', ws11)
            ws22 = info.find('<', ws11)
            ws33 = info[ws11 + 1:ws22]
            if ws33 == 'x&frac12;':
                ws33 = 'x/2'
            elif ws33 == 'x&frac14;':
                ws33 = 'x/4'
            wss.append(ws33)
            ws11 = ws22
    pokemon[pok_num].append(ws)
    pokemon[pok_num].append(wss)


def processInfo(info, info1):
    pokemon.append([])
    findName(info)
    findType(info)
    findColor(info)
    findHeight(info)
    findWeight(info)
    findDescription(info)
    findWeakness(info1)
    findStrength(info1)


for x in range(0, 4):  # busca desde el pokemon 1 hasta el pokemon 809
    pok_num = x
    pok_url = getInfo(pok_num)
    pok_url1 = getInfoWS(pok_num)
    processInfo(pok_url, pok_url1)
    print (pokemon[pok_num])
