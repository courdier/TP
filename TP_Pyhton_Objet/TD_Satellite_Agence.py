#======================================================================
# Programme Satellite-Agence TD RNET Geomatique
#======================================================================

#-------------------
# classe Satellite :
#-------------------
# tout objet satellite est identifié par un idSat et est caractérisé par un poids et une orbite,
# un satellite peut être géré par une seule agence 
class Satellite:

    def __init__(self, unId, unPoids, uneOrbite, uneAgence=0):
        self.idSat=unId
        self.poids=unPoids
        self.orbite= uneOrbite
        self.agency=uneAgence

    def __str__(self):
        return "Satellite : {0}, poids : {1}, orbite : {2}".format(self.idSat, self.poids, self.orbite)

    def connectSatToAgence(self, uneAgence):
        self.agency=uneAgence
        uneAgence.connectSatToAgence(self)

    def getId(self):
        return self.idSat
        
#----------------
# classe Agence :
#----------------
# tout objet Agence est identifié par un nom, une agence peut gérer plusieurs objets Satellite
class Agence:
    def __init__(self, nom):
        self.name=nom
        self.listSatellites=[]

    def __str__(self):
        return self.name + " [" + self.getListSatId() + " ]"

    def connectSatToAgence(self, unSatellite):
        self.listSatellites.append(unSatellite)

    def getListSatId (self):
        strListSatId = ""
        for sat in self.listSatellites:
            strListSatId= strListSatId + " " + sat.getId()
        return strListSatId
    
    def printListSat(self):
        if self.listSatellites==[]:
            print ("L'agence", self.name , "ne gére aucun satellite")
        else:
            print ("Satellites gérés par l'agence : ", self.name)
            for sat in self.listSatellites:
                print("   - ", sat)
        
#======================================================================
# programme principal
#======================================================================
# creation des objets satellites et d'une agence
sat1 = Satellite("RP24", 250, 700)
sat2 = Satellite("RP25", 400, 650)
age1 = Agence("CNES")

# affichage des objets créés
print ("liste des objets crées")
print(" - satellite 1 :", sat1)
print(" - satellite 2 :", sat2)
print(" - agence 1 :", age1)
age1.printListSat()

# connection des satellites à leur agence 
sat1.connectSatToAgence(age1)
sat2.connectSatToAgence(age1)

# affichage des info relatives à l'agence age1
age1.printListSat()
print(age1)

#================== FIN DU PROGAMME Satellite-Agence ==================
       
