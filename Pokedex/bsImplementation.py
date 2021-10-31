from bs4 import BeautifulSoup
import urllib.request

url = "http://www.pokexperto.net/index2.php?seccion=nds/nationaldex/pkmn&pk=4"
browser = urllib.request.urlopen(url)
html = browser.read()

bs = BeautifulSoup(html)
file = open("text.txt", 'w')
file.write(str(bs.prettify()))
file.close()