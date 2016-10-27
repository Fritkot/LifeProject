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
            foret[arbre]=[arbre,1]
    
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
    fusionne deux arbres dans une foret.
    La fusion se déroule comme suit:
        on regarde l'aieul de chaque arbre:
            - si aieul(arbre1) == aieul(arbre2) 
                alors les arbres sont deja connectes dans la foret
            - sinon
                - on affecte l'arbre avec l'aieul de rang le plus grand à l'autre arbre.
        
    """
    pereArbre1 = find(arbre1,foret)
    pereArbre2 = find(arbre2,foret)
    
    if pereArbre1[0] != pereArbre2[0]: # test si les deux arbres ont des aieux differents
         #test les rangs des arbres aieux
        if pereArbre1[1] < pereArbre2[1]: # cas ou rang(arbre1) < rang(arbre2)
            
            foret[pereArbre1[0]][0] = pereArbre2[0]
            foret[pereArbre2[0]][1] += foret[arbre1][1]
            
        elif pereArbre1[1] > pereArbre2[1]: # cas ou rang(arbre1 > rang(arbre2)
            
            foret[pereArbre2[0]][0] = pereArbre1[0]#,pereArbre2[1]]
            foret[pereArbre1[0]][1] += foret[arbre2][1]
        
        else: #cas ou les rangs sont egaux : pereArbre1[1] == pereArbre2[1]:
                foret[pereArbre2[0]][0] = pereArbre1[0] #arbitrairement on selectionne l'arbre1 comme aieul
                foret[pereArbre1[0]][1] += foret[arbre2][1]
            
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
    return acm

    
    
    
