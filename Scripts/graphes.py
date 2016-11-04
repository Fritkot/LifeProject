## Méthodes relatives aux Graphes
"""
Cette section va contenir toutes les methodes relatives aux graphes:
    - trie des arretes
    - extraire la liste des noeuds à partir d'un graphe
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
            type : list (si on renvoit un ditionnaire, l'ordre des arretes n'est plus garantie)
            
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




## méthodes pour l'agorithme de l'Union-Find

def creerForetVierge(listeArbres):
    """
    creer une foret a partir de la liste des noeuds d'un graphe.
    
    parametre :
        listeSommets: liste des sommets (ie noeuds du graphe : nom de ville)
            type list
    return : un dictionnaire avec comme clef le sommet ou ville et comme elements un couple compose de son aieul et de son rang initialise a 1 (tableau à 2 elements)
        type : dictionnaire
        
    ex:
        - villes = ['Bucharest', 'Rome', 'Berlin', 'Hamburg', 'Brussels']
        - creerForetVierge(villes) => {'Brussels': ('Brussels', 1), 'Hamburg': ('Hamburg', 1), 'Berlin': ('Berlin', 1), 'Rome': ('Rome', 1), 'Bucharest': ('Bucharest', 1)}
    """
    
    foret = dict()
    
    for arbre in listeArbres:
        if not(arbre in foret.keys()):
            foret[arbre]=[arbre,1]
    
    return foret
  
def find(sommet,foret):
    """
    cherche l'ancetre du sommet
    
    parametres :
        - sommet : le sommet dont on cherche l'aieul
            type : string
        - foret : l'ensemble de sommets avec leurs aieux et leurs poids respectifs
            type : dictionnaire
    return : l'aieul du sommet
        type : string
        
    ex:
    - foret = {'Bucharest': ('Bucharest', 0), 'Brussels': ('Rome', 0), 'Rome': ('Hamburg', 0), 'Hamburg': ('Hamburg', 0), 'Berlin': ('Berlin', 0)}
    - find('Brussels',foret) => 'Hamburg'
    """
    
    if foret[sommet][0]==sommet:
        return foret[sommet][0]
    return find(foret[sommet][0],foret)
    
def union(sommet1,sommet2,foret):
    """
    fusionne deux sommets dans une foret.
    La fusion se déroule comme suit:
        on regarde l'aieul de chaque sommet:
            - si aieul(sommet1) == aieul(sommet2) 
                alors les arbres sont deja connectes dans la foret
            - sinon
                - on affecte le sommet avec l'aieul de rang le plus grand à l'autre sommet.
        
    """
    aieul1 = find(sommet1,foret)
    aieul2 = find(sommet2,foret)
    
    if aieul1 != aieul2: # test si les deux arbres ont des aieux differents
         #test les rangs des arbres aieux
        if foret[aieul1][1] < foret[aieul2][1]: # cas ou rang(sommet1) < rang(sommet2)
            
            foret[sommet1][0] = aieul2
            foret[aieul2][1] += foret[aieul1][1]
            
        else: # cas rang(sommet1) > rang(sommet2) ou les rangs sont egaux : foret[aieul1][1] == foret[aieul2][1]:
            foret[sommet2][0] = aieul1 # arbitrairement on selectionne le sommet1 comme aieul
            foret[aieul1][1] += foret[aieul2][1]
            
    return foret

## Algorithme d'arbre couvrant de poids minimum

def kruskall(graphe):
    """
    algorithme de Kruskall qui cherche un arbre couvrant de poids minimal qui suit le principe suivant :
        1) trier le graphe par ordre decroissant des poids des arretes
        2) prendre chaque arrete par ordre croissant suivant les critres:
            - si l'arrete a deja ete prise en compte, la rejeter
            - si la nouvelle arrete forme un cycle alors la rejeter
    l'algorithme utilise le principe de l'Union-Find.
    
    parametres :
        - graphe : graphe sur lequel on cherche un arbre couvrant de poids minimum
            type: dictionnaire
    
    return : arbre couvrant de poids minimum
        type : dictionnaire
    
    ex:
        graphe = {('Berlin', 'Bucharest'): 1293.4, ('Brussels', 'Bucharest'): 1769.69, ('Hamburg', 'Rome'): 1307.51, ('Bucharest', 'Rome'): 1137.38, ('Berlin', 'Rome'): 1181.67, ('Berlin', 'Hamburg'): 254.51, ('Brussels', 'Hamburg'): 489.76, ('Bucharest', 'Hamburg'): 1544.17, ('Brussels', 'Rome'): 1171.34, ('Berlin', 'Brussels'): 651.62}
        kruskall(graphe) = {('Berlin', 'Hamburg'): 254.51, ('Brussels', 'Hamburg'): 489.76, ('Bucharest', 'Rome'): 1137.38, ('Brussels', 'Rome'): 1171.34}
    """
    acm = dict() #acm = arbre couvrant minimum
    
    #creons une foret vierge a partir des noeuds de graphe
    foretVierge = creerForetVierge(extraitListNoeuds(graphe))
    
    #trions les arretes de graphe
    grapheTrie = trieGraphe(graphe)
    
    for arrete in grapheTrie:
        #grapheTrie est de la forme: [(('Berlin', 'Hamburg'), 254.51)]
        #arrete est de la forme : (('Berlin', 'Hamburg'), 254.51)
        noeud1 = arrete[0][0] #ie Berlin
        noeud2 = arrete[0][1] #ie Hamburg
        
        if find(noeud1,foretVierge) != find(noeud2,foretVierge):
            # ajout de l'arrete à acm
            acm[arrete[0]] = arrete[1]
            
            union(noeud1,noeud2,foretVierge)
    return acm,foretVierge

    
    
    
