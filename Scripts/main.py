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
#fichier = '../Inputs/GrapheTestProf.csv'
fichier = '../Inputs/GrapheInegTriang.csv'

matriceAdjacence,listVilles = importDonnéesSources(fichier)

#test si la matrice d'adjacence est symétrique
estSymetrique = testEstSymetrique(matriceAdjacence, listVilles)
if estSymetrique == False:
    raise Exception("Le graphe importée par matrice d'adjacence n'est pas symétrique")

#construit le graphe
graphe = creerGrapheDepuisMatriceAdjacence(matriceAdjacence,listVilles)

#selection ville de depart
villeDeDepart = listVilles[0]

#test si le graphe est complet
estComplet = testEstGrapheComplet(graphe)
if estComplet == False:
    raise Exception("Le graphe importé n'est pas complet")

#test si le 
#test si le graphe respecte l'inegalite triangulaire
respecteInegalite = testInegaliteTriangulaire(graphe)
if respecteInegalite == False:
    raise Exception("Le graphe complet ne respecte pas l'inégalite triangulaire.")


# #séléction aléatoire d'un certain nombre de ville
# nbVilles = 0 #on séléctionne toutes les villes
# graine = 1 #on fige la graine pour toujours avoir la même séquence de nb pseudo-aléatoire dans le cadre de tests du code
# villes = selectionAleaVille(listVilles, nbVilles,graine)

## Algorithme donnant un chemin au pire 2*distance de l'arbre couvrant minimum
# Calcul de l'arbre couvrant minimum

acm = kruskall(graphe)
    
# Parcours en profondeur préfixe de l'arbre couvrant minimum
cheminDuVoyageur = parcoursEnProfondeur(acm, villeDeDepart)
    
# Retour à la ville de départ du voyageur
cheminDuVoyageur.append(villeDeDepart)
    
# Calcul de la distance
distanceParcourue = 0
for i in range(len(cheminDuVoyageur)-1):
    distanceParcourue += graphe[creerArete(cheminDuVoyageur[i],cheminDuVoyageur[i+1])]
    
# Affichage des résultats
print(cheminDuVoyageur)
print(distanceParcourue)

print(acm)
## algorithme de Kristofides
#1)  Calculer un arbre couvrant de poids minimum : acm
acm = kruskall(graphe)

#2) Calculer l'ensemble I des noeuds de degres impairs de acm
noeudsImpairs =  selectionNoeudsParite(acm,False) #False car on regrade uniquement les noeuds impairs

#3) calculer le graphe induit par I a partir de graphe
grapheInduit = extraireSousGraphe(graphe,noeudsImpairs)

oo = estGrapheBiparti(grapheInduit)
print(oo)
#TODO: calculer couplage parfait de poids minimum
#TODO: Union de acm et du couplage
#TODO: calculer le tour eulerien
#TODO: en deduire le chemin Hamiltonien