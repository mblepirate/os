import objet

class lieu:
    def __init__(self,id, lobjet, commandes, identite, secret):
        self.secret = int(secret)
        self.identite = identite
        self.objets = []
        self.parent = None
        self.enfants = []

        self.objets = lobjet

        self.commandes = commandes


    def affichage(self):
        print(self.identite.nom, "\n", self.identite.text, "\n Lieux : ", )
        for i in self.enfants:
            if not i.secret in [1,3]:
                print(" "*10,i.identite.nom)
        print("Visible : ")
        for i in self.objets:
            if not i.secret in [1,3]:
                print(" "*10,i.nom)

    def affichagetotal(self):
        print(self.identite.nom, "\n", self.identite.text, "\n Lieux : ", )
        for i in self.enfants:
            print(" "*10,i.identite.nom)
        print("Visible : ")
        for i in self.objets:
            print(" "*10,i.nom)

    def parents(self, parent):
        self.parent = parent

    def aj_enfants(self, enfant):
        self.enfants.append(enfant)

    def chemin(self):
        if self.parent == None:
            return "/" + self.identite.nom 
        else:
            return  self.parent.chemin() + "/" + self.identite.nom

    def ajout_objet(self, objet):
        # ajoute un objet dans la liste des objets
        self.objets.append(objet)

    def ajout_objet_enfant(self, objet, nomlieu):
        # ajout un objet dans un lieu enfants a l'aide du nom du lieu
        for i in self.enfants:
            if i.identite.nom == nomlieu:
                i.ajout_objet(objet)

    def sup_objet(self, nom):
        # supprimer un objet a l'aide du nom de la liste des objets
        for i in self.objets:
            if i.nom == nom:
                self.objets.remove(i)
    
    def presence(self, nom):
        # renvoie un bool en fonction de la presnce de l'objet rechercher
        for i in self.objets:
            if i.nom == nom:
                return True
        return False

    def renvoie_objet(self, nom):
        for i in self.objets:
            if i.nom == nom:
                return i
        return None
        
    def renvoie_lieu(self, nom):
        for i in self.enfants:
            if i.identite.nom == nom:
                return i
        return None