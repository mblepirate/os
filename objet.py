class objet:
    def __init__(self, nom, text, secret):
        self.secret = int(secret)
        self.nom = nom
        self.text = text
    
    def __str__(self):
        return self.nom + " : " + self.text



billy = objet("Billy","Aller suis moi dans la ville, on va etre en retard sinon !", 0)
#exec("billy."+ dir(billy)[-2]+"()")