from personnage import personnage ;
from chargement import * ;
from commande import commande;
import questionnaire

def main():
    personom = input("Donner le nom de votre personnage\n")
    com = commande()
    perso = personnage(personom)
    print("Bienvenue",perso, ", tu es dans le monde du numérique et tu viens de découvrir tes pouvoirs d'informaticien. Un monde magique et immense s'ouvre à toi. Mais prend garde a l'innommable ...")
    print("Eh Oh", perso.nom, ", utilise le sort ls pour voir les choses interessante autour de toi !\n\n")
    lieux,even = chargement_principal()
    perso.lieu = lieux[0]

    perso.maison = lieux[0]
    entre = None
    while entre != "exit":
        entre = input(">")
        if entre != "exit":
            if entre == "examen":
                exam = questionnaire.questionnaire(perso)
                print(exam.start())
                entre = "exit"
            else:
                flag = even.lancement(entre,perso)
                if flag :
                    com.lancement(entre, perso)

main()


# mettre les indicateur de modif diectement dans les objets (ajout de systeme de droit plus complet et simple)
