# Dans ce module nous allons récupérer les informations spécifiques à chaque joueurs
# On va donc récuperer 
# Le nom complet 
# La position
# Droitier ou gaucher 
# Naissance
# Taille
# Poid
# Photo

#%% Fonction recuperation caracateristique
from url import allUrl
import pandas as pd 
import urllib.request
from bs4 import BeautifulSoup as bs
import re


def recupCaract(ligne,carac):
    debut = re.search(carac, str(ligne)).end()
    fin = debut
    while str(ligne)[fin] != "<":
        fin += 1

    return str(ligne)[debut+1:fin]

# %%
listurl = allUrl()

#%%
result = pd.DataFrame()
errorNom = []
errorGene = []


indice = 0 
for url in listurl:
    image = [""]
    nom = [""]
    nomComplet = [""]
    position = [""]
    piedFort = [""]
    taille = [""]
    poid = [""]
    dateNaissance = [""]
    lieuNaissance = [""]
    club = [""]

    indice += 1

    try:
        page = urllib.request.urlopen(url) 
        html = page.read().decode("utf-8")
        soup = bs(html, "html.parser")
        all = soup.find("div",id = "meta")
        containers = all.find_all("p")
    except:
        errorNom.append(url)
        continue

    try:
        image[0] = all.find("img").attrs["src"]
    except:
        image[0] = "Inconnue"

    nom[0] = all.h1.span.text


    for ligne in containers:
        if re.search(str(nom[0].replace(" ",".+")), str(ligne)):
            nomComplet[0] = ligne.text

        elif re.search("Position:|Droitier/Gaucher:|Footed",str(ligne)):
            if re.search("Position:", str(ligne)):
                position[0] = recupCaract(str(ligne),"Position:</strong>")
                position[0] = position[0].replace("\xa0▪\xa0","")

            if re.search("Droitier/Gaucher:|Footed", str(ligne)):
                if re.search("Droitier/Gaucher:", str(ligne)):
                    piedFort[0] = recupCaract(str(ligne),"Droitier/Gaucher:</strong>")
                else :
                    piedFort[0] = recupCaract(str(ligne),"Footed:</strong>")

        elif re.search('\"height\"|\"weight\"',str(ligne)):
            if re.search('\"height\"', str(ligne)):
                taille[0] = recupCaract(str(ligne),"height")
                taille[0] = taille[0].replace(">","")

            if re.search('\"weight\"', str(ligne)):
                poid[0]= recupCaract(str(ligne),"weight")
                poid[0] = poid[0].replace(">","")

        elif re.search("birthDate|birthPlace",str(ligne)):
            naissance = ligne.find_all("span")
            for item in naissance:
                if re.search("birthDate",str(item)):
                    dateNaissance[0] = item.text
                    dateNaissance[0] = dateNaissance[0].replace("\n","")
                if re.search("birthPlace",str(item)):
                    lieuNaissance[0] = item.text
                    lieuNaissance[0] = lieuNaissance[0].replace("\n","")

        elif re.search("Club:", str(ligne)):
            club[0] = ligne.a.text

    dfValeur = pd.DataFrame(
        {"Image":image,
        "Nom" : nom,
        "Nom complet": nomComplet,
        "Position": position,
        "Pied fort": piedFort,
        "Taille":taille,
        "Poid":poid,
        "Date de naissance": dateNaissance,
        "Lieu de naissance":lieuNaissance,
        "Club" : club
        }
    )
    print(indice)
    result = pd.concat([result, dfValeur])

#%%
result.set_index("Nom")
result.to_csv("StatistiquesPerso.csv", index=False)
# %%
len(errorNom)
# %%
