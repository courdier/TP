rep21="Ce programme affiche la table de multiplication de 3 pour les 10 premiers termes"

def test_exo_2_2():
    a = int( input (" Donner la valeur de a : "))
    b = int( input (" Donner la valeur de b : "))
    # On utilise une variable i qui va prendre les valeurs des entiers compris entre a et b
    # Au départ on initialise i avec la valeur de a
    i = a
    # Tant que i n'a pas dépassée la valeur de b
    while i <= b:
        # On affiche la valeur de i uniquement si celle-ci vérifie la condition demandée
        if (i%3 != 0) and( (i*i -4) % 7 == 0):
            print (i)
        # On passe a l'entier suivant avant de boucler
        i = i+1
        
def test_exo_2_3():
    # Ne pas oublier de convertir la valeur retournée par input en entier
    nombre = int( input (" Donner un entier [1..4] : "))
    # Tant que nombre n'est pas dans l'intervalle
    while not ( nombre >=1 and nombre <= 4):
        nombre = int( input (" Donner un entier [1..4] : "))

def test_exo_2_4():
    # Le programme doit s'arrêter lorsque l'utilisateur a rentré 15 
    # entiers ou bien s'il a saisi la valeur 0. Traduit par une boucle
    # while, cela veut dire que les itérations doivent être réalisées 
    # tant que la valeur saisie n'est pas 0 et que le nombre d'entiers
    # rentré n'est pas 15.
    # Le test de la boucle portant sur les variables a et nbentiers il
    # est nécessaire de les initialiser avant de commencer la boucle :
    # on effectue une première saisie de a et on initialise nbentiers 
    # à 1 (ce qui correspond à la première saisie).
    # A la fin de chaque itération il ne faut pas oublier de re-saisir
    # la valeur de a et d'incrémenter nbentiers.
    nbentiers = 0
    a = 1
    while ( nbentiers <15 and a !=0) :
        a = int( input (" Donnez un entier : "))
        if a !=0:
            nbentiers = nbentiers +1
            print (" Entiers numero",nbentiers ,":",a)
    print(" Merci ")
    
def test_exo_2_5():
    a=int( input (" Donner la valeur de a :"))
    b=int( input (" Donner la valeur de b : "))
    # La variable somme va contenir la somme des carrés des entiers impairs
    # compris entre a et b
    # On initialise cette variable à 0
    somme = 0
    # On utilise une variable i qui va prendre les valeurs des entiers compris entre a et b
    # Au départ on initialise i avec la valeur de a
    i = a
    # Tant que i n'a pas dépassé la valeur de b
    while i <= b:
    # Si i est impair on ajoute son carré dans la somme
        if i%2 == 1:
            somme = somme + i*i
        # Et on passe a l'entier suivant avant de boucler
        i = i+1
    # En sortant de la boucle while (lorsque i est devenu strictement supérieur a b)
    # la variable somme contient le résultat
    print ("La somme des carrés des impairs compris entre ", 
           a, " et ", b, " vaut : ", somme )    
    
from random import *
def test_exo_2_6():   
    # On choisit au hasard le nombre a trouver
    nombre = randint (1 ,100)
    
    # La variable proposition va contenir l'entier proposé par l'utilisateur
    # On initialise cette variable en demandant une première saisie
    proposition = int( input (" Proposer un nombre entre 1 et 100 : "))

    # La variable nbcoup contient le nombre d'essais effectués par l'utilisateur
    # On l'initialise a 1 car on a demandé a l'utilisateur une première proposition
    nbcoup = 1

    # Tant que la proposition est différente du nombre à trouver
    while proposition != nombre :
        # On affiche un message selon que la proposition est plus petite ou plus grande
        # que le nombre à trouver
        if proposition < nombre :
            print (" Trop petit ")
        else :
            print (" Trop grand ")
        # Puis avant de boucler on saisie une nouvelle proposition
        proposition = int( input (" Proposer un nombre entre 1 et 100 : "))
        # ce qui correspond à un essai de plus
        nbcoup = nbcoup +1
        # Lorsqu'on sort de la boucle c'est que la proposition est égale au nombre a trouver
        print (" Gagné en ", nbcoup , " coups ")

def test_exo_2_7():
    # Dans la boucle while qu'on utilise pour calculer chaque terme, 
    # pour une valeur de i, si on veut directement traduire la
    # formule ui = 1/2 × ui_1, on peut utiliser deux variables : 
    # u_i qui contient la valeur du terme ui et u_imoins1 qui contient
    # la valeur du terme précédent.
    # Dans ce cas la boucle commence pour i=1 en ayant initialisée la 
    # variable u_imoins1 avec la valeur de a, c'est à dire u0.
    # Il ne faut pas oublier, à la fin de chaque itération de remplacer
    # la valeur de u_imoins1 par celle de u i, après avoir affiché
    # la valeur u_i et de passer à la valeur i+1 suivante
    u_imoins1 = int( input (" Donner la valeur de a : "))
    n=int( input (" Donner n :"))
    i = 1
    while i < n :
        if u_imoins1 % 2 == 0:
            u_i = u_imoins1 // 2
        else :
            u_i = 3 * u_imoins1 + 1
    print (u_i)
    u_imoins1 = u_i
    i = i + 1

def test_exo_2_8():
    # Programme qui compte le nombre de voyelles (minuscule ou majuscule non accentuée)
    # d'une chaîne de caractères saisie.
    phrase = input (" Donner une phrase : ? ")
    # On compte le nombre de voyelles dans la variable nbvoy
    nbvoy = 0
    # On parcourt la séquence de caractères phrase en comptant
    # et on incrémente nbvoy pour chaque voyelle rencontrée.
    # Un caractère est une voyelle s'il apparaît dans la chaîne "aeiouyAEIOUY"
    for c in phrase :
        if c in " aeiouyAEIOUY ":
            nbvoy = nbvoy + 1
    print ("La phrase : ", phrase )
    print (" contient : ", nbvoy , " voyelles .")

def test_exo_2_9():
    phrase = input (" Donner une phrase : ")

    # On parcourt la séquence de caractères phrase :
    # Pour chaque caractère c
    # si c'est une voyelle on l'affiche
    # sinon si c'est une lettre on affiche * a la place
    # sinon on affiche le caractère c

    for c in phrase :
        # On teste si c est une voyelle
        if c in " aeiouyAEIOUY ":
            print (c, end="")
        else :
            # Ca n'est pas une voyelle mais est-ce une lettre ?
            if (c > "A" and c <= "Z") or (c >= "a" and c <= "z"):
                print ("*", end="")
            else :
                # Ca n'est ni une voyelle ni une lettre
                print (c, end="")
    
def test_exo_2_10():
    # programme brin ADN
    print ("Un brin d'ADN est une séquence de lettre composée uniquement avec des caractères A, C, G et T")
    brin = input ("Donner une séquence de lettres qui représente un brin d'ADN : ")
    # Vérification que la chaîne ne contient que des ACGT
    # A priori on suppose que c'est vrai. On teste les caractères
    # et si l'un deux n'est pas correct c'est faux
    ok= True
    for base in brin :
        if not( base in " AGCT ") :
            ok = False
    if not ok :
        print ("Il y a au moins une erreur dans le brin donné")
    else :
        # On construit le brin complémentaire en parcourant
        # les caractères du brin donné en entrée.
        # Pour chaque caractère dans brin on ajoute le caractère
        # complémentaire dans brin2 qui au départ est une chaîne vide
        brin2 = ""
        for base in brin :
            if base == "A" :
                duo = "T"
            if base == "T" :
                duo = "A"
            if base == "C" :
                duo = "G"
            if base == "G" :
                duo = "C"
            brin2 = brin2 + duo
        print ("Le brin complementaire de :")
        print ( brin )
        print ("est : ")
        print ( brin2)