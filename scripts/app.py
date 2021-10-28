# Import des package nécessaire depuis le module

from pays import * 
from clubs import *
# Extraction des pages 
'''' Extraction des tables des pays : 
{nom du pays,
nombre de clubs dans le pays ,
lien vers l'ensembles des clubs du pays
 '''

link = "https://fbref.com/fr/equipes/"
resPays = LesPays(link)
print(resPays)
resPays.to_csv("tabPays.csv")

''' Extraction des tables des différentes clubs  de chaque pays:
 {nom du club ,
 lienClubDetails, 
 SexeDuClub (F/H), 
 divisionDuClub,
 linkDivisionDetail,
 DebutSaisonSave,
 DerniereSaisonSave,
 NombreDeCompetitionJoue,
 nombreDePremierePlace}
 '''

resClub= LesClubs(resPays.lienDesClubs)
print(resClub)
resClub.to_csv("tabClubs.csv")