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
        trieGraph(graphe) => [(('Berlin', 'Hamburg'), 254.51), (('Brussels', 'Hamburg'), 489.76), (('Berlin', 'Brussels'), 651.62), (('Bucharest', 'Rome'), 1137.38), (('Brussels', 'Rome'), 1171.34), (('Berlin', 'Rome'), 1181.67), (('Berlin', 'Bucharest'), 1293.4), (('Hamburg', 'Rome'), 1307.51), (('Bucharest', 'Hamburg'), 1544.17), (('Brussels', 'Bucharest'), 1769.69)]
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
    return : un dictionnaire avec comme clef l'arbre ou ville et comme elements un tuple compose de son pere et de son rang initialise a 0
        type : dictionnaire
        
    ex:
        - sousGraphe = {('Brussels', 'Rome'): 1171.34, ('Brussels', 'Bucharest'): 1769.69, ('Berlin', 'Bucharest'): 1293.4, ('Bucharest', 'Hamburg'): 1544.17, ('Berlin', 'Hamburg'): 254.51, ('Berlin', 'Rome'): 1181.67, ('Brussels', 'Hamburg'): 489.76, ('Hamburg', 'Rome'): 1307.51, ('Berlin', 'Brussels'): 651.62, ('Bucharest', 'Rome'): 1137.38}
        - creerForetVierge(sousGraphe) => {'Bucharest': ('Bucharest', 0), 'Brussels': ('Brussels', 0), 'Rome': ('Rome', 0), 'Hamburg': ('Hamburg', 0), 'Berlin': ('Berlin', 0)}
    """
    
    foret = dict()
    
    for arbre in arretes:
        origine = arbre[0]
        destination = arbre[1]
        if not(origine in foret.keys()):
            foret[origine]=(origine,0)
        if not(destination in foret.keys()):
            foret[destination] = (destination,0)
    
    return foret
  
def find(arbre,foret):
    """
    cherche le parent de l'arbre
    
    parametres :
        - arbre : l'arbre dont on cherche son aieul
            type : string
        - foret : l'ensemble des arbres avec leurs aieux respectifs
            type : dictionnaire
    return : (pere,rang) de l'arbre
        type : tuple
        
    ex:
    - foret = {'Bucharest': ('Bucharest', 0), 'Brussels': ('Rome', 0), 'Rome': ('Rome', 0), 'Hamburg': ('Hamburg', 0), 'Berlin': ('Berlin', 0)}
    - find('Brussels',foret) => ('Rome', 0)
    """
    
    if foret[arbre][0]==arbre:
        return foret[arbre]
    return find(foret[arbre][0],foret)
    
def union(arbre1,arbre2,foret):
    """
    
    """
    pereArbre1 = find(arbre1,foret)
    pereArbre2 = find(arbre2,foret)
    
    if pereArbre1[0] != pereArbre2[0]:
        if pereArbre1[1] < pereArbre2[1]:
            foret[pereArbre1] = pereArbre2
        else:
            foret[pereArbre2] = pereArbre1
            if pereArbre1[1] == pereArbre2[1]:
                foret[pereArbre1][1] = pereArbre1[1]+1
                
    return foret