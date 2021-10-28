

import requests
from bs4 import BeautifulSoup
import pandas as pd

#************************************** Fonction pour extraire les informations d'un club  *********************************

def clubExtraction(tr_club) :
  
  soup_tr_i =  tr_club
  #print(soup_tr_i)
  soup_tr_i_th = soup_tr_i.find("th",class_= "left") # pour info nom et lien club 
  soup_tr_i_td = soup_tr_i.findAll("td") # pour le reste des info
  #print(soup_tr_i_td)
  #print(30*"-")
  if( len(soup_tr_i_td)!=0):
    #   # 1- Nom du club 
    NomDesClubs= soup_tr_i_th.find("a").get_text()
    #print(NomDesClubs)
    #   # 1bis - lien pour les détails du club
    lienClubDetails= "https://fbref.com"+str(soup_tr_i_th.find("a")).split('"')[1]
    #print(lienClubDetails)
    #   # 2- Sexe des joueurs du club
    SexeDuClub = soup_tr_i_td[0].get_text()
    #print(SexeDuClub)
    #   # 3- Division du chanpionant 
  
    #   #------------ Prise en compte la structure des page en fonction des  équipes -----------
    if(len(soup_tr_i_td[1])==0  ):
      division  =  " -- no info -- "
      linkDivisionDetail = "pas de détails "
    else:
      division = soup_tr_i_td[1].get_text() # Nom de la division
      #   print(division)
      linkDivisionDetail = "https://fbref.com"+str(soup_tr_i_td[1].find("a")).split('"')[1]#[1] # lien pour les détails concernant les résultats de cette division
      #  print(linkDivisionDetail)
      #   #4- Premiere saison enrégistée
    DebutSaison = soup_tr_i_td[2].get_text()
    # print(DebutSaison)
    #   #5- Dernière saison enrégisté
    DerniereSaison= soup_tr_i_td[3].get_text()
    #print(DerniereSaison)
    #   #6- Nombre de compétitions joués 
    NombreDeCompetitionJoue = soup_tr_i_td[4].get_text()
    #print(NombreDeCompetitionJoue)
    #   #7- Nombre de première place
    nombreDePremierePlace = soup_tr_i_td[5].get_text()
    #print(nombreDePremierePlace)
    #   #Creation d'un dataframe
    df_info_club= {
      # assign data of lists.
      "NomDesClubs": [NomDesClubs],
      "lienClubDetails": [lienClubDetails],
      "SexeDuClub": [SexeDuClub],
      "divisionDuClub" :[division],
      "linkDivisionDetail":[linkDivisionDetail],
      "DebutSaisonSave": [DebutSaison],
      "DerniereSaisonSave":[DerniereSaison],
      "NombreDeCompetitionJoue":[NombreDeCompetitionJoue],
      "nombreDePremierePlace":[nombreDePremierePlace] }
    # Create DataFrame.
    df_info_club = pd.DataFrame(df_info_club)
  else:
    print("Une ligne incohérente!!! ça doit être une header")
    #print(tabx)
  return df_info_club




  '''
  la fonction Les clubs . Parcours fait une boucle pour extraire dans chaque pays les informations de chaque club
  '''

def LesClubs(linkcountryclubs):
    lienDesClubs = linkcountryclubs #df_info_pays.lienDesClubs
    probleme= []
    frame = []

    for lien in lienDesClubs:
        lienDesClubs = lien
        
        print("**************** Je scrap ************************* "+ str(lienDesClubs))
        
        page = requests.get(lienDesClubs)
        soup = BeautifulSoup(page.content, "html.parser")
        soup_tr = soup.findAll("tr")

        print("Dans ce pays j'ai les infos de "+str(len(soup_tr))+ " Clubs")
        
        for tr in range(0,len(soup_tr)) :
            
            try:
                club= clubExtraction(soup_tr[tr])
                print("* ---------- "+ str(club["NomDesClubs"])+ "------------ extraction Terminé ","\n")
                frame.append(club)
                
            except:
                probleme.append(soup_tr[tr])
        
        
    df_ClubDesPays = pd.concat(frame) 


    return df_ClubDesPays