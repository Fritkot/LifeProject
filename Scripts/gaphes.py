"""
Ce script va contenir toutes les methodes relatives aux graphes:
    - Union-Find
    - Kruskal
    - ...
"""

def trieGraphe(graphe,ascendant=True):
    """
        trie un graphe par valeur ascendante (par defaut) ou descendante des poids des arrêtes.
        
        parametres:
            gaphe : un graphe sous forme de dictionnaire avec un couple de ville comme clef
                type: dictionnaire
            ascendant : indique si le trie est ascendant ou descendant
                type : booleen
        return : graph trie
            type : list
            
        ex:
        graphe = {('Berlin', 'Brussels'): 651.62, ('Brussels', 'Hamburg'): 489.76, ('Bucharest', 'Hamburg'): 1544.17, ('Brussels', 'Bucharest'): 1769.69, ('Berlin', 'Rome'): 1181.67, ('Berlin', 'Hamburg'): 254.51, ('Berlin', 'Bucharest'): 1293.4, ('Bucharest', 'Rome'): 1137.38, ('Hamburg', 'Rome'): 1307.51, ('Brussels', 'Rome'): 1171.34}
        trieGraph(graphe) = [(('Berlin', 'Hamburg'), 254.51), (('Brussels', 'Hamburg'), 489.76), (('Berlin', 'Brussels'), 651.62), (('Bucharest', 'Rome'), 1137.38), (('Brussels', 'Rome'), 1171.34), (('Berlin', 'Rome'), 1181.67), (('Berlin', 'Bucharest'), 1293.4), (('Hamburg', 'Rome'), 1307.51), (('Bucharest', 'Hamburg'), 1544.17), (('Brussels', 'Bucharest'), 1769.69)]
    """
    
    from operator import itemgetter
    
    clefs = graphe.items()
    clefsTriees = sorted(clefs , key = itemgetter(1),reverse=not(ascendant))
    return clefsTriees


def creerForetVierge(arretes):
    """
    creer une foret a partir de la liste des arbres.
    Une arrete correspondant a un couple d'arbre (ou de ville)
    
    parametre :
        arretes: liste des arretes (ie tuple de ville)
            type liste
    return : un dictionnaire avec comme clef l'arbre ou ville et comme element son rang initialise a 0
        type : dictionnaire
    """
    
    foret = dict()
    
    for arbre in arretes:
        origine = arbre[0]
        destination = arbre[1]
        if origine in foret.keys():
            foret[origine]=0
        if destination in foret.keys():
            foret[destination] = 0
    
    return foret
  

def unionFind():
    