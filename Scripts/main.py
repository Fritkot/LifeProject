##changement du workingdirectory
from sys import path
from os import chdir

chdir(path[0])

##import des scripts
from Read_Cities_Source_file import *
from graphes import *
#C:\Users\Joe\Documents\GitHub\LifeProject\Scripts\Read_Cities_Source_file.py


## script principal

#chargement de données sources des villes
#fichier = '../Inputs/Distances.csv'
fichier = '../Inputs/GrapheTestProf.csv'
graph,listVilles = importDonnéesSources(fichier)

# #séléction aléatoire d'un certain nombre de ville
# nbVilles = 0 #on séléctionne toutes les villes
# graine = 1 #on fige la graine pour toujours avoir la même séquence de nb pseudo-aléatoire dans le cadre de tests du code
# villes = selectionAleaVille(listVilles, nbVilles,graine)

## algorithme de Kristofides
#1)  Calculer un arbre couvrant de poids minimum : acm
acm = kruskall(graph)

#2) Calculer l'ensemble I des noeuds de degres impairs de acm
noeudsImpairs =  selectionNoeudsParite(acm,False) #False car on regrade uniquement les noeuds impairs

#3) calculer le graphe induit par I a partir de graphe
grapheInduit = extraireSousGraphe(graph,noeudsImpairs)

#TODO calculer couplage parfait de poids minimum
#TODO Union de acm et du couplage
#TODO calculer le tour eulerien
#TODO en deduire le chemin Hamiltonien