import urllib.request
from FileMgmt import newOpen


class Pokemon:
    Pokemons = []

    def __init__(self, pokNum):
        self.num = pokNum
        self.html = Pokemon.getInfo(pokNum)
        self.name = self.getName()
        self.type = self.getTypes()
        self.weight = self.getGeneral("Peso")
        self.height = self.getGeneral("Altura")
        self.color = self.getGeneral("Color")
        Pokemon.Pokemons.append(self)

    def getName(self):
        ref = "<title>"
        refLen = len(ref)
        preBegin = self.html.find(ref) + refLen
        begin = self.html.find(' ', preBegin) + 1
        end = self.html.find(' ', begin)
        return self.html[begin:end]

    # This method is specifically for those informations that their way of straction is similar
    def getGeneral(self, toGet):
        toGet = f"<tr><td>{toGet}:</td><td>"
        toGetLen = len(toGet)
        begin = self.html.find(toGet) + toGetLen
        end = self.html.find('<', begin)
        return self.html[begin:end]

    def getTypes(self):
        # Reference of multi-type pokemons
        ref1 = "<tr><td>Tipos:</td><td nowrap>"

        # Reference of single-type pokemons
        ref2 = "<tr><td>Tipo:</td><td nowrap>"

        # After this tag is the info that we want
        typeRef = 'alt="'
        typeRefLen = len(typeRef)

        # At the beginning it is assumed that the pokemon is single-type
        repetitions = 1
        ref = ref2
        refLen = len(ref2)

        type = []
        if ref1 in self.html:  # It means that it has multiple types
            repetitions = 2
            ref = ref1
            refLen = len(ref1)
        preBegin = self.html.find(ref) + refLen
        for count in range(repetitions):
            begin = self.html.find(typeRef, preBegin) + typeRefLen
            end = self.html.find('"', begin)
            type.append(self.html[begin:end])
            preBegin = begin
        return type

    @staticmethod
    def getInfo(pokNum):
        url = f"http://www.pokexperto.net/index2.php?seccion=nds/nationaldex/pkmn&pk={pokNum}"
        output = urllib.request.urlopen(url)
        return str(output.read())

num = int(input("Introduzca el numero: "))
pok = Pokemon(num)
print(pok.name)
print(pok.type)
print(pok.color)
print(pok.weight)
print(pok.height)
input()