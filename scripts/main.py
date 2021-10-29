#%%
from bs4 import BeautifulSoup as bs 
import urllib.request
import re
import pandas as pd
from fonctionnel import createContainers
from url import allUrl
import tableau

#%%
def main():
    result = pd.DataFrame()

    listurl = allUrl()
    errorNom = []
    errorGene = []

    indice = 0 
    for url in listurl:
        indice += 1
        try:
            page = urllib.request.urlopen(url) 
            html = page.read().decode("utf-8")
            soup = bs(html, "html.parser")
            all = soup.find_all("div",class_="table_wrapper tabbed")
            containers = createContainers(url)
        except:
            errorNom.append(url)
            continue


        nbAnnee = 0
        try :
            while containers[nbAnnee].find("th", class_ = "left").text.split(sep = "-") <= containers[nbAnnee+1].find("th", class_ = "left").text.split(sep = "-"):
                nbAnnee += 1
        except IndexError:
            nbAnnee = 0


        #Initialisation des listes
        nomJoueur = [re.split("\/",url)[-1]] * (nbAnnee+1)
        annees = [""]*(nbAnnee+1)
        ages = [""]*(nbAnnee+1)
        clubs = [""]*(nbAnnee+1)
        ligues = [""]*(nbAnnee+1)
        matchsPlayed = [""]*(nbAnnee+1)
        matchsBegin = [""]*(nbAnnee+1)
        minutesPlayed = [""]*(nbAnnee+1)
        yellowCards = [""]*(nbAnnee+1)
        redCards = [""]*(nbAnnee+1)
        goals = [""]*(nbAnnee+1)
        decisivePasses = [""]*(nbAnnee+1)
        nonPenaltyGoals = [""]*(nbAnnee+1)
        penaltyGoals = [""]*(nbAnnee+1)
        penaltyAttempteds = [""]*(nbAnnee+1) 
        shotsTotal = [""]*(nbAnnee+1)
        shotsOnTarget = [""]*(nbAnnee+1)
        distance = [""]*(nbAnnee+1)
        freeShots = [""]*(nbAnnee+1)
        passesCompleted = [""]*(nbAnnee+1)
        passesAttempted = [""]*(nbAnnee+1)
        totalDistance = [""]*(nbAnnee+1)
        passesCompletedShort = [""]*(nbAnnee+1)
        passesAttemptedShort = [""]*(nbAnnee+1)
        passesCompletedMedium = [""]*(nbAnnee+1)
        passesAttemptedMedium = [""]*(nbAnnee+1)
        passesCompletedLong = [""]*(nbAnnee+1)
        passesAttemptedLong = [""]*(nbAnnee+1)
        passesLeadShots = [""]*(nbAnnee+1)
        oneTierPitch = [""]*(nbAnnee+1)
        passesCompleted18Yard = [""]*(nbAnnee+1)
        crossCompletedt18yard = [""]*(nbAnnee+1)
        Prog = [""]*(nbAnnee+1)
        livePasses = [""]*(nbAnnee+1)
        deadPasses = [""]*(nbAnnee+1)
        passesAttemptedFreeKick = [""]*(nbAnnee+1)
        completedPassesBackDefenders = [""]*(nbAnnee+1)
        passesUnderPressure = [""]*(nbAnnee+1)
        passesMore40Yards = [""]*(nbAnnee+1)
        crosses = [""]*(nbAnnee+1)
        cornerKicks = [""]*(nbAnnee+1)
        cornerKickIn = [""]*(nbAnnee+1)
        cornerKickOut = [""]*(nbAnnee+1)
        cornerKickStraight = [""]*(nbAnnee+1)
        groundPasses = [""]*(nbAnnee+1)
        lowPasses = [""]*(nbAnnee+1)
        highPasses = [""]*(nbAnnee+1)
        leftFootPasses = [""]*(nbAnnee+1)
        rightFootPasses = [""]*(nbAnnee+1)
        headPasses = [""]*(nbAnnee+1)
        throwIn = [""]*(nbAnnee+1)
        otherPasses = [""]*(nbAnnee+1)
        offsidesPasses = [""]*(nbAnnee+1)
        outBoundPasses = [""]*(nbAnnee+1)
        interceptedPasses = [""]*(nbAnnee+1)
        blockedPasses = [""]*(nbAnnee+1)
        SCA = [""]*(nbAnnee+1)
        passesLiveLeadShotAttempted = [""]*(nbAnnee+1)
        passesDeadLeadShotAttempted = [""]*(nbAnnee+1)
        dribleLeadShotAttempted = [""]*(nbAnnee+1)
        shotLeadShotAttempted = [""]*(nbAnnee+1)
        foulDrawLeadShotAttempted = [""]*(nbAnnee+1)
        defenseLeadShotAttempted = [""]*(nbAnnee+1)
        GCA = [""]*(nbAnnee+1)
        passesLiveLeadGoal= [""]*(nbAnnee+1)
        passesDeadLeadGoal = [""]*(nbAnnee+1)
        dribleLeadGoal = [""]*(nbAnnee+1)
        shotLeadGoal = [""]*(nbAnnee+1)
        foulDrawLeadGoal = [""]*(nbAnnee+1)
        defenseLeadGoal = [""]*(nbAnnee+1)
        trkl = [""]*(nbAnnee+1)
        trklW = [""]*(nbAnnee+1)
        def3Rd = [""]*(nbAnnee+1)
        mid3Rd = [""]*(nbAnnee+1)
        att3Rd = [""]*(nbAnnee+1)
        trklDribble = [""]*(nbAnnee+1)
        pastDribble = [""]*(nbAnnee+1)
        pressures = [""]*(nbAnnee+1)
        pressuresSucceded = [""]*(nbAnnee+1)
        pressuresDef3Rd = [""]*(nbAnnee+1)
        pressuresMid3Rd = [""]*(nbAnnee+1)
        pressuresAtt3Rd = [""]*(nbAnnee+1)
        defPassesBlocked = [""]*(nbAnnee+1)
        defShotBlocked = [""]*(nbAnnee+1)
        defShotTargetBlocked = [""]*(nbAnnee+1)
        Interceptions = [""]*(nbAnnee+1)
        clearances = [""]*(nbAnnee+1)
        errorLeadShot = [""]*(nbAnnee+1)
        touches = [""]*(nbAnnee+1)
        touchesDefPenArea = [""]*(nbAnnee+1)
        touchesDef3Rd = [""]*(nbAnnee+1)
        touchesMid3Rd = [""]*(nbAnnee+1)
        touchesAtt3Rd = [""]*(nbAnnee+1)
        touchesAttPenArea = [""]*(nbAnnee+1)
        touchesLive = [""]*(nbAnnee+1)
        dribbleSucceed = [""]*(nbAnnee+1)
        dribbleAttempted = [""]*(nbAnnee+1)
        numberPlayerDribbled = [""]*(nbAnnee+1)
        dribbleThroughtlegs = [""]*(nbAnnee+1)
        carriesFeet = [""]*(nbAnnee+1)
        distanceControlBall = [""]*(nbAnnee+1)
        distanceControlOpponentGoal = [""]*(nbAnnee+1)
        carriesCloseGoal = [""]*(nbAnnee+1)
        keepAgainstPlayer = [""]*(nbAnnee+1)
        targetPasses = [""]*(nbAnnee+1)
        receivedPasses = [""]*(nbAnnee+1)
        completedMatchPlayed = [""]*(nbAnnee+1)
        averagePointEarnedTeam = [""]*(nbAnnee+1)
        onG = [""]*(nbAnnee+1)
        doubleYellowCard = [""]*(nbAnnee+1)
        foulsCommited = [""]*(nbAnnee+1)
        foulsDrawn = [""]*(nbAnnee+1)
        offsides = [""]*(nbAnnee+1)
        penaltyConceded = [""]*(nbAnnee+1)
        ownGoal = [""]*(nbAnnee+1)
        recoveredBall = [""]*(nbAnnee+1)
        aerialWon = [""]*(nbAnnee+1)
        aerialLoose = [""]*(nbAnnee+1)

        try:
            for tab in all:
                if re.search("all_stats_standard",str(tab)):
                    containers = tab.find_all("tr",id = "stats")
                    for index in range(0,len(containers),1):
                        tableau.standartStats(containers,index)
                    

                elif re.search("all_stats_shooting", str(tab)):
                    containers = tab.find_all("tr",id = "stats")
                    for index in range(0,len(containers),1):
                        tableau.shooting(containers,index) 


                elif re.search("all_stats_passing", str(tab)):
                    containers = tab.find_all("tr",id = "stats")
                    for index in range(0,len(containers),1):
                        tableau.passing(containers,index) 


                elif re.search("all_stats_passing_types", str(tab)):
                    containers = tab.find_all("tr",id = "stats")
                    for index in range(0,len(containers),1):
                        tableau.passTypes(containers, index) 


                elif re.search("all_stats_gca", str(tab)):
                    containers = tab.find_all("tr",id = "stats")
                    for index in range(0,len(containers),1):
                        tableau.goalShotCreation(containers, index) 


                elif re.search("all_stats_defense", str(tab)):
                    containers = tab.find_all("tr",id = "stats")
                    for index in range(0,len(containers),1):
                        tableau.defensiveActions(containers,index) 


                elif re.search("all_stats_possession", str(tab)):
                    containers = tab.find_all("tr",id = "stats")
                    for index in range(0,len(containers),1):
                        tableau.possession(containers, index)  


                elif re.search("all_stats_playing_time", str(tab)):
                    containers = tab.find_all("tr",id = "stats")
                    for index in range(0,len(containers),1):
                        tableau.playingTime(containers, index)  


                elif re.search("all_stats_misc", str(tab)):
                    containers = tab.find_all("tr",id = "stats")
                    for index in range(0,len(containers),1):
                        tableau.miscellaneousStats(containers,index)
        except IndexError:
            errorGene.append(url)
            continue
        
        
        #Récupération des données dans un dataframe
        dfJoueur = pd.DataFrame(
            {"joueur":nomJoueur,
            'Annees' : annees,
            'Ages' : ages,
            'Clubs' : clubs,
            'Ligues' : ligues,
            'Matchs Played' : matchsPlayed, 
            'Matchs Begin' : matchsBegin,
            'Minutes Played' : minutesPlayed,
            'Yellow Cards' : yellowCards,
            'Red Cards' : redCards,
            'Goals' : goals,
            'Decisives Passes' : decisivePasses,
            'Non Penalty Goals' : nonPenaltyGoals,
            'Penalty Goals' : penaltyGoals,
            'Penalty Attempteds' : penaltyAttempteds,
            'Shoots Total' : shotsTotal,
            "Shoots On Target" : shotsOnTarget,
            "Distance" : distance,
            "Free Shoots": freeShots,
            "Passes Completed" : passesCompleted,
            "Passes Attempted" : passesAttempted,
            "Total Distance (in yards)": totalDistance,
            "Passes Completed in short range (5 - 15yards)" : passesCompletedShort,
            "Passes Attempted in short range (5 - 15yards)" : passesAttemptedShort,
            "Passes Completed in medium range (15 - 30yards)" : passesCompletedMedium,
            "Passes Completed in medium range (15 - 30yards)" : passesAttemptedMedium,
            "Passes Completed in long range (30 + yards)" : passesCompletedLong,
            "Passes Completed in long range (30 + yards)" : passesAttemptedLong,
            "Passes that directly to shot" : passesLeadShots,
            "Completed passes that enter the 1-3 of the pitch": oneTierPitch,
            "Completed passes into the 18yard box" : passesCompleted18Yard,
            "Completed crosses into the 18yard box":crossCompletedt18yard,
            "Prog":Prog,
            "Live-Ball passes":livePasses,
            "Dead-ball passes":deadPasses,
            "Passes Attempted from free kicks":passesAttemptedFreeKick,
            "Completed passes back to defenders":completedPassesBackDefenders,
            "Passes made under opponent's pressure":passesUnderPressure,
            "Passes which travel more than 40yards":passesMore40Yards,
            "Crosses":crosses,
            "Corner kicks":cornerKicks,
            "Corner kicks In":cornerKickIn,
            "Corner kicks out":cornerKickOut,
            "Corner kicks straight":cornerKickStraight,
            "Grouds passes":groundPasses,
            "Low Passes":lowPasses,
            "High Passes":highPasses,
            "Passes from left foot":leftFootPasses,
            "Passes from right foot":rightFootPasses,
            "Passes from head":headPasses,
            "Throw in":throwIn,
            "Passes from an othen part":otherPasses,
            "Offsides passes":offsidesPasses,
            "Out of bounds passes":outBoundPasses,
            "Intercepted passes":interceptedPasses,
            "Blocked passes":blockedPasses,
            "SCA" : SCA,
            "Passes Live lead to a shot attempted": passesLiveLeadShotAttempted,
            "Passes Dead lead to a shot attempted": passesDeadLeadShotAttempted,
            "Dribble lead to a shot attempted": dribleLeadShotAttempted,
            "Shot lead to a shot attempted":shotLeadShotAttempted,
            "Foul draw lead to a shot attempted":foulDrawLeadShotAttempted,
            "Defensive moove lead to a shot attempted":defenseLeadShotAttempted,
            "GCA" : GCA,
            "Passes Live lead to a goal": passesLiveLeadGoal,
            "Passes Dead lead to a goal": passesDeadLeadGoal,
            "Dribble lead to a goal": dribleLeadGoal,
            "Shot lead to a goal":shotLeadGoal,
            "Foul draw lead to a goal":foulDrawLeadGoal,
            "Defensive moove lead to a goal":defenseLeadGoal,
            "Number of tackles":trkl,
            "Number of tackles which win possession of ball": trklW,
            "Tackles in 1/3 defensive part":def3Rd,
            "Tackles in 1/3 middle part":mid3Rd,
            "Tackled in 1/3 offensive part": att3Rd,
            "Number of dribblers tackled":trklDribble,
            "Number of times dribbles past by an opposing player":pastDribble,
            "Pressure which impose to release ball": pressures,
            "Pressure which won the ball":pressuresSucceded,
            "Pressure in 1/3 defensive part": pressuresDef3Rd,
            "Pressure in 1/3 mid part": pressuresMid3Rd,
            "Pressure in 1/3 offensive part":pressuresAtt3Rd,
            "Number of times blocking the ball": defPassesBlocked,
            "Number of shot blocked":defShotBlocked,
            "Number of shot on target blocked":defShotTargetBlocked,
            "Interceptions":Interceptions,
            "Clearances":clearances,
            "Error leadind to opponent's shot":errorLeadShot,
            "Number of touche":    touches,
            "Touches in defensive penalty area"    :touchesDefPenArea,
            "Touches in 1/3 defensive part"   :touchesDef3Rd,
            "Touches in 1/3 middle part"    :touchesMid3Rd,
            "Touches in 1/3 offensive part"    :touchesAtt3Rd,
            "Touches in offensive penalty area"    :touchesAttPenArea,
            "Touches on living ball"    :touchesLive,
            "Dribble succeed"    :dribbleSucceed,
            "Dribble attempted"   :dribbleAttempted,
            "Number of player dribbled"    :numberPlayerDribbled,
            "Number of player passing with ball throught leg's"    :dribbleThroughtlegs,
            "Number of time player control the ball"    :carriesFeet,
            "Distance (in yard) player moove the ball"    :distanceControlBall,
            "Distance (in yard) player moove the ball in penalty area"    :distanceControlOpponentGoal,
            "Distance (in yard) player moove the ball closest to the goal"    :carriesCloseGoal,
            "Number of times a player failed to gain ball":keepAgainstPlayer,
            "Number of targetting passes"    :targetPasses,
            "Number of receiving passes"    :receivedPasses,
            "Complete matches played":completedMatchPlayed,
            "Average points earned by the team while on match":averagePointEarnedTeam,
            "Ong" : onG,
            "Double Yellow Card":doubleYellowCard,
            "Fouls comitted":foulsCommited,
            "Fouls drawn":foulsDrawn,
            "Offsides":offsides,
            "Penalty concedeed" : penaltyConceded,
            "Own  goal":ownGoal,
            "Number of loose ball recovered":recoveredBall,
            "Arerials duel won":aerialWon,
            "Aerial duel loose":aerialLoose
        })

        result = pd.concat([result, dfJoueur])

        if indice == 20:
            break
    
        return result



informationGeneral = main()


# %%
