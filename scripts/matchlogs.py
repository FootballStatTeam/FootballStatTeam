#%%
from numpy import mat
from url import allUrl
import urllib.request
import re
from bs4 import BeautifulSoup as bs 
import pandas as pd
from fonctionnel import recupData
#%%
listUrl = allUrl()

#%% 
def recupDataHref(data, log):
    fin = re.search('\"'+data+'\"', str(log)).end()
    flag = True
    while flag:
        if str(log)[fin] == "/" and str(log)[fin+1] == "a" and str(log)[fin+2] == ">":
            flag = False
        fin += 1
    fin -= 2
    
    debut = fin
    flag = True
    while flag:
        if str(log)[debut] == ">":
            flag = False
        debut -= 1
    debut += 2

    return str(log)[debut:fin]
#%%
listSaison = []
errorNom = []

indice = 0
for url in listUrl:
    try:
        page = urllib.request.urlopen(url) 
        html = page.read().decode("utf-8")
        soup = bs(html, "html.parser")
        all = soup.find("div",id="all_stats_standard")
        containers = all.tbody.find_all("tr",id = "stats")
    except:
        errorNom.append(url)
        continue

    joueur = url.split("/")[-1]
    id = url.split("/")[-2]

    for index in range(len(containers)):
        saison = containers[index].find("th", class_ = "left").text
        urlSaison = "https://fbref.com/en/players/"+str(id)+"/matchlogs/"+str(saison)+"/summary/"+str(joueur)+"-Match-Logs"
        listSaison.append(urlSaison)

    indice += 1
    print(indice)


    #%% 
result = pd.DataFrame({"Url matchlogs" : listSaison})
result.to_csv("urlMatchLogs.csv", index = False)


#%%
url = "https://fbref.com/en/players/d70ce98e/matchlogs/2017-2018/summary/Lionel-Messi-Match-Logs"
page = urllib.request.urlopen(url) 
html = page.read().decode("utf-8")
soup = bs(html, "html.parser")
all = soup.find("div",id="div_matchlogs_all")
matchLog = all.tbody.find_all("tr")

date = [""] * len(matchLog)
jour = [""] * len(matchLog)
competition = [""] * len(matchLog)
round = [""] * len(matchLog)
venue = [""] * len(matchLog)
result = [""] * len(matchLog)
squad = [""] * len(matchLog)
opponent = [""] * len(matchLog)
start = [""] * len(matchLog)
pos = [""] * len(matchLog)
minutePlayed = [""] * len(matchLog)
goals = [""] * len(matchLog)
assists = [""] * len(matchLog)
penaltyGoals = [""] * len(matchLog)
penaltyAttempted = [""] * len(matchLog)
shotTotal = [""] * len(matchLog)
shotOnTarget = [""] * len(matchLog)
yellowCard = [""] * len(matchLog)
redCard = [""] * len(matchLog)
touches = [""] * len(matchLog)
pressureApply = [""] * len(matchLog)
tackles = [""] * len(matchLog)
interceptions = [""] * len(matchLog)
block = [""] * len(matchLog)
SCA = [""] * len(matchLog)
GCA = [""] * len(matchLog)
passesComplete = [""] * len(matchLog)
passesTotal = [""] * len(matchLog)
ballCarries = [""] * len(matchLog)
dribbleSuccedeed = [""] * len(matchLog)
dribbleAttempted = [""] * len(matchLog)

for match in range(len(matchLog)):
    print(match)
    try:
        date[match] = matchLog[match].find("th").text
        jour[match] = recupData(str(matchLog[match]),"dayofweek")
        if re.search('\"comp\"', str(matchLog[match])):
            competition[match] = recupDataHref("comp", matchLog[match])


        if re.search('\"round\"', str(matchLog[match])):
            round[match] = recupDataHref("round", matchLog[match])

        venue[match] = recupData(str(matchLog[match]),"venue")

        if re.search('\"result\"', str(matchLog[match])):
            debut = re.search('\"result\"', str(matchLog[match])).end()
            flag = True
            while flag:
                if str(matchLog[match])[debut] == ">":
                    flag = False
                debut += 1

            fin = debut
            flag = True
            while flag:
                if str(matchLog[match])[fin] == "<":
                    flag = False
                fin += 1

            result[match] = str(matchLog[match])[debut:fin-1]

        if re.search('\"squad\"', str(matchLog[match])):
            squad[match] = recupDataHref("squad", matchLog[match])


        if re.search('\"opponent\"', str(matchLog[match])):
            opponent[match] = recupDataHref("opponent", matchLog[match])
    except:
        continue

    start[match] = recupData(str(matchLog[match]),"game_started")
    pos[match] = recupData(str(matchLog[match]),"position")
    minutePlayed[match] = recupData(str(matchLog[match]),"minutes")
    goals[match] = recupData(str(matchLog[match]),"goals")
    assists[match] = recupData(str(matchLog[match]),"assists")
    penaltyGoals[match] = recupData(str(matchLog[match]),"pens_made")
    penaltyAttempted[match] = recupData(str(matchLog[match]),"pens_att")
    shotTotal[match] = recupData(str(matchLog[match]),"shots_total")
    shotOnTarget[match] = recupData(str(matchLog[match]),"shots_on_target")
    yellowCard[match] = recupData(str(matchLog[match]),"cards_yellow")
    redCard[match] = recupData(str(matchLog[match]),"cards_red")
    touches[match] = recupData(str(matchLog[match]),"touches")
    pressureApply[match] = recupData(str(matchLog[match]),"pressures")
    tackles[match] = recupData(str(matchLog[match]),"tackles")
    interceptions[match] = recupData(str(matchLog[match]),"interceptions")
    block[match] = recupData(str(matchLog[match]),"blocks")
    SCA[match] = recupData(str(matchLog[match]),"sca")
    GCA[match] = recupData(str(matchLog[match]),"gca")
    passesComplete[match] = recupData(str(matchLog[match]),"passes_completed")
    passesTotal[match] = recupData(str(matchLog[match]),"passes")
    ballCarries[match] = recupData(str(matchLog[match]),"carries")
    dribbleSuccedeed[match] = recupData(str(matchLog[match]),"dribbles_completed")
    dribbleAttempted[match] = recupData(str(matchLog[match]),"dribbles")


dfMatch = pd.DataFrame({"Date":date,
            "Jour":jour,
            "Competition":competition,
            "Round":round,
            "Venue":venue,
            "Resultats":result,
            "Equipe":squad,
            "Opponent":opponent,
            "Start match":start,
            "Position":pos,
            "Minute played":minutePlayed,
            "Goals":goals,
            "Passes decisives":assists,
            "Penalty goals":penaltyGoals,
            "Penalty attempted":penaltyAttempted,
            "Total shots":shotTotal,
            "Shot on target":shotOnTarget,
            "Yellow cards":yellowCard,
            "Red cards":redCard,
            "Touches":touches,
            "Pressure applies":pressureApply,
            "Tackles": tackles,
            "Interceptions":interceptions,
            "Block":block,
            "SCA":SCA,
            "GCA":GCA,
            "Passes completed":passesComplete,
            "Passes total": passesTotal,
            "Ball Carries":ballCarries,
            "Dribble succedeed":dribbleSuccedeed,
            "Dribble attempted":dribbleAttempted})


# %%
dfMatch.to_csv("test.csv",index=False)

# %%
