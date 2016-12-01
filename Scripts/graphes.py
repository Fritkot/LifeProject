## Méthodes relatives aux Graphes
"""
Cette section va contenir toutes les methodes relatives aux graphes:
    - trie des arretes
    - extraire la liste des noeuds à partir d'un graphe
"""


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


def calculerDegreNoeuds(graphe):
    """
    Calcul le degre de chaque noeud du graphe
    
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
                if graphe.get(couple) is not None:
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
            arete.append(ar)
    
    return arete
    
   
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

##Algorithme concernant les graphes biparti
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
                
                #testons si l'autre extremite de l'arete a deja ete visitee
                if arete[0] == noeud:
                    extremite = 1
                else:
                    extremite = 0
                noeudArrivee = arete[extremite]
                
                if estVisite.get(noeudArrivee) == False:
                    estVisite[noeudArrivee] = True
                    #ajout du nouveau noeud a la liste des noeuds en attente d'exploration
                    file[niveau+1].append(noeudArrivee)
        niveau += 1
    
    return file
    
    
    
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
    

##Algorithme pour arbres eulériens
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
        
    ex :
    graphe = {('A', 'F'): 3.0, ('A', 'B'): 1000.0, ('B', 'C'): 4.0, ('C', 'F'): 200.0}
    cheminEulerien(graphe) => [A, F, C, B, A]
    """
    # Vérification que le graph est eulérien
    bVerif = True
    dDegres = calculerDegreNoeuds(graphEulerien)
    for degre in dDegres.values():
        if degre % 2 != 0:
            bVerif = False
            print('Attention : utilisation d\'un graph non-eulerien dans la fonction \"cheminEulerien\"')
            break
    
    lChemin = list()
    # if bVerif:
    #     # Etape 1: construire les listes de noeuds et d'adjacence du graphe
    #     dListeAdj = listeAdjacente(graphEulerien)
    #     lListeNoeuds = extraitListNoeuds(graphEulerien)
    #     
    #     # Etape 2: construire un chemin à partir d'un sommet jusqu'à boucler sur lui-même
    #     for arete in graphEulerien:
    #         
    #     
    #     # Etape 3: rechercher le sommet où il reste des arêtes et décaler le chemin parcouru s'il existe
    return lChemin
    

    
##Algorithme de Flot
#algorithme de calcul de couplage parfait dans un graphe biparti


##Algorithme d'Edmonds
#algorithme de calcul d'un couplage parfait dans un graphe quelconque