#!/usr/bin/python3.2

## lecture du fichier source

def importDonnéesSources(cheminFichier):
    """
    prend la matrice des distances en paramètre contenue dans un fichier csv
    
    paramètre :
        cheminFichier : chemin relatif vers le fichier csv, ex : '../Inputs/Distances.csv'
    return : deux éléments :
                1) un dictionnaire avec un couple de ville relié en clef avec la distance qui les sépare.
                2) un liste de toutes les villes considérées
    
    exemple :
        dictionnire : {('Barcelona', 'Belgrade'): 1528.13, ('Belgrade', 'Istanbul'): 809.48}
        liste       : ['Barcelona', 'Belgrade']
    """
    
    
    #set current working directory
    from sys import path
    from os import chdir
    import csv
    
    chdir(path[0])
    
    townMatrix = dict() #stores all the cities with the distance between the other cities
    townList = list()
    
    #open Distance file
    with open(cheminFichier,'r') as file:
        
        #crée un reader
        reader = csv.reader(file, delimiter=';')
        
        #first row is an header row which is not relevant for the moment
        isHeader = True 
        for row in reader:
            if isHeader:
                isHeader = False #skip the first row
            else:            
                town = row[0]
                townList.append(town)
                townMatrix[town] = [float(el) for el in row[1:]]
        file.close()

    # print(townMatrix)
    # print(townList)
    # print(townMatrix.keys())

    # graphe = dict() #dictionnaire avec un couple de ville comme clef
    # #construisons le graphe
    # for ligne in townMatrix.keys():
    #     for colonne in townMatrix.keys():
    #         graphe[(ligne,colonne)]=townMatrix[ligne][townList.index(colonne)]
    # print(graphe[(townList[0],townList[2])])

    graphe = dict() #dictionnaire avec un couple de ville comme clef
    #construisons le graphe
    for ligne in townMatrix.keys():
        for colonne in townMatrix.keys():
            
            distance = townMatrix[ligne][townList.index(colonne)]
            if distance <= 0 :
                break   # si distance = 0, la ville correspond à elle-même
                        # si distance < 0, il n'y a pas de liaison entre les deux villes
            
            graphe[triePlusPetiteVille(ligne,colonne)]=distance
    #print(graphe[triePlusPetiteVille(townList[0],townList[2])])
    return graphe,townList


def triePlusPetiteVille(ville1,ville2):
    """
    compare de maniere lexicographique le noms des deux villes
    
    Paramètres:
        ville1 : nom de la première ville
            type : string
        ville2 : nom de la deuxième ville
            type : string
    
    Return : un tuple avec la ville la plus petite d'un point de vu lexicographique en premier
        type : tuple de 2 strings
        
        
    exemple :
        >>> triePlusPetiteVille("Vienna","Brussels")
        ('Brussels', 'Vienna')
    """
    if ville1>ville2 :
        return (ville2,ville1)
    else:
        return (ville1,ville2)


## script principal

fichier = '../Inputs/Distances.csv'

graph,villes = importDonnéesSources(fichier)

