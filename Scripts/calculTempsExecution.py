##changement du workingdirectory
from sys import path
from os import chdir


#chdir(path[1])
chdir(path[0])

##import des scripts
from Read_Cities_Source_file import *
from graphes import *

#C:\Users\Joe\Documents\GitHub\LifeProject\Scripts\Read_Cities_Source_file.py

## Chargement des données sources
#fichier = '../Inputs/Distances.csv'
#fichier = '../Inputs/GrapheTestProf.csv'
#fichier = '../Inputs/GrapheInegTriang.csv'
# fichier = '../Inputs/Villes Europe.csv'
fichier = '../Inputs/LargeDataSet.csv'
# fichier = '../Inputs/MiddleDataSet.csv'


matriceAdjacence,listVilles = importDonnéesSources(fichier)
estSymetrique = testEstSymetrique(matriceAdjacence, listVilles)
if estSymetrique == False:
    raise Exception("Le graphe importée par matrice d'adjacence n'est pas symétrique")
    
estComplet = testEstGrapheComplet(graphe)
if estComplet == False:
    raise Exception("Le graphe importé n'est pas complet")

#test si le graphe respecte l'inegalite triangulaire
respecteInegalite = testInegaliteTriangulaire(graphe)
if respecteInegalite == False:
    raise Exception("Le graphe complet ne respecte pas l'inégalite triangulaire.")


villeDeDepart = listVilles[0]
from datetime import datetime
import time
import csv
file  =open("MONFICHIER.csv", "w")
c = csv.writer(file, delimiter=';', lineterminator='\n')

#séléction aléatoire d'un certain nombre de ville
for j in range(4,len(listVilles)+1):

    # start_time = datetime.now()
    start_time = time.clock()
    nbVilles =j #on séléctionne toutes les villes
    graine = 1 #on fige la graine pour toujours avoir la même séquence de nb pseudo-aléatoire dans le cadre de tests du code
    villes = selectionAleaVille(listVilles, nbVilles,graine)
    villeDeDepart = villes[0]
    ## Construction et tests sur le graphe
    # Construction du graphe
    graphe = creerGrapheDepuisMatriceAdjacence(matriceAdjacence,villes)
    
    ## Algorithme donnant un chemin au pire 2*distance de l'arbre couvrant minimum
    # Calcul de l'arbre couvrant minimum
    acm = kruskall(graphe)
    
    #print(acm)
    
    # Parcours en profondeur préfixe de l'arbre couvrant minimum
    cheminDuVoyageur = parcoursEnProfondeur(acm, villeDeDepart)
    #     
    # # Retour à la ville de départ du voyageur
    cheminDuVoyageur.append(villeDeDepart)
    #     
    # # # Calcul de la distance
    distanceParcourue = 0
    for i in range(len(cheminDuVoyageur)-1):
        distanceParcourue +=    graphe[creerArete(cheminDuVoyageur[i],cheminDuVoyageur[i+1])]
    
    # Affichage des résultats
    #print(cheminDuVoyageur)
    #print(distanceParcourue)
    #print(trieGraphe(acm))
        
    # # 2) Calculer l'ensemble I des noeuds de degres impairs del' acm
    # noeudsImpairs =  selectionNoeudsParite(acm,False) #False car on regrade uniquement les noeuds impairs
    # 
    # # 3) calculer le graphe induit par I a partir de graphe
    # grapheInduit = extraireSousGraphe(graphe,noeudsImpairs)
    # 
    # # 4) calculer le couplage parfait de poids minimum
    # couplage = couplageNaif(grapheInduit)
    # 
    # # 5) Union du couplage et de l'arbre couvrant de poids minimum
    # grapheUni = unionDeuxGraphes(acm,couplage)
    # 
    # # 6) Calculer un tour eulérien
    # cycleEulerien = calculerCheminEulerien(grapheUni)
    # 
    # # 7) calculer un cycle hamiltonien
    # cycleHamiltonien = calculerCycleHamiltonien(cycleEulerien)
    # 
    # # 8) Construire le sous-graphe représentant le cycle Hamiltonien
    # grapheHamiltonien = extraireGrapheDepuisListeArete(graphe,cycleHamiltonien)
    # 
    # # Calcul de la distance parcourus
    # distanceParcourue = 0
    # for arete in grapheHamiltonien:
    #     distanceParcourue += grapheHamiltonien[arete]
        
    
    
    end_time = datetime.now()
    print(j," noeuds",time.clock() - start_time, "seconds",distanceParcourue)
    # print('Duration: {}'.format(end_time - start_time))
    c.writerow([str(j)+" villes",time.clock() - start_time,"distance",distanceParcourue])
# c.close()
file.close()

## algorithme de Kristofides

#1)  Calculer un arbre couvrant de poids minimum : acm
acm = kruskall(graphe)

#2) Calculer l'ensemble I des noeuds de degres impairs del' acm
noeudsImpairs =  selectionNoeudsParite(acm,False) #False car on regrade uniquement les noeuds impairs

#3) calculer le graphe induit par I a partir de graphe
grapheInduit = extraireSousGraphe(graphe,noeudsImpairs)

#4) calculer le couplage parfait de poids minimum
couplage = couplageNaif(grapheInduit)

#5) Union du couplage et de l'arbre couvrant de poids minimum
grapheUni = unionDeuxGraphes(acm,couplage)

#6) Calculer un tour eulérien
cycleEulerien = calculerCheminEulerien(grapheUni)

#7) calculer un cycle hamiltonien
cycleHamiltonien = calculerCycleHamiltonien(cycleEulerien)

#8) Construire le sous-graphe représentant le cycle Hamiltonien
grapheHamiltonien = extraireGrapheDepuisListeArete(graphe,cycleHamiltonien)

#Calcul de la distance parcourus
distance = 0
for arete in grapheHamiltonien:
    distance += grapheHamiltonien[arete]
print("distance : ",distance)
print(cycleHamiltonien)


## affichage des résultats
afficherResultat(cheminDuVoyageur,"Simplifié "+str(distanceParcourue)+"km ",cycleHamiltonien,"Christofides "+str(distance)+"km")
