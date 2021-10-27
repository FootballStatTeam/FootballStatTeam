from fonctionnel import recupData
import re

# Déclaration des listes contenant les statistiques
# Initialisation des listes
nbAnnee = 0
url = ""
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


# On commence par le tableau : Standard Stats: Domestic Leagues.
#     * Annnees
#     * Ages
#     * Clubs
#     * Ligues
#     * Match joués
#     * Matchs commencés
#     * Goals
#     * Passes décisives
#     * Buts (hors pénalty)
#     * Pénalty marqués
#     * Pénalty tentées
#     * Carton jaune
#     * Carton rouge

def standartStats(containers, index):
    indice = index
    line = containers[index].find_all("td")
    
    annees[indice] = containers[index].find("th", class_ = "left").text
    ages[indice] = containers[index].find("td", class_ = "center").text
    clubs[indice] = containers[index].find("td", class_ = "left").text
    # ligues[indice] = containers[index].find_all("a")[3].text
    
    matchsPlayed[indice] = recupData(str(line), "games")
    matchsBegin[indice] = recupData(str(line), "games_starts")
    minutesPlayed[indice] = recupData(str(line), "minutes")
    goals[indice] = recupData(str(line), "goals")
    decisivePasses[indice] = recupData(str(line), "assists")
    nonPenaltyGoals[indice] = recupData(str(line), "goals_pens")
    penaltyGoals[indice] = recupData(str(line), "pens_made")
    penaltyAttempteds[indice] = recupData(str(line), "pens_att")
    yellowCards[indice] = recupData(str(line), "cards_yellow")
    redCards[indice] = recupData(str(line), "cards_red")

# Ici on s'occupe du deuxième tableau : Shooting
#     * Nombre de tir total
#     * Nombre de tir cadré
#     * Distance moyenne des tirs (en yard)
#     * Tir libre (Opposé de coup de pied arrété)

def shooting(containers, index):
    line = containers[index].find_all("td")
    indice = index

    shotsTotal[indice] = recupData(str(line), "shots_total")
    shotsOnTarget[indice] = recupData(str(line), "shots_on_target")
    distance[indice] = recupData(str(line), "average_shot_distance")
    freeShots[indice] = recupData(str(line), "shots_free_kicks")


# Troisième tableau : Passing
#     * Passes réussies
#     * Passes tentées
#     * Distance total des passes (en yards)
#     * Passes réussies (entre 5 et 15 yards)
#     * Passes tentées (entre 5 et 15 yards)
#     * Passes réussies (entre 15 et 30 yards)
#     * Passes tentées (entre 15 et 30 yards)
#     * Passes réussies (plus de 30 yards)
#     * Passes tentées (plus de 30 yards)
#     * Passes réussis dans le terrain adverse
#     * Passes réussis dans les 18 yards adverse
#     * Passes tentées dans les 18 yards adverse
#     * Passes réussies devant le but adverse

def passing(containers, index):
    line = containers[index].find_all("td")
    indice = index
    
    passesCompleted[indice] = recupData(str(line), "passes_completed")
    passesAttempted[indice] = recupData(str(line), "passes")
    totalDistance[indice] = recupData(str(line), "passes_total_distance")
    passesCompletedShort[indice] = recupData(str(line), "passes_completed_short")
    passesAttemptedShort[indice] = recupData(str(line), "passes_short")
    passesCompletedMedium[indice] = recupData(str(line), "passes_completed_medium")
    passesAttemptedMedium[indice] = recupData(str(line), "passes_medium")
    passesCompletedLong[indice] = recupData(str(line), "passes_completed_long")
    passesAttemptedLong[indice] = recupData(str(line), "passes_long")
    passesLeadShots[indice] = recupData(str(line), "assisted_shots")
    oneTierPitch[indice] = recupData(str(line), "passes_into_final_third")
    passesCompleted18Yard[indice] = recupData(str(line), "passes_into_penalty_area")
    crossCompletedt18yard[indice] = recupData(str(line), "crosses_into_penalty_area")
    Prog[indice] = recupData(str(line), "progressive_passes")


# Quatrième tableau : Pass Types
#     * Passes directes
#     * Passes coup de pied arrété
#     * Passes en coup francs
#     * Passes réussis dérrière les defenseurs
#     * Passes sous pressions
#     * Passes trés longue (plus 40 yards)
#     * Traversées de terrain
#     * Corners (Passes + tir)
#     * Corners (effet intérieur)
#     * Corners (effet extérieur)
#     * Corners (sans effet)
#     * Passes proche du sol
#     * Passes en hauteur
#     * Passes (pied gauche)
#     * Passes (pied droit)
#     * Passes (Tête)
#     * Touches
#     * Autres type de passes
#     * Passes en dehors des limites
#     * Passes interceptées
#     * Passes blockées par un adversaire

def passTypes(containers, index):
    line = containers[index].find_all("td")
    indice = index

    livePasses[indice] = recupData(str(line), "passes_live")
    deadPasses[indice] = recupData(str(line), "passes_dead")
    passesAttemptedFreeKick[indice] = recupData(str(line), "passes_free_kicks")
    completedPassesBackDefenders[indice] = recupData(str(line), "through_balls")
    passesUnderPressure[indice] = recupData(str(line), "passes_pressure")
    passesMore40Yards[indice] = recupData(str(line), "passes_switches")
    crosses[indice] = recupData(str(line), "crosses")
    cornerKicks[indice] = recupData(str(line), "corner_kicks")
    cornerKickIn[indice] = recupData(str(line), "corner_kicks_in")
    cornerKickOut[indice] = recupData(str(line), "corner_kicks_out")
    cornerKickStraight[indice] = recupData(str(line), "corner_kicks_straight")
    groundPasses[indice] = recupData(str(line), "passes_ground")
    lowPasses[indice] = recupData(str(line), "passes_low")
    highPasses[indice] = recupData(str(line), "passes_high")
    leftFootPasses[indice] = recupData(str(line), "passes_left_foot")
    rightFootPasses[indice] = recupData(str(line), "passes_right_foot")
    headPasses[indice] = recupData(str(line), "passes_head")
    throwIn[indice] = recupData(str(line), "throw_ins")
    otherPasses[indice] = recupData(str(line), "passes_other_body")
    offsidesPasses[indice] = recupData(str(line), "passes_offsides")
    outBoundPasses[indice] = recupData(str(line), "passes_oob")
    interceptedPasses[indice] = recupData(str(line), "passes_intercepted")
    blockedPasses[indice] = recupData(str(line), "passes_blocked")


# Cinquième tableau : Goal and Shot Creation
#     * Tir créant une action
#     * Passes directes menant à un tir
#     * Passes coup de pied arrétées menant à un tir 
#     * Dribles menant à un tir
#     * Fautes récupérées menant à un tir
#     * Action defensive menant à un tir
#     * Tir créant un but
#     * Passes directes menant à un but
#     * Passes coup de pied arrétées menant à un but 
#     * Dribles menant à un but
#     * Fautes récupérées menant à un but
#     * Action defensive menant à un but

def goalShotCreation(containers, index):
    line = containers[index].find_all("td")
    indice = index

    SCA[indice] = recupData(str(line), "sca")
    passesLiveLeadShotAttempted[indice] = recupData(str(line), "sca_passes_live")
    passesDeadLeadShotAttempted[indice] = recupData(str(line), "sca_passes_dead")
    dribleLeadShotAttempted[indice] = recupData(str(line), "sca_dribbles")
    shotLeadShotAttempted[indice] = recupData(str(line), "sca_shots")
    foulDrawLeadShotAttempted[indice] = recupData(str(line), "sca_fouled")
    defenseLeadShotAttempted[indice] = recupData(str(line), "sca_defense")
    GCA[indice] = recupData(str(line), "gca")
    passesLiveLeadGoal[indice] = recupData(str(line), "gca_passes_live")
    passesDeadLeadGoal[indice] = recupData(str(line), "gca_passes_dead")
    dribleLeadGoal[indice] = recupData(str(line), "gca_dribbles")
    shotLeadGoal[indice] = recupData(str(line), "gca_shots")
    foulDrawLeadGoal[indice] = recupData(str(line), "gca_fouled")
    defenseLeadGoal[indice] = recupData(str(line), "gca_defense")


# Sixième tableau : Defensive Actions
#     * Tackles
#     * Tackles récupérant la balle
#     * Tackles en défenses
#     * Tackles en milieu de terrain
#     * Tackles en attaques
#     * Tackles sur un joueur driblant
#     * Driblé par un joueur adverse
#     * Applique pression sur un joueur
#     * Applique pression sur un joueur et recupère la balle
#     * Applique pression defensive
#     * Applique pression milieu de terrain
#     * Applique pression offensive
#     * Block d'une passe
#     * Block un tir
#     * Block un tir cadré
#     * Interception 
#     * Dégagement
#     * Erreur menant à un but adverse

def defensiveActions(containers, index):
    line = containers[index].find_all("td")
    indice = index

    trkl[indice] = recupData(str(line), "tackles")
    trklW[indice] = recupData(str(line), "tackles_won")
    def3Rd[indice] = recupData(str(line), "tackles_def_3rd")
    mid3Rd[indice] = recupData(str(line), "tackles_mid_3rd")
    att3Rd[indice] = recupData(str(line), "tackles_att_3rd")
    trklDribble[indice] = recupData(str(line), "dribble_tackles")
    pastDribble[indice] = recupData(str(line), "dribbled_past")
    pressures[indice] = recupData(str(line), "pressures")
    pressuresSucceded[indice] = recupData(str(line), "pressure_regains")
    pressuresDef3Rd[indice] = recupData(str(line), "pressures_def_3rd")
    pressuresMid3Rd[indice] = recupData(str(line), "pressures_mid_3rd")
    pressuresAtt3Rd[indice] = recupData(str(line), "pressures_att_3rd")
    defPassesBlocked[indice] = recupData(str(line), "blocks")
    defShotBlocked[indice] = recupData(str(line), "blocked_shots")
    defShotTargetBlocked[indice] = recupData(str(line), "blocked_shots_saves")
    Interceptions[indice] = recupData(str(line), "interceptions")
    clearances[indice] = recupData(str(line), "clearances")
    errorLeadShot[indice] = recupData(str(line), "errors")


# Septième tableau : Possession
#     * Touches
#     * Touches dans la zone de pénalty defensive
#     * Touches en defenses
#     * Touches en milieu de terrain
#     * Touches en attaques
#     * Touches dans la zone de pénalty offensive
#     * Touches balles vivantes
#     * Dribles réussis
#     * Dribles essayés
#     * Nombre de joueur driblé
#     * Nombre de fois ou le joueur controlle la ball avec ses pied
#     * Distance parcourrut en controlant la balle
#     * Distance parcourrut en controlant la balle en attaque
#     * Distance parcourrut en controlant la balle devant le but adverse
#     * Nombre de joueur ratant la prise de balle
#     * Nombre de fois visé par une passe
#     * Nombre de fois recevant une passe

def possession(containers,index):
    line = containers[index].find_all("td")
    indice = index

    touches[indice] = recupData(str(line), "touches")
    touchesDefPenArea[indice] = recupData(str(line), "touches_def_pen_area")
    touchesDef3Rd[indice] = recupData(str(line), "touches_def_3rd")
    touchesMid3Rd[indice] = recupData(str(line), "touches_mid_3rd")
    touchesAtt3Rd[indice] = recupData(str(line), "touches_att_3rd")
    touchesAttPenArea[indice] = recupData(str(line), "touches_att_pen_area")
    touchesLive[indice] = recupData(str(line), "touches_live_ball")
    dribbleSucceed[indice] = recupData(str(line), "dribbles_completed")
    dribbleAttempted[indice] = recupData(str(line), "dribbles")
    numberPlayerDribbled[indice] = recupData(str(line), "players_dribbled_past")
    dribbleThroughtlegs[indice] = recupData(str(line), "nutmegs")
    carriesFeet[indice] = recupData(str(line), "carries")
    distanceControlBall[indice] = recupData(str(line), "carry_distance")
    distanceControlOpponentGoal[indice] =recupData(str(line), "carry_progressive_distance")
    carriesCloseGoal[indice] = recupData(str(line), "carries_into_final_third")
    keepAgainstPlayer[indice] = recupData(str(line), "miscontrols")
    targetPasses[indice] = recupData(str(line), "pass_targets")
    receivedPasses[indice] = recupData(str(line), "passes_received")


# Huitième tableau : Playing Time
#     * Match entièrement joué
#     * Nombre moyen de point gagné par l'équipe lorsqu'il joue
#     * But marqué par l'équipe lorsqu'il joue

def playingTime(containers, index):
    line = containers[index].find_all("td")
    indice = index

    completedMatchPlayed[indice] = recupData(str(line), "games_complete")
    averagePointEarnedTeam[indice] = recupData(str(line), "points_per_match")
    onG[indice] = recupData(str(line), "on_goals_for")


# Neuvième et dernier tableau : Miscellaneous Stats
#     * Double cartons jaunes
#     * Fautes faites
#     * Fautes offertes
#     * Hors limites
#     * Penalty offert
#     * But contre son camp
#     * Balle perdu puis récupérée
#     * Duel aérien gagné
#     * Duel aérien perdu

def miscellaneousStats(containers, index):

    line = containers[index].find_all("td")
    indice = index

    doubleYellowCard[indice] = recupData(str(line), "cards_yellow_red")
    foulsCommited[indice] = recupData(str(line), "fouls")
    foulsDrawn[indice] = recupData(str(line), "fouled")
    offsides[indice] = recupData(str(line), "offsides")
    penaltyConceded[indice] = recupData(str(line), "pens_conceded")
    ownGoal[indice] = recupData(str(line), "own_goals")
    recoveredBall[indice] = recupData(str(line), "ball_recoveries")
    aerialWon[indice] = recupData(str(line), "aerials_won")
    aerialLoose[indice] = recupData(str(line), "aerials_lost")