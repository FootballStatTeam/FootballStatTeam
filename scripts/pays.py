

################################################################################################################################
# ############################### Les Pays : le nombre de club et lien des clubs ###############################################
################################################################################################################################

import requests
from bs4 import BeautifulSoup
import pandas as pd


#************ Fonction pour récupéré un pays **********************************
def nom_pays(tabx):
    #print(tab1.prettify())
    nom_pays = tabx.find(class_="left").get_text()
    return nom_pays

#********** Fonction pour récupérer tous les pays ****************************
#tab1 = tab[1]
def all_contries(tab, tabLength):
    contries = []
    for i in range(0,tabLength):
        try:
            tabx= tab[i]
            pays=nom_pays(tabx)
            contries.append(pays)
        except:
            print("Exception thrown. x does not exist.")
    return contries

#*********** fonction pour récupéré le lien des clubs d'un pays ***************
def lien_clubs(tabx):
    # récupération et création du lien
    a= tabx.find("a")
    # le lien se trouve dans les "" je découpe donc avec les "
    # e récupère le lien non complet à l'index 1(deuxieme position)
    # Je recompose le lien complet(lien vers les clubs )
    lienClubs= "https://fbref.com"+str(a).split('"')[1]
    return lienClubs

# ********* Fonction pour récupérer tous les liens ******************************
 
#tab1 = tab[1]
def all_link(tab, tabLength):
    links = []
    for i in range(0,tabLength):
        try:
            tabx= tab[i]
            link=lien_clubs(tabx)
            links.append(link)
        except:
            print("Exception thrown. x does not exist.")
    return links

#*************** Fonction pour técupérr le nombre de club dans le pays ****************
def nbClub_pays(tabx):
    # nombre de club dans le pays se trouve dans une classe right
    nbClub = tabx                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   .findAll(class_="right")
    # le premier element de la classe contien le nombre de club
    nbclub_1 = nbClub[1]
    # récupération du nombre de club 
    nombre_de_clubs = nbclub_1.find("a").get_text()
    return nombre_de_clubs

#*************** Nombre de club dans tous les pays **************************************

#tab1 = tab[1]
def all_nbClub_pays(tab, tabLength):
    nbClubs = []
    for i in range(0,tabLength):
        try:
            tabx= tab[i]
            nbclub=nbClub_pays(tabx)
            nbClubs.append(nbclub)
        except:
            print("Exception thrown. x does not exist.")
    return nbClubs



# ****************************** Création de data frame des pays ( Pays des : le nombre de club et lien des clubs )



#****************************** Fonction pour créer les pays 
def LesPays( countriesPagelink):

    #countriesPagelink = "https://fbref.com/fr/equipes/"
    # lecture de la page
    page= requests.get(countriesPagelink)
    soup = BeautifulSoup(page.content, "html.parser")
    tab= soup.findAll("tr")
    # la longueyr de la table
    tabLength = len(tab)

    df_info_pays= {

        # assign data of lists.
        "pays" : all_contries(tab=tab ,tabLength=tabLength),
        "nombreDeClubs" : all_nbClub_pays(tab=tab,tabLength=tabLength),
        "lienDesClubs" : all_link(tab=tab,tabLength=tabLength)}

    # Create DataFrame.
    df_info_pays = pd.DataFrame(df_info_pays)
    # Print the output.
    return df_info_pays