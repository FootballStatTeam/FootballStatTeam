# %%
import urllib.request
from bs4 import BeautifulSoup as bs 
import re
import pandas as pd
from fonctionnel import correctionNom, createContainers

# Récupération de toutes les initials possibles
def allInitials():
    url = "https://fbref.com/en/players/"
    page = urllib.request.urlopen(url)
    html = page.read().decode("utf-8")
    soup = bs(html, "html.parser")
        
    containers = soup.find_all("div", id="div_2201552314")
    containers = containers[0].find_all("a")

    initials = []

    for index in containers:
        initial = (index.text).lower()
        initials.append(initial)

    return initials

# Récupération de l'id du joueur et du nom du joueur (indispensable pour URL)

def idJoueur():
    initials = allInitials()
    joueurs = []
    ids = []

    for indice in initials:
        url = "https://fbref.com/en/players/"+str(indice)+"/"
        page = urllib.request.urlopen(url)
        html = page.read().decode("utf-8")
        soup = bs(html, "html.parser")

        containers = soup.find_all("div", class_ = "section_content")
        containers = containers[0].find_all("p")

        for index in containers:
            joueur = index.a.text
            id = re.findall('\w{8}',str(index))[0]
            date = re.findall('>\d{4}|\d{4}-\d{4}',str(index))

            if date != []:
                date = date[0].split("-")
            if ( "2022" in date):
                joueurs.append(joueur)
                ids.append(id)

    df = pd.DataFrame(
        {'id' : ids,
        'Joueur' : joueurs} 
    )

    return (df)


# Recupération de tout les urls sous liste

def allUrl():
    df = idJoueur()
    listUrl = []
    for i in range(0,len(df)-1):
        joueur = correctionNom(df.Joueur[i])
        url = "https://fbref.com/en/players/"+str(df.id[i])+"/"+joueur
        listUrl.append(url)

    return (listUrl)
# %%
