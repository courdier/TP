#!/usr/bin/env python
# coding: utf-8

#---------------------------------------------------------------------------------------------
# # TD BD Python - Base de Données
# 
# Exercice de manipulation de base de données en Python avec la librairie SQLite
# SQLite a été conçu pour être intégré dans le programme même.
# Pour des projets plus ambitieux le choix de MySQL est plus judicieux.
# Auteur : R. Courdier, Université de la Réunion
# Version du 15 octobre 2021

# ### Le TD consiste à :
# - ETAPE 1 : Utiliser une Librairie de manipulation de base de donnée en python
# - ETAPE 2 : Création d'une base de données 
# - Etape 3 : Créer une table dans la base de donnée
# - ETAPE 4 : Insérer des données dans une base de données
# - ETAPE 5 : Accéder aux données d'une BD
# - ETAPE 6 : Modifier les valeurs d'un tuple dans la BD
# - ETAPE 7 : Gérer la validation et retour en arrière sur les transactions faites dans la BD
# - ETAPE 8 : Fermer d'une base de données

#---------------------------------------------------------------------------------------------
# ## ETAPE 1 : Utiliser une Librairie de manipulation de base de donnée en python
# 
# Import de la librairie Python de manipulation de base de données sqlite et création du répertoire de stockage de la base de données par la fonctin *creerDirData()*

import sqlite3 # cette librairie permettra toute les opréation relative à la manipulation de BD sqlite
import os # cette librairie sera utiliser pour gerer un répertoire sur votre disque pour stocker votre base de données

DirBD = "data" # Nom du répertoire de stockage 

# fonction de création de répertoire de données
def creerDirData():
    try: # si il y a des erreurs dans les instructions dans ce bloc, le bloc "except" sera invoqué
        os.makedirs(DirBD, exist_ok=True)
        print ('-> Repertoire "'+ DirBD + "'créé ou exitant")
    except Exception as err:
        print(err)  # affichage de l'erreur
        exit()      # sortie du programme

creerDirData()


# ### Vérification de votre répertoire
print(os.listdir())
listeFic= os.listdir()
print ("Top ! c'est ok, le répertoire " + DirBD + " est bien dans la liste") if DirBD in listeFic else print("Pas top... vérifier votre code !")     

#---------------------------------------------------------------------------------------------
# # ETAPE 2 : Création d'une base de données 
# Création d'une base de données avec SQLite
# - saisie par l'utilisateur du nom de la base de données à creer
# - appel à a fonction *creerDirData()* par précaution pour la création du répertoire 
# - création de la base de donnée par la fonction ** *connect("NomDeLaBDaCreer")* ** de la librairie sqlite
# ### retour :
# - conn : variable donnant accès à ma Base de Donnée nouvellement créée
def creeBD():  
    try: # si il y a des erreurs dans les instructions dans ce bloc, le bloc "except" sera invoqué
        creerDirData() # creer le répertoire data si il n'exsiste pas
        BDname= DirBD + "/" + input("nom de votre base de données ? ")+".bd"
        conn = sqlite3.connect(BDname)
        print ('-> Base de donnée "'+ BDname + "'créé ou existante")
    except Exception as err:
        print(err)  # affichage de l'erreur
        exit()      # sortie du programme
        
    # ... suite du programme si tout est OK
    return conn # creeBd() retourne une variable donnant accès à ma Base de Donnée nouvellement créée

# ouverture ou creation de maBD
maBD=creeBD()

# ### Vérification de la création de la BD
os.listdir("./data/")

#---------------------------------------------------------------------------------------------
# # Etape 3 : Créer une table dans la base de donnée
# Création de la table VILLE dans votre base de données

def creerTableVille(conn):
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS VILLE(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     nombre_habitants INTEGER
    )
    """)
    conn.commit()
    print ('->Table VILLE créé ou existante')

#creation de la table users dans maBD
creerTableVille(maBD)

# ### Lister les Tables de la Base de Donnees : 
# sélection de toutes les tables de la base de données à l'exception des tables "systèmes" préfixées par "sqlite_" 
def listeTable(cursor):
    cursor.execute("""SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';""")
    print("Liste des Tables de la Base de Donnees : ")
    print('  ',cursor.fetchall())

listeTable(maBD.cursor())

# ### Supprimer une table d'une base de données
# Suppression de la table VILLE dans ma base de données

def supTableVille(conn):
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE VILLE""")
    conn.commit()
    print ('->Table VILLE supprimmée')
    
supTableVille(maBD)

# ### On vérifie la suppression !
listeTable(maBD.cursor())

# ### Bon fini de jouer...on recréé notre table VILLE maitenant ! 
creerTableVille(maBD)
listeTable(maBD.cursor())


#---------------------------------------------------------------------------------------------
# # ETAPE 4 : Insérer des données dans une base de données

# ### Création d'un "curseur"
# Considérez le curseur comme un pointeur vers l’enregistrement actif, similaire à la façon dont un index de tableau pointe vers la valeur à cet emplacement particulier dans le tableau.
cursor=maBD.cursor()

# ### Insertion d'un tuple dans la table VILLE d ela Base de Données
cursor.execute("""INSERT INTO VILLE(name, nombre_habitants) VALUES(?, ?)""", ("Saint-Denis", 147931))

# ### Plusieurs insertions en une seule fois avec la fonction ** *executemany()* **
def addVillesReunion():
    villes = []
    villes.append(("Saint-Pierre", 84212))
    villes.append(("Saint-Benoit", 37759))
    villes.append(("Saint-André", 56268))
    cursor.executemany("""INSERT INTO VILLE(name, nombre_habitants) VALUES(?, ?)""", villes)
addVillesReunion()

#---------------------------------------------------------------------------------------------
# # ETAPE 5 : Accéder aux données d'une BD
# ### Acceder au premier tuple d'une table ** *cursor.fetchone()* **
cursor.execute("""SELECT name, nombre_habitants FROM VILLE""")
ville1 = cursor.fetchone()
print("Le premier tuple de la table VILLE est : ")
print('  ',ville1)

# ### Accéder à la liste de tous les tuples d'une table d'une BD ** *cursor.fetchall()* **

def afficheVille(cursor):
    try:
        cursor.execute("""SELECT name, nombre_habitants FROM VILLE""")
        print("La liste de tous les tuples de la table VILLE est : ")
        print('  ', cursor.fetchall())
    except Exception as err:
        print("*** Err: ", err)  # affichage de l'erreur
        exit()      # sortie du programme
afficheVille(cursor)

# ### Afficher un par un les tuples de la table VILLE sur un format choisi :

print("Liste des villes :")
cursor.execute("""SELECT id, name, nombre_habitants FROM VILLE""")
for row in cursor:
    print('  {0} - nom : {1}, Nb habitants : {2}'.format(row[0], row[1], row[2]))


# ### Recherche de tuples par filtres :
# Recherche spécifique sur une valeur d'une donnée

id = 2
cursor.execute("""SELECT id, name, nombre_habitants FROM VILLE WHERE id=?""", (id,))
response = cursor.fetchone()
print("Recherche du tuple de la table VILLE dont l'identifiant est : ", id)
print("  SELECT id, name, nombre_habitants FROM VILLE WHERE id=2")
print("  réponse = " , response)


# # ETAPE 6 : Modifier les valeurs d'un tuple dans la BD

cursor.execute("""UPDATE VILLE SET nombre_habitants = ? WHERE id = 2""", (31000,))
id = 2
cursor.execute("""SELECT id, name, nombre_habitants FROM VILLE WHERE id=?""", (id,))
response = cursor.fetchone()
print("Affiche un tuple spécifique apres modification de valeur de la table VILLE :")
print("  UPDATE VILLE SET nombre_habitants = ? WHERE id = 2, (31000,)")
print("  SELECT id, name, nombre_habitants FROM VILLE WHERE id = 2", response)

#récupération des tuples de la BD correspeonfant à la sélection
#on constate que la modication faite après le commit a été invalidée
print("Affiche la table VILLE 'récupée' suite à un rollback: ")
cursor.execute("""SELECT id, name, nombre_habitants FROM VILLE""")
for row in cursor:
    print('  {0} : {1}, {2}'.format(row[0], row[1], row[2]))


# # ETAPE 7 : Gérer la Validation et retour en arrière sur les transactions faites dans la BD
# ### Validation des transactions
# Vérifier dans votre répertoire de stockage de votre base de données création d'un fichier temporaire nommé ** *nomdeBD.bd-journal** *
# Ce fichier "journalise" tout ce qui est fait sur la Base de données

os.listdir("./data/")

# validation de tout ce qui a été fait jusqu'à présent sur ma BD
maBD.commit()

# Vérifier maintenant votre répertoire courant, le fichier ** *nomdeBD.bd-journal* ** a été supprimé
os.listdir("./data/")

# je rajoute d'autres villes dans ma base de données
villes = []
villes.append(("Besançon", 251700 ))
villes.append(("Lausanne", 139720))
villes.append(("Paris", 2187526))
cursor.executemany("""INSERT INTO VILLE(name, nombre_habitants) VALUES(?, ?)""", villes)
afficheVille(cursor)


# ### Retour en arrière
# Je m'aperçois que j'ai insérer des villes qui ne sont pas de La réunion et je veux revenir en arriere sur cette opération.
# Je ne veux pas que l'opération soit prise en compte pour les autres utilisateurs de base de données

#retour au dernier commit
maBD.rollback()

# ### Vérification du retour arriere
afficheVille(cursor)


# ### Gestion d'erreurs 
# Ici on utilise une table qui n'existe pas dans notre base de données

#la mise à jour de la table supprimée provoque maintenant une erreur 
try:
    # actions susceptibles de lancer une exception
    # ici la table "COMMUNE" n'exsite pas dans notre base de données 
    # et effectivement une exception sera générée
    cursor.execute("""UPDATE COMMUNE SET nombre_habitants = ? WHERE id = 2""", (200000,))
except sqlite3.OperationalError:
    #actions de gestion de l'exception
    print("*** ERROR : Impossible de faire l'opération de mise à jour de données")
finally:
    #actions toujours exécutées qu'il y ait exception ou non
    print("Vous avez souhaité mettre à jour la base de données en montrant une erreur")

# ### Après  correction....
try:
    #actions susceptibles de lancer une exception
    cursor.execute("""UPDATE VILLE SET nombre_habitants = ? WHERE id = 2""", (200000,))
except sqlite3.OperationalError:
    #actions de gestion de l'exception
    print("Impossible de faire l'opération de mise à jour de données")
finally:
    #actions toujours exécutées qu'il y ait exception ou non
    print("Vous avez souhaité mettre à jour la base de données sans montrer d'erreur")

afficheVille(cursor)


# # ETAPE 8 : Fermer d'une base de données
# La base de données peut etre aceede par plusieurs programmes il est important de la fermer lorsque l'on a plus d'action à réaliser dessus avec la fonction ** *close()* **

maBD.close()

# ### Maintenant on ne peu plus faire d'opération sur cette base de donnée...
# cette instruction affichera un message erreur de l'environnement python
afficheVille(cursor)

#---------------------------------------------------------------------------------------------
#                                           Fin
#---------------------------------------------------------------------------------------------