## Méthodes relatives aux Graphes
"""
Cette section va contenir toutes les methodes relatives aux graphes:
    - trie des arretes
    - extraire la liste des noeuds à partir d'un graphe
"""

def creerGrapheDepuisMatriceAdjacence(matriceAdjacence,listeNoeuds):
    """
    construit un graphe a partir de la matrice d'adjacence
    
    parametre :
        matriceAdjacence :  une matrice d'adjacence representant un graphe non-oriente
            type : dictionnaire de la forme : {['noeud1','noeud2'] : poids}
        listeNoeuds : la liste de tous les noeuds du graphe
            type : list
    return graphe sous forme d'un dictionnaire
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
    """
    graphe = dict()
    
    for noeud1 in listeNoeuds:
        for noeud2 in listeNoeuds:
            distance = matriceAdjacence[noeud1,noeud2]
            if distance > 0 : # si 0 => la ville correspond à elle-même
                            # si <0 => il n'y a pas de connexion entre les deux villes
                graphe[creerArete(noeud1,noeud2)] = distance
            
    return graphe

def testEstSymetrique(matriceAdjacence, listeNoeuds):
    """
    test si la matrice d'adjacence est symétrique
    
    parametre :
        matriceAdjacence :  une matrice d'adjacence representant un graphe non-oriente
            type : dictionnaire de la forme : {['noeud1','noeud2'] : poids}
        listeNoeuds : la liste de tous les noeuds du graphe
            type : list
    return True si la matrice est symetrique, False sinon
        type : bool
    """
    
    for ligne in listeNoeuds:
        for colonne in listeNoeuds:
            if ligne != colonne and matriceAdjacence[ligne,colonne] != matriceAdjacence[colonne,ligne]:
                return False
    
    return True
    
    
def testEstGrapheComplet(graphe):
    """
    test si le graphe est un graphe complet.
    C'est-a-dire si chaque noeud est connecte a chaque noeud.
    
    parametre :
        graphe : un graphe non-oriente complet
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
    return True si le graphe est complet, False sinon
        type: bool
    
    """
    listNoeuds = extraitListNoeuds(graphe)
    
    for noeud1 in listNoeuds:
        for noeud2 in listNoeuds:
            if noeud1 != noeud2:
                if graphe.get(creerArete(noeud1,noeud2)) is None:
                   return False
    return True #tous les noeuds sont connectes
    
def testEstPair(graphe):
    """
    test si tous les noeuds du graphe sont de degré pair
    
    parametre :
        graphe :  un graphe non-oriente
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
    return True : si le graphe est pair, False sinon
        type: bool
    """
    bool = True
    
    for el in calculerDegreNoeuds(graphe).items():
        if el[1]%2 > 0 :
            bool = False
    
    return bool
    
    
    

def testInegaliteTriangulaire(graphe):
    """
    regarde si le graphe respecte l'inegalite triangulaire. On suppose le graphe complet.
    
    Boucle sur tous les noeuds et verifie pour chaque noeuds que:
        poids(arete 1-2)<= poids(arete 1-3) + poids(arete 2-3)
    
    parametre :
        graphe : un graphe non-oriente complet
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
    return True si le graphe respecte l'inegalite triangulaire, False sinon
        type: bool
    """
    bool = True
    
    #parcours de tous les noeuds
    listNoeuds = extraitListNoeuds(graphe)
    for noeud1 in listNoeuds:
        for noeud2 in listNoeuds:
            if noeud1 != noeud2:
                for noeud3 in listNoeuds:
                    if noeud3 != noeud1 and noeud3 != noeud2:
                        areteN12 = creerArete(noeud1,noeud2)
                        areteN13 = creerArete(noeud1,noeud3)
                        areteN23 = creerArete(noeud2,noeud3)
                        
                        if graphe.get(areteN12) > graphe.get(areteN13)+graphe.get(areteN23):
                            print("l'arete",areteN12," > arete",areteN13," + arete",areteN23)
                            return False
                        if graphe.get(areteN13) > graphe.get(areteN12)+graphe.get(areteN23):
                            print("l'arete",areteN13," > arete",areteN12," + arete",areteN23)
                            return False
                        if graphe.get(areteN23) > graphe.get(areteN13)+graphe.get(areteN12):
                            print("l'arete",areteN23," > arete",areteN13," + arete",areteN12)
                            return False
    return True



def autreExtremiteArete(arete, noeud):
    """
    renvoie l'autre extremité d'une arete par rapport au noeud passe en parametre
    
    parametre :
        - arete : arete dans laquelle on cherche l'autre extremite
            type : tuple
        - noued : premiere extremite de l'arete
            type : string
    return l'autre extremite de l'arete ou None si le noeud n'appartient pas a l'arete
        type : string
    
    ex : autreExtremiteArete(creerArete('A','B'),'A') => 'B'
    """
    
    if noeud in arete:
        if noeud == arete[0]:
            return arete[1]
        else:
            return arete[0]
    return None

def creerArete(noeud1,noeud2):
    """
    cree une arete a partir de deux noeuds.
    L'arete est representee par un tuple dont le premier element est le noeud le plus petit dans le sens lexicographique
    
    parametre :
        - noeud1 : premier noeud
            type : string
        - noeud2 : deuxieme noeud
    
    return un tuple (noeud1, noeud2) si noeud1 <= noeud2, sinon (noeud2,noeud1)
    
    ex:
    creerArete('B','A') => ('A', 'B')
    """
    
    if noeud1 <= noeud2:
        return (noeud1,noeud2)
    else:
        return (noeud2,noeud1)


def trieGraphe(graphe,ascendant=True):
    """
        trie un graphe par valeur ascendante (par defaut) ou descendante des poids des arrêtes.
        
        parametres:
            gaphe : un graphe sous forme de dictionnaire avec un couple de ville comme clef
                type: dictionnaire
            ascendant : indique si le trie est ascendant ou descendant
                type : booleen
        return : graph trie
            type : list (si on renvoit un dictionnaire, l'ordre des arretes n'est plus garantie)
            
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


def calculerDegreNoeuds(graphe):
    """
    Calcul le degre de chaque noeud du graphe
    
    Le calcul des degres d'un noeud prend en compte le cas des graphes a aretes multiples
    Ceci intervient dans l'etape 4 de l'algorithme de Christofides ou des graphes a aretes multiples peuvent etre generes.
    
    parametre :
        - graphe : un graphe non-oriente
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
    return : le degre de chaque noeud du graphe en parametre
        type : dictionnaire ou la clef est le nom du noeud et son degre : {"noeud":degre}
        
    ex:
        graphe = {('B', 'F'): 4.0, ('A', 'F'): 3.0, ('D', 'F'): 50.0, ('D', 'E'): 2.0, ('C', 'E'): 1.0}
        calculerDegreNoeuds(graphe) => {'E': 2, 'A': 1, 'D': 2, 'C': 1, 'F': 3, 'B': 1}
    
    """
    listNoeuds = extraitListNoeuds(graphe)
    
    degres = dict()
    
    for noeudOrigine in listNoeuds:
        degres[noeudOrigine] = 0 #initialisation du dictionnaire
        
        for noeudArrivee in listNoeuds:
            if noeudOrigine != noeudArrivee:
                #trie lexicographique des noms de noeuds
                couple = creerArete(noeudOrigine,noeudArrivee)
                poids = graphe.get(couple)
                if poids is not None:#test si l'arete existe
                    if isinstance(poids,list): #cas du graphe à arêtes mutliples
                        degres[noeudOrigine] += len(poids)
                    else:
                        degres[noeudOrigine] += 1    
    return degres


def selectionNoeudsParite(graphe,pair=True):
    """
    extrait uniquement les noeuds de degre pair (par defaut) ou impair du graphe
    parametre :
        - graphe : un graphe non-oriente
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
        - pair : indique si uniquement les noeuds de degre pair sont regardés ou les noeuds de degre impairs. Par defaut, la methode ne selectionne que les noeuds de degre pair
            type : booleen
    return : la liste des noeuds de degre impair
        type : liste
    ex:
    graphe = {('D', 'F'): 50.0, ('C', 'E'): 1.0, ('A', 'F'): 3.0, ('B', 'F'): 4.0, ('D', 'E'): 2.0}
    selectionNoeudParite(graphe) => ['E', 'D']
    """
    resultat = list()
    
    #calcul des degres de chaque noeud du graphe
    degresNoeuds = calculerDegreNoeuds(graphe)
    
    if pair:
        for noeud in degresNoeuds.keys():
            if degresNoeuds.get(noeud)%2 == 0: #selection degre pair
                resultat.append(noeud)
    else:
        for noeud in degresNoeuds.keys():
            if degresNoeuds.get(noeud)%2 == 1: #selection degre impair
                resultat.append(noeud)
    
    return resultat

def extraireAretesDepuisNoeuds(graphe, noeud):
    """
    extrait les aretes adjacente au noeud en parametre
    
    Le cas des graphes a aretes multiple est pris en compte. (peut-etre produit dans l'etape 4 de l'algorithme de Christofides)
    
    parametre:
        - graphe : un graphe non-oriente
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique 
        - noeud : le noeud depuis lequel on extrait les aretes
            type : string
    return : list des aretes sous forme de couple
        type: list()
    """
    
    arete=list()
    listeNoeuds = extraitListNoeuds(graphe)
    
    for n in listeNoeuds:
        ar = creerArete(noeud,n)
        if ar in graphe.keys():
            if isinstance(graphe[ar],list): # cas des graphes à arêtes multiples
                for el in graphe[ar]:
                    arete.append(ar)
            else:
                arete.append(ar)
    
    return arete

def extraireGrapheDepuisListeArete(graphe,liste):
    """
    extrait un sous-graphe a partir d'une liste d'arete
    
    parametre :
        - graphe : un graphe non-oriente
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique 
        - liste : liste des noeuds a extraire du graphe 
            type : liste
            ex : ['C', 'E', 'D', 'A', 'B', 'C', 'F', 'C']
    return un sous-graphe issu de graphe n'ayant comme aretes que les aretes decrites dans liste
        type :  dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique 
    
    ex :
    

    """
    
    newGraphe = dict()
    
    for i in range(len(liste)-1):
        arete = creerArete(liste[i],liste[i+1])
        newGraphe[arete] = graphe[arete]
    
    return newGraphe
   
def extraireSousGraphe(graphe,listeNoeuds):
    """
    extrait un sous-graphe a partir d'une liste de noeuds
    
    parametre :
        - graphe : un graphe non-oriente
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique 
        - listeNoeuds : liste des noeuds a extraire du graphe
            type : liste
    return un sous-graphe issu de graphe n'ayant comme noeuds que les noeuds de listeNoeuds
        type :  dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique 
                    
    ex:
    graphe = {('D', 'E'): 2.0, ('B', 'F'): 4.0, ('A', 'B'): 1000.0, ('C', 'F'): 200.0, ('C', 'E'): 1.0, ('C', 'D'): 300.0, ('B', 'D'): 100.0, ('D', 'F'): 50.0, ('A', 'F'): 3.0}
    extraireSousGraphe(graphe) => {('C', 'F'): 200.0, ('B', 'F'): 4.0, ('A', 'B'): 1000.0, ('A', 'F'): 3.0}
    """
    newGraph= dict()
    
    for noeudOrigine in listeNoeuds:
        for noeudArrivee in listeNoeuds:
            arete = creerArete(noeudOrigine,noeudArrivee)
            #test si l'arete existe dans graphe
            if graphe.get(arete) is not None:
                newGraph[arete] = graphe.get(arete)
    return newGraph

def unionDeuxGraphes(graphe1,graphe2):
    """
    realise l'union des deux graphes en parametres
    
    si une même arete apparait dans les deux graphes, les deux aretes sont ajoutees.
    Ceci implique que des aretes multiples peuvent apparaitre.
    
    parametre :
        - graphe1, graphe2 : un graphe non-oriente
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique 
    
    return : l'union des deux graphes
            Attention des aretes multiples peuvent apparaitre sous la forme d'un liste de poids plutot que d'une valeur pour le poids de l'arete dans le dictionnaire. ex:  {('C', 'F'): [2.0, 2.0]}
        type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
    
    ex :
    graphe1 =  {('C', 'F'): 2.0, ('A', 'B'): 2.0, ('C', 'E'): 3.0, ('D', 'E'): 2.0, ('B', 'C'): 2.0}
    graphe2 = {('C', 'F'): 2.0, ('A', 'D'): 4.0}
    unionDeuxGraphes(graphe1,graphe2) => {('C', 'E'): 3.0, ('D', 'E'): 2.0, ('C', 'F'): [2.0, 2.0], ('A', 'B'): 2.0, ('A', 'D'): 4.0, ('B', 'C'): 2.0}
    """
    
    graphe = dict()
    
    #ajoutons toutes les arêtes du premier graphe
    for arete in graphe1:
        graphe[arete] = graphe1[arete]
    
    #regardons chaque arête de graphe2 et ajouons les si besoin est
    for arete in graphe2:
        if arete in graphe1:
            graphe[arete] = [graphe1[arete],graphe2[arete]]
        else:
            graphe[arete] = graphe2[arete]
    
    
    return graphe
   
def listeAdjacence(graph):
    """
    renvoie la liste d'adjacence du graph passé en paramètre
    
    parametre :
        - graph : un graph non-oriente
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
                    
    return : la liste d'adjacence du graph passé en paramètre
        type :  dictionnaire des noeuds du graph contenant la liste de leurs noeuds adjacents 
            {'noeud1':[noeud2, noeud4], 'noeud2':[noeud1], 'noeud3':[], 'noeud4':[noeud1]}
                    
    ex:
    graph = {('D', 'E'): 2.0, ('B', 'F'): 4.0, ('A', 'B'): 1000.0, ('C', 'F'): 200.0, ('C', 'E'): 1.0, ('C', 'D'): 300.0, ('B', 'D'): 100.0, ('D', 'F'): 50.0, ('A', 'F'): 3.0}
    listeAdjacence(graph) => {'A':['B','F'], 'B':['A','D','F'], 'C':['D','E','F'], 'D':['B','C','E','F'], 'E':['C','D'], 'F':['A','B','C','D']}
    """
    listeAdj=dict()
    
    # Parcours des aretes du graph
    for arete in graph.keys():
        # Traitement du noeud de début de l'arete
        if arete[0] not in listeAdj: # Création de la clef correspondant au noeud si besoin
            listeAdj[arete[0]] = list()
        listeAdj[arete[0]].append(arete[1]) # Ajout du noeud relié à la liste
        # Meme traitement appliqué au noeud de fin de l'arete
        if arete[1] not in listeAdj:
            listeAdj[arete[1]] = list()
        listeAdj[arete[1]].append(arete[0])
    
    return listeAdj
    
    
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
        return sommet
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
            
            foret[aieul1][0] = aieul2
            foret[aieul2][1] += foret[aieul1][1]
            
        else: # cas rang(sommet1) > rang(sommet2) ou les rangs sont egaux : foret[aieul1][1] == foret[aieul2][1]:
            foret[aieul2][0] = aieul1 # arbitrairement on selectionne l'aieul du sommet1 comme aieul
            foret[aieul1][1] += foret[aieul2][1]
            
    return 

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

##Algorithmes de parcours de graphs
def parcoursEnLargeur(graphe, noeudDepart):
    """
    Parcours en largeur d'un graphe
    
    parametre :
        -graphe : un graphe non-oriente
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
        
    return liste des noeuds dans l'ordre du parcours en largeur. Chaque element correspond a un niveau
        type : list()
    
    ex:
    graphe = {('A', 'F'): 3.0, ('C', 'F'): 200.0, ('A', 'B'): 1000.0, ('B', 'F'): 4.0}
    parcoursEnLargeur(graphe, 'A') => [['A'], ['F', 'B'], ['C'], []]
    """    
    listeNoeud = extraitListNoeuds(graphe)
    
    #initialisation des noeuds, pour le moment aucun noeud n'a ete visite
    estVisite = dict()
    for node in listeNoeud : 
        estVisite[node] = False
    estVisite[noeudDepart] = True
    
    #creons la file des noeuds a visiter
    #chaque element de file est une liste de noeuds qui correspond au niveau du noeud dans le parcours en largeur
    file = list()
    file.append([noeudDepart]) #le noeud de depart est au niveau 0
    
    niveau = 0
    while len(file[niveau])>0 : #tant que la file des noeuds encore a explorer n'est pas vide

        # creons un nouveau niveau d'exploration
        file.append(list())
        
        #parcourons les noeuds
        for noeud in file[niveau]:
            for arete in extraireAretesDepuisNoeuds(graphe,noeud):
                
                # #testons si l'autre extremite de l'arete a deja ete visitee
                # if arete[0] == noeud:
                #     extremite = 1
                # else:
                #     extremite = 0
                # noeudArrivee = arete[extremite]
                noeudArrivee = autreExtremiteArete(arete,noeud)
                
                if estVisite.get(noeudArrivee) == False:
                    estVisite[noeudArrivee] = True
                    #ajout du nouveau noeud a la liste des noeuds en attente d'exploration
                    file[niveau+1].append(noeudArrivee)
        niveau += 1
    
    return file
    
    
    
def parcoursEnProfondeur(graph, noeudDepart):
    """
    Parcours en profondeur d'un graph
    
    parametre :
        -graph : un graph non-oriente
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
        
    return liste des noeuds dans l'ordre d'un parcours en profondeur en mode prefixe
        type : list()
    
    ex:
    graph = {('A', 'F'): 3.0, ('C', 'F'): 200.0, ('A', 'B'): 1000.0, ('B', 'F'): 4.0}
    parcoursEnProfondeur(graph, 'A') => ['A', 'F', 'B', 'C'] ou ['A', 'F', 'C', 'B']
            ou ['A', 'B', 'F', 'C'] (en fonction de l'acces memoire aux aretes du graph
    """    
    
    # initialisation des noeuds, aucun noeud n'a encore ete visite
    estVisite = dict()
    for node in extraitListNoeuds(graph) : 
        estVisite[node] = False
    
    # creons la pile des noeuds a visiter, initialisee donc par le noeud de depart
    pile = [noeudDepart]
    # et la liste du parcours du graph, initialisee vide
    parcours = list()
    
    while len(pile)>0 : # tant que la pile des noeuds a explorer n'est pas vide

        # prenons le noeud du dessus de la pile
        noeudAExp = pile.pop()
        
        # si le noeud n'a pas ete visite, ajouter a la pile ses voisins
        if not estVisite[noeudAExp]:
            
            # ajoutons le noeud au parcours
            parcours.append(noeudAExp)
            estVisite[noeudAExp] = True
            
            # parcourons les aretes du graph a partir du noeud pour trouver ses voisins
            for arete in extraireAretesDepuisNoeuds(graph,noeudAExp):
                pile.append(autreExtremiteArete(arete,noeudAExp))
                # # testons quelle extremite de l'arete est le noeud a explorer pour ajouter le voisin et non le noeud en cours d'exploration
                # if arete[0] == noeudAExp:
                #     pile.append(arete[1])
                # else:
                #     pile.append(arete[0])
    
    return parcours
    
    
    
##Algorithme concernant les graphes biparti   
def estGrapheBiparti(graphe):
    """
    Un graphe est biparti s'il existe une partition de son ensemble de sommets en deux sous-ensembles U et V telle que chaque arete ait une extremite dans U et l'autre dans V.
    
    Pour determiner si un graphe est biparti, on peut utiliser un parcours en profondeur de la maniere suivante:
    1) colorier les noeuds de niveau pair en rouge et les noeuds de niveau impair en vert.
    2) si il existe une arete entre deux noeuds d'une meme couleur alors le graphe n'est pas biparti. Il l'est sinon.
    
    
    parametre :
        - graphe : un graphe non-oriente
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
        
    return True si le graphe est biparti, False sinon
        type : bool
        
    ex :
    graphe = {('A', 'F'): 3.0, ('A', 'B'): 1000.0, ('B', 'F'): 4.0, ('C', 'F'): 200.0}
    estGrapheBiparti(graphe) => False
    """
    
    #realisons le parcours en largeur
    noeudDepart = extraitListNoeuds(graphe)[0] #on prend arbitrairement le premier element
    parcours = parcoursEnLargeur(graphe,noeudDepart)
    
    vert = list()
    rouge = list()
    
    #colorions les noeuds de niveau pair en rouge et les noeuds de niveau impair en vert
    for niveau in range(0,len(parcours)):
        for noeud in parcours[niveau]:
            if niveau%2==0:#niveau pair
                rouge.append(noeud)
            else:
                vert.append(noeud)
    
    #testons s'il existe une arete entre noeuds de meme couleur

    #1) noeud vert
    for noeud1 in vert:
        for noeud2 in vert:
            if noeud1 != noeud2:
                arete = creerArete(noeud1,noeud2)
                if graphe.get(arete) is not None: #l'arete existe
                    return False
    
    #2) noeud rouge
    for noeud1 in rouge:
        for noeud2 in rouge:
            if noeud1 != noeud2:
                arete = creerArete(noeud1,noeud2)
                if graphe.get(arete) is not None: #l'arete existe
                    return False
                    
    #return True s'il n'y a pas d'arete au sein de noeuds de meme couleur
    return True
    

##Algorithme pour graphes eulériens
# Algorithme de calcul d'un cycle eulérien dans un graphe eulérien
# NON FINI car plus nécessaire
def cheminEulerien(graphEulerien):
    """
    Un graphe est eulérien si tous les sommets sont de degré pair, i.e. le nombre d'arêtes partant de chaque sommet est pair
    
    parametre :
        - graphEulerien : un graphe eulérien non-oriente
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
        
    return chemin : un chemin eulérien parcourant le graphe
        type : liste de sommets
        
    ex :²
    graphe = {('A', 'F'): 3.0, ('A', 'B'): 1000.0, ('B', 'C'): 4.0, ('C', 'F'): 200.0}
    cheminEulerien(graphe) => [A, F, C, B, A]
    """
    # Vérification que le graph est eulérien
    bVerif = True
    dDegres = calculerDegreNoeuds(graphEulerien)
    for degre in dDegres.values():
        if degre % 2 != 0:
            bVerif = False
            print('Attention : utilisation d\'un graph non-eulerien dans la fonction "cheminEulerien"')
            break
    
    lChemin = list()
    if bVerif:
        
        # Etape 1: construire les listes de noeuds et d'adjacence du graphe
        dListeAdj = listeAdjacente(graphEulerien)
        lListeNoeuds = extraitListNoeuds(graphEulerien)
        
        # Etape 2: construire un chemin à partir d'un sommet jusqu'à boucler sur lui-même
        #for arete in graphEulerien:
            
        
        # Etape 3: rechercher le sommet où il reste des arêtes et décaler le chemin parcouru s'il existe
    
    return lChemin

def algorithmeEuclide(graphe,noeudDepart):
    """
    
    """
    parcours = [noeudDepart]
    
    aretes = extraireAretesDepuisNoeuds(graphe,noeudDepart)
    
    #test si noeudDepart est un noeud isolé
    if len(aretes) == 0:
        return parcours
    else:
        noeudCourant = noeudDepart
        estNoeudIsole = False
        while not(estNoeudIsole):
            #prenons la première arête partant de noeudCourant
            areteAdjacente = extraireAretesDepuisNoeuds(graphe,noeudCourant)[0]
            
            #cherchons l'autre extrémité de l'arête
            # if noeudCourant == areteAdjacente[0]:
            #     noeudAutreExtremite = areteAdjacente[1]
            # else:
            #     noeudAutreExtremite = areteAdjacente[0]
            noeudAutreExtremite = autreExtremiteArete(areteAdjacente,noeudCourant)
            
            #supprimons l'arête du graphe
            if isinstance(graphe[areteAdjacente],list): #cas du graphe à arêtes multiples
                graphe[areteAdjacente].pop(-1) #retire le dernier élément de la liste des poids
                if len(graphe[areteAdjacente])==0: #si la liste des poids est nulle => il n'y a plus d'arête
                    graphe.pop(areteAdjacente) #on retire l'arête du graphe
            else:
                graphe.pop(areteAdjacente)
            
            noeudCourant = noeudAutreExtremite
            parcours.append(noeudCourant)
            
            if len(extraireAretesDepuisNoeuds(graphe,noeudCourant))==0:
                estNoeudIsole = True
    
    
    #créons des cycles pour chaque noeud du parcours et concaténons les parcours obtenus
    chemin = []
    for element in parcours:
        cycle = algorithmeEuclide(graphe,element)
        chemin.extend(cycle)
    
    return chemin
            
    
def calculerCheminEulerien(graphe):
    """
    
    """
    
    "Test si le graphe est pair"
    if not(testEstPair(graphe)):
        raise Exception("Le graphe n'est pas pair")
    
    
    #copions le graphe
    # et séléctionnons un noeud de départ
    #Arbitrairement prenons le premier dans le dictionnaire graphe
    noeudDepart = None
    grapheTemp = dict()
    for el in graphe:
        if isinstance(graphe[el],list): #cas des graphes à arêtes mutliples
            grapheTemp[el] = []
            #on copie chaque élément de la liste de poids pour éviter des effets de bords
            #dans algorithmeEuclide, il y a une recursivité qui enlève des éléments à grapheTemp
            #avec une copie simple, c'est la référence de la liste qui est affectée à grapheTemp et non ses valeurs.
            for poids in graphe[el]:
                grapheTemp[el].append(poids)
        else:
            grapheTemp[el]=graphe[el]
        if noeudDepart is None:
            noeudDepart = el[0]
    
    return algorithmeEuclide(grapheTemp,noeudDepart)

## Algorithme pour graphe hamiltonien
def calculerCycleHamiltonien(cycleEulerien):
    """
    Principe :
    A partir d'un graphe complet qui respecte l'inegalite triangulaire et a partir d'un cycle eulerien, on deduit un cycle Hamiltonien de la maniere suivante :
        - On parcours le cycle hamiltonien.
        - Quand on repasse par un noeud par lequel on est deja passe, on saute directement au noeud suivant. Ceci est donne par l'inegalite triangulaire et par la completude du graphe : on sait qu'il existe un chemin de poids plus petit qui relie directement le premier noeud au troisieme noeud. Si on veut aller de A a C en passant par B et qu'on est deja passe par B, on sait qu'il existe une arete reliant A a C qui est plus petit poids que le poids de (A,B)+(B,C).
    
    Fait :
    On itere dans l'ordre le cycle et des que l'on repasse par un noeud deja visite, on ne le prend pas en compte.
    
    parametres :
        - cycleEulerien : liste des noeuds representant le chemin, le dernier noeud est le premier noeud ce qui indique la presence d'un cycle. Un chemin Eulerien est un chemin qui passe une seule fois par toutes les aretes du graphe.
            type : liste ex: ['C', 'E', 'D', 'A', 'B', 'C', 'F', 'C']
            
    return : cycle hamiltonien : un cycle qui passe une et une seule fois par tous les noeuds du graphe passe en parametre.
        type : liste
    
    ex : cycleEulerien = ['C', 'E', 'D', 'A', 'B', 'C', 'F', 'C']
        calculerCycleHamiltonien(cycleEulerien) => ['C', 'E', 'D', 'A', 'B', 'F', 'C']
    """
    cycle = []
    for noeud in cycleEulerien:
        if not(noeud in cycle):
            cycle.append(noeud)
    
    #on ajoute le premier noeud pour former le cycle
    cycle.append(cycleEulerien[0])
    return cycle
    
    
##Algorithme de Couplage
def couplageNaif(graphe):
    """
    Test toutes les aretes possible pour trouver un couplage de poids minimum :
        - démarre par l'arete de poids minimum et ajoute successivement les autres aretes tant 
        qu'il y a encore des noeuds disponible
        - si le couplage trouvé n'est pas parfait, on recommence avec l'arete suivante, etc.
    parametre :
        graphe : un graphe non-oriente complet
            type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
                    le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
    return : couplage parfait ou None si aucun couplage parfait n'a ete trouve.
        type : dictionnaire de la forme : {('noeud1','noeud2') : poids}
            le premier element du tuple est le plus petit noeud dans l'ordre lexicographique
    
    ex :
        graphe ={('A', 'C'): 4.0, ('A', 'F'): 5.0, ('C', 'D'): 3.0, ('C', 'F'): 2.0, ('D', 'F'): 3.0, ('A', 'D'): 4.0}
        couplageNaif(graphe) => {('C', 'F'): 2.0, ('A', 'D'): 4.0}
    """
    #on trie le graphe par poids d'arête croissante
    grapheTrie = trieGraphe(graphe)
    
    #on teste toutes les arêtes on démarrant par celle de poids le plus petit
    for arete1 in grapheTrie:
        couplage = dict()
        noeudsPris = list() #indique si un noeud est déjà untilisé dans un couplage
        
        couplage[arete1[0]]=arete1[1]
        noeudsPris.append(arete1[0][0])
        noeudsPris.append(arete1[0][1])
        
        #on ajoute successivement d'autres arêtes afin de former le couplage parfait
        for arete2 in grapheTrie:
            if arete1 != arete2:
                if not(arete2[0][0] in noeudsPris or arete2[0][1] in noeudsPris):
                    couplage[arete2[0]]=arete2[1]
                    noeudsPris.append(arete2[0][0])
                    noeudsPris.append(arete2[0][1])
                    
        
        #test si le couplage est parfait
        #le couplage est parfait si chaque noeud est de  dégré 1
        estParfait = True
        degres = calculerDegreNoeuds(couplage)
        for noeud in degres.items(): #de la forme [('Noeud1',degre),('Noeud2',degre)]
            if noeud[1] != 1: 
                estParfait = False 
        
        if estParfait :
            return couplage
    #fin boucle for
    
    print("aucun couplage n'a été trouvé")
    return None #aucun couplage parfait n'a été trouvé

##Algorithme d'Edmonds
#algorithme de calcul d'un couplage parfait dans un graphe quelconque