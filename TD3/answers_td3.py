def test_exo_3_11():
    couleurs=[]
    couleurs=couleurs + ['rouge', 'vert', 'bleue']
    return couleurs

def test_exo_3_2():
    print ("1. indoccur : occurence d'une valeur dans une liste ")
    print ("2. que0et1 : tous les elements ont la valeur 0 ou 1")
    print ("3. Quitter ")
    choix = 0
    while not ( choix >= 1 and choix <=3):
        choix =int( input (" Votre choix : ? "))
        if not ( choix >= 1 and choix <=3):
            print (" Erreur : choix invalide , choisir une valeur [1..3] ")
    if choix == 1:
        print (" appel de indoccur ([3 ,2 ,1 ,4 ,1 ,1 ,5 ,8 ,3 ,1] , 1)")
    elif choix == 2:
        print (" appel de que0et1 ([0 ,0 ,0 ,1 ,0 ,0 ,1])")

# exo 3.3 -------------
def indoccur_alt (l,v):
    print (" appel de la fonction indoccur(", l, v, ")")
    res = []
    for indice,element in enumerate (l): #et pas "for a in (l):"
    # enumerate(l): Retourne une sequence dont chaque element est
    # une paire (indice, element) de la liste l
        if element == v:
            res. append (indice) # équivalent à : res=res+[indice]
    return res

# exo 3.4 -------------
# On suppose le résultat True par défaut et on le rend False si et
# seulement si en examinant successivement tous les éléments de la
# liste on en rencontre (au moins) un différent de 0 et différent de 1.
# Les indices n'ont ici pas d'importance, on peut donc appliquer la
# boucle for directement sur la collection de valeurs formée par la liste.
def que0et1 (l):
    print (" appel de la fonction que0et1(", l,")")
    res= True
    for n in l:
        if n != 1 and n != 0 :
            res= False
    return res

# exo 3.3 et 3.4 et 4 -------------
def test_exo_3_3et4():
    print ("1. indoccur : occurence d'une valeur dans une liste ")
    print ("2. que0et1 : tous les elements ont la valeur 0 ou 1")
    print ("3. Quitter ")
    choix = 0
    while not ( choix >= 1 and choix <=3):
        choix =int( input (" Votre choix : ? "))
        if not ( choix >= 1 and choix <=3):
            print (" Erreur : choix invalide , choisir une valeur [1..3] ")
    if choix == 1:
        tab = [3 ,2 ,1 ,4 ,1 ,1 ,5 ,8 ,3 ,1]
        val = int(input(" Choisir une valeur du tableau : " + str(tab) + " : "))
        print(" la valeur ", val, "se trouve aux indices :", indoccur_alt (tab, val), "de ce tableau")
    elif choix == 2:
        if que0et1 ([0 ,0 ,0 ,1 ,0 ,0 ,1]) :
            print (" OUI, cette liste comporte que des 0 et 1")
        else :
            print (" NON, cette liste ne comporte PAS que des 0 et 1")
            
# exo 3.5 -------------
def elem_ind_pair (l):
    # On ajoute dans la liste résultat, au départ vide, tous les éléments
    # d'indice pair de la liste donnée. Il suffit pour cela de faire
    # un parcours de la liste à partir de l'indice 0 avec un pas de 2.
    res =[]
    for i in range (0, len(l) ,2):
        res += [l[i]]
    return res

# exo 3.6 -------------
def est_triee (l):
    # On suppose la liste triée et on vérifie que pour tout indice i
    # (depuis 0 jusqu'à l'avant dernier) on a bien l[i] <= l[i+1]
    # ou en d'autre terme, s'il existe au moins un indice i tel que
    # l[i] > l[i+1] alors la liste n'est pas triée en ordre croissant.
    res= True
    for i in range (len(l) -1):
        if l[i] > l[i+1] :
            res= False
    return res

# exo 3.7 -------------
def listesom (l1):
    # On parcourt la liste l1, et pour chacune des listes l qui la
    # compose, on calcule la somme des éléments de l qu'on ajoute
    # dans la liste résultat.
    res =[]
    for l in l1:
        som =0
        for n in l:
            som = som+n
        res = res + [ som ]
    return res

# exo 3.8 -------------
def singleton (l):
    res =[]
    for e in l:
        res = res + [[e]]
    return res

# exo 3.9 -------------
def fusion (t1 ,t2):
    res =[]
    i1 =0 # indice pour parcourir le tableau t1
    i2 =0 # indice pour parcourir le tableau t2

    # tant qu'on n'est pas au bout d'un des tableaux
    while i1 < len(t1) and i2 < len(t2) :
    # on insère la plus petite des valeurs t1[i1] et t2[i2]
        if t1[i1] < t2[i2 ]:
            res = res + [t1[i1 ]]
            i1=i1 +1
        else :
            res = res + [t2[i2 ]]
            i2=i2 +1
    # si on est arrivé au bout du tableau t1, on insère les éléments restant de t2
    if i1 >= len(t1):
        res = res + t2[i2 :]
    # sinon, on est arrivé au bout du tableau t2 et on insère les éléments restant de t1
    else :
        res = res + t1[i1 :]
    return res

# exo 3.10 -------------
def carre01 (n):
    res =[]
    if n > 1:
        res = res + [ [0]* n ]
    for i in range (1,n -1):
        res =res+ [[0]+[1]*(n -2) +[0]]
    res =res + [ [0]* n ]
    return res

def carre01_2 (n):
    if n >2:
        return [ [0]* n ] + (n -2) * [[0]+[1]*(n -2) +[0]] + [[0]* n]
    else :
        return []
