rep111="Lorsqu'il y a un plus d'un opérateur, l'ordre de leur évaluation suit des règles de priorité. L'ordre peut se retenir à l'aide du mémotechnique PEMDAS. Python respecte les priorités usuelles des langages de programmation."
rep112="Lorsqu'une expression porte à la fois sur des flottants et des entiers, l'interpréteur transforme alors tous les entiers en flottants"
rep113="L'opérateur / est l'opérateur de division sur les flottants. L'opérateur // est l'opérateur de division entière appliquée sur des flottants, le résultat est la partie entière de la division renvoyée sous forme de flottant."
rep114="L'opérateur % calcule le reste de la division entière. Appliquée sur des flottants, le résultat est renvoyé sous forme de flottant."
rep132="Pour savoir si un nombre est impair il sufit de tester que le reste de sa division par 2 est égal à 1."
rep151="On peut connaître le code ASCII d'un caractère grâce à la fonction ord. 3 avec l'entier 123 ! droite. La comparaison est faite selon l'ordre alphanumérique ou plus exactement selon l'ordre définit par le codage ASCII des caractères dans lequel - entre autre - les chiffres précédent les lettres majuscules qui précédent elles-même les lettres minuscules."
rep162="Les fonctions int et float sont des fonctions de conversion de type."
rep182="La fonction type permet de connaître le type d'une expression. (De savoir ce que l'on manipule comme donnée dans une variable.)"
rep192="En affectant la valeur a=20 il ne se passe rien ! L'expression d'alternative ne retourne aucune valeur puisque le cas a<=100 n'est pas prévu."  


def test_exo_1_13():
    print("1. Enregistrer la partie")
    print("2. Charger une partie")
    print("3. Nouvelle partie")
    print("4. Quitter")
    ichoix = int(input("Votre choix : "))
    if (0 < ichoix and ichoix < 5): 
        print ("Ok")
    else:
        print("Choix incorrect")
        
def test_exo_1_14():
    a = int( input (" Donner un premier entier "))
    b = int( input (" Donner un second entier ")) 
    c = int( input (" Donner un troisieme entier "))
    nb_zero = 0
    if a == 0 :
        nb_zero += 1
    if b == 0 :
        nb_zero += 1
    if c == 0 :
        nb_zero += 1
    print ("Il y a", nb_zero , " zeros ")    
    
def test_exo_1_15():
    # Programme de conversion de temperature
    # On saisit la valeur de la ytempetrature sous la forme d'un réel (float)
    temp = float ( input (" Donnez la temperature :"))
    unite = input (" Donnez l'unite C, F ou K : ")

    if ( unite != "C") and ( unite != "F") and ( unite != "K") :
        print ("Erreur , unite incorrecte ")
    else :
        if unite == "C" :
            tempC = temp
        elif unite == "F" :
            tempC = 9 * ( temp - 32) / 5.0
        elif unite == "K" :
            tempC = temp - 273.15
        
    tempF = 5 * tempC / 9.0 + 32
    tempK = tempC + 273.15
    print (tempC ,"C =", tempF , "F =", tempK , "K")

def test_exo_1_16():
    # Calcul de volume d'un parallélépipède
    long = float ( input (" Donnez la longueur : "))
    larg = float ( input (" Donner la largeur : "))
    haut = float ( input (" Donner la hauteur : "))
    print ("Le volume du parallelepipede ainsi definit est ", long * larg * haut )   

def test_exo_1_17():
    # Le nombre est-il entier ?
    a = int( input (" Donner une entier : "))
    if a % 2 == 0 :
        print (" Entier pair ")
    else :
        print (" Entier impair ")        

from math import *
def test_exo_1_18():
    # Affichage du menu
    print ("1. Carre ")
    print ("2. Rectangle ")
    print ("3. Triangle rectangle ")
    
    # Saisie du choix utilisateur
    figure = int( input (" Quelle figure :"))

    if figure == 1: # Carre
        cote = float ( input (" Donner la valeur du cote :"))
        print (" Aire = ", cote * cote )
        print (" Perimetre =", cote *4)
    elif figure == 2: # Rectangle
        longueur = float ( input (" Donner la valeur de la longueur :"))
        largeur = float ( input (" Donner la valeur de la largeur :"))
        print (" Aire =", longueur * largeur )
        print (" Perimetre =", 2*( longueur + largeur ))
    elif figure == 3: # Triangle
        cote1 = float ( input (" Donner la valeur du premier cote :"))
        cote2 = float ( input (" Donner la valeur du deuxieme cote :"))
        print (" Aire =", ( cote1 * cote2 ) /2.0)
        print (" Perimetre =", cote1 + cote2 + sqrt ( cote1 * cote1 + cote2 * cote2 ))
    else : # choix invalide
        print (" Cette figure est inconnue ")
