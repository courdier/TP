
#Pour importer la librairie Python SQLite:
import sqlite3
import os
# from sqlite3 import *


import sqlite3 # cette librairie permettra toute les opréation relative à la manipulation de BD sqlite
import os # cette librairtie sera utiliser pour gerer un répertoire sur votre disque pour stocker votre base de données

DirBD = "data" # Nom du répertoire de stockage 

# FONCTION CreerDirData
# creation du répertoire de stockage de la base de données
def creerDirData():
    os.makedirs(DirBD, exist_ok=True)
    try: # si il y a des erreurs dans les instructions dans ce bloc, le bloc "except" sera invoqué
        print ('-> Repertoire "'+ DirBD + "'créé ou exitant")
    except Exception as err:
        print(err)  # affichage de l'erreur
        exit()      # sortie du programme

#FONCTION creerBD
# Création d'une base de données avec SQLite
# Création d'un fichier nommé maBD.bd dans un répertoire Data existant
# retour :
# - conn : ma Base de Donnée nouvellement créée
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
    
#PROCEDURE creerTableVille
# Création d'une table dans une base de données avec SQLite
# paramètre :
# - conn : ma Base de Donnée courante
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

#PROCEDURE supTableVille  
# Suppression d'une table dans une base de données avec SQLite
# paramètre :
# - conn : ma Base de Donnée courante
def supTableVille(conn):
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE VILLE""")
    conn.commit()
    print ('->Table VILLE supprimmée)

#PROCEDURE error  
# fct d'affich. message & exit
# paramètre :
# - mess : le message à afficher
def error(msg): # 
    sys.stderr.write("Error: %s\n" % msg)
    sys.exit('Aborting...')

    
#DEBUT ===================================================

# ouverture ou creation de maBD
maBD=creeBD()

#creation de la table VILLE dans maBD
creerTableVille(maBD)

cursor = maBD.cursor()
cursor.execute("""SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';""")
print("Liste des Tables de la Base de Donnees : ")
print('  ',cursor.fetchall())
print("----")

#Insérer des données
cursor.execute("""INSERT INTO VILLE(name, nombre_habitants) VALUES(?, ?)""", ("Saint-Denis", 147931))

#plusieurs insert en une seule fois avec la fonction executemany
villes = []
villes.append(("Saint-Pierre", 84212))
villes.append(("Saint-Benoit", 37759))
cursor.executemany("""INSERT INTO VILLE(name, nombre_habitants) VALUES(?, ?)""", villes)


#===Récupérer des données de la BD===
#récupération du premier tuple de la BD correspondant à la sélection
cursor.execute("""SELECT name, nombre_habitants FROM VILLE""")
ville1 = cursor.fetchone()
print("Affiche le premier tuple de la table VILLE : ")
print('  ',ville1)
print("----")

#récupération de la liste de tous les tuples d'une table d'une BD
cursor.execute("""SELECT name, nombre_habitants FROM VILLE""")
print("Affiche la liste de tous les tuples de la table VILLE : ")
print('  ', cursor.fetchall())
print("----")

print("Liste des villes :")
cursor.execute("""SELECT id, name, nombre_habitants FROM VILLE""")
for row in cursor:
    print('  {0} - nom : {1}, Nb habitants : {2}'.format(row[0], row[1], row[2]))
print("----")
    
#recherche spécifique, utilisation de la même logique vu précédemment:
id = 2
cursor.execute("""SELECT id, name, nombre_habitants FROM VILLE WHERE id=?""", (id,))
response = cursor.fetchone()
print("Recherche du tuple de la table VILLE dont l'identifiant est : ", id)
print("  SELECT id, name, nombre_habitants FROM VILLE WHERE id=2")
print("  réponse = " , response)
print("---")

#validationdes transaction faite dans la BD
# création d'un fichier temporaire nommé nomdeBD.bd-journal dans le répertoire courant
maBD.commit()

#Modification d'un tuple de la BD
cursor.execute("""UPDATE VILLE SET nombre_habitants = ? WHERE id = 2""", (31000,))
id = 2
cursor.execute("""SELECT id, name, nombre_habitants FROM VILLE WHERE id=?""", (id,))
response = cursor.fetchone()
print("Affiche un tuple spécifique apres modification de valeur de la table VILLE :")
print("  UPDATE VILLE SET nombre_habitants = ? WHERE id = 2, (31000,)")
print("  SELECT id, name, nombre_habitants FROM VILLE WHERE id = 2", response)
print("---")

#retour au dernier commit
maBD.rollback()

#récupération des tuples de la BD correspeonfant à la sélection
#on constate que la modication faite après le commit a été invalidée
print("Affiche la table VILLE 'récupée' suite à un rollback: ")
cursor.execute("""SELECT id, name, nombre_habitants FROM VILLE""")
for row in cursor:
    print('  {0} : {1}, {2}'.format(row[0], row[1], row[2]))
print("---")

#suppression de la table VILLE de la BD
supTableVille(maBD)
    
#Gestion des erreurs
#la mise à jour de la table supprimée provoque maintenant une erreur 
try:
    #actions susceptibles de lancer une exception
    cursor.execute("""UPDATE VILLE SET nombre_habitants = ? WHERE id = 2""", (31000,))
except sqlite3.OperationalError:
    #actions de gestion de l'exception
    print("Impossible de faire l'opération de mise à jour de données")
finally:
    #actions toujours exécutées qu'il y ait exception ou non
    print("Passage tjs exécuté")

maBD.close()

#FIN ===============================================
