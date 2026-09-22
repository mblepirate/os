import personnage
from random import *

class questionnaire:
    def __init__(self, perso):
        self.nom = perso.nom
        self.question = []
        base =  [   ["Quelle est la commande qui permet de voir tout les lieux et objets ?",["ls"]],
                    ["Quelle est la commande qui permet de voir tout les lieux et objets y compris les secret ?",["ls","-a"]],
                    ["Je veux creer une planche de même nom",["touch", "planche"]],
                    ["Je veux creer un carnet avec pour nom texte",["touch", "texte"]],
                    ["Je veux dupliquer une planche1 en planche2",["cp","planche1", "planche2"]],
                    ["Je veux dupliquer une planche1 en caisse",["cp","planche1", "caisse"]],
                    ["Je veux déplacer carnet dans le coffre",["mv","carnet", "coffre"]],
                    ["Je veux déplacer planche dans coffre",["mv","planche", "coffre"]],
                    ["Je veux détruire le carnet",["rm","carnet"]],
                    ["Je veux détruire le coffre",["rm","-r","carnet"]],
                    ["Je veux retourner dans ma chambre",["cd"]],
                    ["Je veux revenir un cran en arrière",["cd", ".."]],
                    ["Je veux aller dans la salle_de_destruction",["cd", "salle_de_destruction"]],
                    ["Je veux lire livre_grep",["cat", "livre_grep"]],
                    ["Je veux parler avec Billy",["cat","Billy"]],
                ]
        for i in range(10):
            tmp = randint(0,len(base)-1)
            self.question.append(base[tmp])
            base.pop(tmp)
        

    def start(self):
        compteur = [2,3,5,7,11,13,17,19,23,29]
        for i in range(len(self.question)):
            entre = input(self.question[i][0]+"\n")
            entre = entre.split(" ")
            if entre != self.question[i][1]:
                compteur[i] = 1
        
        tmp = 1
        for i in compteur:
            tmp = i * tmp
        return str(tmp + ord(self.nom[0])*ord(self.nom[1]))