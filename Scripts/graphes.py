"""
Ce script va contenir toutes les methodes relatives aux graphes:
    - trie des arretes
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

def extraitListNoeuds(graphe):
    """
    extrait la liste des noeuds du graphes passé en parametre
    
    parametre :
        - graphe : graphe représenté par un dictionnaire avec un couple de ville (noeuds) comme clefs
            type : dictionnaire
    return : la liste des noeuds (villes) du graphes
        type : list
    
    ex:
        - graphe = {('Brussels', 'Rome'): 1171.34, ('Bucharest', 'Hamburg'): 1544.17, ('Brussels', 'Bucharest'): 1769.69, ('Berlin', 'Hamburg'): 254.51, ('Hamburg', 'Rome'): 1307.51, ('Bucharest', 'Rome'): 1137.38, ('Berlin', 'Bucharest'): 1293.4, ('Brussels', 'Hamburg'): 489.76, ('Berlin', 'Brussels'): 651.62, ('Berlin', 'Rome'): 1181.67}
        - extraitListNoeuds(graphe) => ['Brussels', 'Rome', 'Bucharest', 'Hamburg', 'Berlin']
    
    """
    liste = list()
    
    for arbre in graphe.keys():
        origine = arbre[0]
        destination = arbre[1]
        if not(origine in liste):
            liste.append(origine)
        if not(destination in liste):
            liste.append(destination)
    
    return liste



def creerForetVierge(listeArbres):
    """
    creer une foret a partir de la liste des arbres ou noeuds d'un graphe.
    
    parametre :
        listeArbres: liste des arbres (ie noeuds du graphe : nom de ville)
            type list
    return : un dictionnaire avec comme clef l'arbre ou ville et comme elements un couple compose de son pere et de son rang initialise a 0 (tableau à 2 elements)
        type : dictionnaire
        
    ex:
        - villes = ['Bucharest', 'Rome', 'Berlin', 'Hamburg', 'Brussels']
        - creerForetVierge(villes) => {'Brussels': ('Brussels', 0), 'Hamburg': ('Hamburg', 0), 'Berlin': ('Berlin', 0), 'Rome': ('Rome', 0), 'Bucharest': ('Bucharest', 0)}
    """
    
    foret = dict()
    
    for arbre in listeArbres:
        if not(arbre in foret.keys()):
            foret[arbre]=[arbre,0]
    
    return foret
  
def find(arbre,foret):
    """
    cherche le parent de l'arbre
    
    parametres :
        - arbre : l'arbre dont on cherche son aieul
            type : string
        - foret : l'ensemble des arbres avec leurs aieux respectifs
            type : dictionnaire
    return : [pere,rang] de l'arbre
        type : tableau a 2 elements
        
    ex:
    - foret = {'Bucharest': ('Bucharest', 0), 'Brussels': ('Rome', 0), 'Rome': ('Hamburg', 0), 'Hamburg': ('Hamburg', 0), 'Berlin': ('Berlin', 0)}
    - find('Brussels',foret) => ('Hamburg', 0)
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
            foret[arbre1] = [pereArbre2[0],pereArbre1[1]] #sinon quand foret[arbre1] est maj, foret[arbre2] l'est aussi. Les variables sont passées par référence en Python et non par valeur
        else:
            foret[arbre2] = [pereArbre1[0],pereArbre2[1]]
            if pereArbre1[1] == pereArbre2[1]:
                foret[arbre1][1] += 1
                
    return foret