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

acm=kruskall(graph)