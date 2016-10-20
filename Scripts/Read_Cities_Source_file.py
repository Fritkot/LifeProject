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
        liste       : ['Barcelona', 'Belgrade','Istanbul']
    """
    
    import csv
    
    #set current working directory
    # from sys import path
    # from os import chdir
    # import csv
    # 
    # chdir(path[0])
    
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


def selectionAleaVille(villes,nbVille=0,graine=0):
    """
    Selectionne aleatoirement et uniformément un certain nombre de ville dans une liste de ville.
    
    La graine du generateur de nombre pseudo-aleatoire n'est pas fixe. 
    
    Parametres :
        villes  : la liste des villes parmis lesquelles la selection est realisee.
            type : list
            
        nbVille : le nombre de ville a selectionner, par default toutes les villes sont selectionnees.
            type : int
        graine : la graine du generateur de nombre pseudo-aleatoire. La graine est par defaut fixee sur l'horloge du processeur. Si on veut la fixer (pour des tests par exemple), il faut indiquer une graine.
            type : float/int/long
    
    return : la liste des villes selectionnees au hasard
        type : list
        
    
    """
    if nbVille > len(villes):
        raise(InputError('Le nombre de ville a selectionner ne peut exceder le nombre de ville dans la liste de ville a selectionner'))
    
    if (nbVille == 0) or (nbVille == len(villes)):
        return villes
    
    if nbVille < 0:
        raise InputError('Le nombre de ville a selectionner ne peut etre negatif.')
    
    from random import sample
    from random import seed
    
    if graine != 0:
        seed(graine)
    
    return sample(villes,nbVille)

def extraitSousGraphe(graphe,listVilles):
    """
    extrait un sous-graphe a partir de graphe correspondant a la listVille
    
    Parametres:
        graphe : un dictionnaire qui represente un graphe.
            type : dictionnaire
        listVille : la liste des villes a extraire
            type : list
        return : graphe correspondant a la liste en parametres
            type : dictionnaire
    """
    
    sousGraphe = dict()
    
    for v1 in listVilles:
        for v2 in listVilles:
            if v1 != v2:
                villesTriees = triePlusPetiteVille(v1,v2)
                if not(villesTriees in sousGraphe.keys()):
                    sousGraphe[villesTriees] = graphe[villesTriees]
    
    return sousGraphe
