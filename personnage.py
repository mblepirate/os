import lieu

class personnage:
    def __init__(self, nom):
        self.nom = nom
        self.commandes = ["ls", "examen","cd"]
        self.lieu = None
        self.sudo = False
        self.maison = None

    def __str__(self):
        return self.nom

