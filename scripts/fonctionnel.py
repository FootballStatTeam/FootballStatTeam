import urllib
from bs4 import BeautifulSoup as bs 
import re
import pandas as pd

# Création des containers avec les différents tableaux
def createContainers(url):
    page = urllib.request.urlopen(url) 
    html = page.read().decode("utf-8")
    soup = bs(html, "html.parser")

    containers = soup.find_all("tr", id = "stats")

    return containers


# Fonction récupérant la data souhaité dans une ligne
def recupData(line,data):
    try:
        debut = re.search('"'+data+'">',str(line)).end()

        indice = debut
        result = ""
        while str(line)[indice] != '<':
            result += str(line)[indice]
            indice+=1
    except AttributeError:
        result = ""

    return result


# Fonction corrigeant les noms des joueurs (caractère spéciaux)
def correctionNom(nomJoueur):
    nomJoueur = nomJoueur.replace(" ","-")
    nomJoueur = nomJoueur.replace("é","e")
    nomJoueur = nomJoueur.replace("ý","y")
    nomJoueur = nomJoueur.replace("ï","i")
    nomJoueur = nomJoueur.replace("á","a")
    nomJoueur = nomJoueur.replace("ç","c")
    nomJoueur = nomJoueur.replace("ö","o")
    nomJoueur = nomJoueur.replace("ñ","n")
    nomJoueur = nomJoueur.replace("ć","c")
    nomJoueur = nomJoueur.replace("ü","u")
    nomJoueur = nomJoueur.replace("í","i")
    nomJoueur = nomJoueur.replace("ž","z")
    nomJoueur = nomJoueur.replace("ã","a")
    nomJoueur = nomJoueur.replace("Á","A")
    nomJoueur = nomJoueur.replace("ğ","g")
    nomJoueur = nomJoueur.replace("É","E")
    nomJoueur = nomJoueur.replace("ı","i")
    nomJoueur = nomJoueur.replace("Ü","U")
    nomJoueur = nomJoueur.replace("Ö","O")
    nomJoueur = nomJoueur.replace("ø","o")
    nomJoueur = nomJoueur.replace("ó","o")
    nomJoueur = nomJoueur.replace("ú","u")
    nomJoueur = nomJoueur.replace("æ","ae")
    nomJoueur = nomJoueur.replace("ă","a")
    nomJoueur = nomJoueur.replace("š","s")
    nomJoueur = nomJoueur.replace("è","e")
    nomJoueur = nomJoueur.replace("ş","s")
    nomJoueur = nomJoueur.replace("ễ","e")
    nomJoueur = nomJoueur.replace("İ","I")
    nomJoueur = nomJoueur.replace("Ş","S")
    nomJoueur = nomJoueur.replace("Ó","O")
    nomJoueur = nomJoueur.replace("ț","t")
    nomJoueur = nomJoueur.replace("Ș","S")
    nomJoueur = nomJoueur.replace("ứ","u")
    nomJoueur = nomJoueur.replace("à","a")
    nomJoueur = nomJoueur.replace("ù","u")
    nomJoueur = nomJoueur.replace("ệ","e")
    nomJoueur = nomJoueur.replace("ô","o")
    nomJoueur = nomJoueur.replace("č","c")

    return nomJoueur


# Fonction poid d'une data frame
def mem_usage(pandas_obj):
    if isinstance(pandas_obj,pd.DataFrame):
        usage_b = pandas_obj.memory_usage(deep=True).sum()
    else:
        usage_b = pandas_obj.memory_usage(deep=True)    
    usage_mb = usage_b / 1024 ** 2 # convertir les bytes en megabytes
    return "{:03.2f} MB".format(usage_mb) # afficher sous format nombre (min 3 chiffres) et une précision de deux décimales


# Repérage de la ligue du joueur
def ligue(line):
    indice = re.search("comp_level",line).end()
    flag = True
    while flag:
        if (line[indice] == "<") and (line[indice+1] == "a"):
            flag = False
        indice += 1

    flag = True
    while flag:
        if (line[indice] == ">"):
            debut = indice + 1
            flag = False
        indice+=1

    flag = True
    while flag:
        if (line[indice] == "<"):
            fin = indice
            flag = False
        indice += 1


    return line[debut:fin]