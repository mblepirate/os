import personnage
import objet
import lieu

class commande:
    def __init__(self):
        self.dico = {"cat":self.cat, "ls":self.ls, "cd":self.cd, "pwd":self.pwd, "mv":self.mv, "cp":self.cp, "grep":self.grep, "rm":self.rm, "mkdir":self.mkdir, "touch":self.touch}
        
    def lancement(self, entre, perso):
        entre = entre.split(" ")
        sudo = 'sudo' in entre
        if sudo:
            entre = entre[1:]
        if (perso.sudo and sudo) or not sudo:
            if not entre[0] in perso.commandes:
                print("Tu ne connais pas ce sort ou il y a autre chose à faire ...")
            else:
                if entre[0] in self.dico.keys():
                    self.dico[entre[0]](entre, perso, sudo)
        else:
            print("Le monde ne vous a pas autorisé à utiliser ce sort ...")
        
    def cat(self, entre, perso, sudo):
        if len(entre) != 2:
            print("Sort cat mal ecris")
        else:
            ok = False
            for i in perso.lieu.objets:
                if entre[1] == i.nom:
                    if not i.secret in [2,3] or sudo:
                        print(i)
                    else:
                        print("Un grand pouvoir vous empeche d'interagir avec ceci")
                    ok = True
                    
            if not ok:
                print("aucun élements avec ce nom")

    def ls(self, entre, perso, sudo):
        if len(entre) == 1 or (len(entre)==2 and entre[1] == "-a"):
            print("-"*30,"\n", "Vous réactivez votre magie pour reveler les éléments important autour de vous")
            if len(entre) == 1:
                perso.lieu.affichage()
            elif entre[1] == "-a":
                perso.lieu.affichagetotal()
        else:
            print("Sort ls mal ecris")

    def cd(self, entre, perso, sudo):
        if len(entre) > 2:
            print("Sort cd mal ecris")
        else:    
            ok = False
            if len(entre) == 1:
                print("vous vous téléporter dans votre chambre")
                perso.lieu = perso.maison
                ok = True
            elif entre[1] == "..":
                print("vous retourner en arrière")
                perso.lieu = perso.lieu.parent
                ok = True
            else:
                for i in perso.lieu.enfants:
                    if entre[1] == i.identite.nom:
                        if not i.secret in [2,3] or sudo:
                            print("vous vous déplacer vers", i.identite.nom, "...")
                            perso.lieu = i
                        else:
                            print("Un grand pouvoir vous empeche d'interagir avec ceci")
                        ok = True
            if not ok:
                print("lieu inaccesible depuis cette endroit")
        
    def pwd(self, entre, perso, sudo):
        if len(entre) != 1 :
            print("Sort pwd mal ecris")
        else:
            print("vous utiliser votre magie pour vous reperer depuis votre chambre")
            print(perso.lieu.chemin())

    def mv(self, entre, perso, sudo):
        if len(entre) < 3:
            print("mauvaise utilisation du sort")
        else:
            okl = False
            oko = False
            for i in perso.lieu.objets:
                if entre[1] == i.nom:
                    oko = True
                    for j in perso.lieu.enfants:
                        if entre[2] == j.identite.nom:
                            if (not i.secret in [0,1,2,3] and not j.secret in [0,1,2,3]) or sudo:
                                perso.lieu.ajout_objet_enfant(i, j.identite.nom)
                                perso.lieu.sup_objet(i.nom)
                            else:
                                print("Un grand pouvoir vous empeche d'interagir avec ceci")
                            okl = True
            if not oko:
                print("l'objet n'est pas present")
            elif not okl:
                print("le lieu n'est pas accessible")
        
    def cp(self, entre, perso, sudo):
        if len(entre) < 3:
            print("mauvaise utilisation du sort")
        elif entre[1] == entre[2]:
            print("le nom de la copie est identique a l'objet de base")
        else:
            oko = False
            for i in perso.lieu.objets:
                if entre[1] == i.nom:
                    if not i.secret in [0,1,2,3] or sudo:
                        perso.lieu.ajout_objet(objet.objet(entre[2], i.text, 4))
                        print("Vous creez une copie de l'objet")
                    else:
                        print("Un grand pouvoir vous empeche d'interagir avec ceci")
                    oko = True
            if not oko:
                print("l'objet n'est pas present")

    # vvv peut etre plus tard dans une seconde version plus abouti vvv
    def grep(self, entre, perso, sudo):
        pass

    def rm(self, entre, perso, sudo):
        ok = False
        cmp = 0
        if entre[1] == "-r" and len(entre) == 3:
            for i in perso.lieu.enfants:
                if entre[2] == i.identite.nom:
                    if not i.secret in [0,1,2,3] or sudo:
                        perso.lieu.enfants.pop(cmp)
                    else:
                        print("Un grand pouvoir vous empeche d'interagir avec ceci")
                    ok = True
                cmp += 1
            if not ok:
                print("le lieu n'existe pas")

        elif len(entre) == 2:
            for i in perso.lieu.objets:
                if entre[1] == i.nom:
                    if not i.secret in [0,1,2,3] or sudo:
                        perso.lieu.objets.pop(cmp)
                    else:
                        print("Un grand pouvoir vous empeche d'interagir avec ceci")
                    
                    ok = True
                cmp += 1
            if not ok:
                print("l'objet n'existe pas")

    def mkdir(self, entre, perso, sudo):
        okl = False
        for i in perso.lieu.enfants:
            if entre[1] == i.identite.nom:
                okl = True
        if okl:
            print("le lieu existe deja")
        else:
            new = lieu.lieu(-1,[], [], objet.objet(entre[1], "lieu que vous avez creer", 0), 4)
            new.parent = perso.lieu
            perso.lieu.enfants.append(new)

    def touch(self, entre, perso, sudo):
        oko = False
        for i in perso.lieu.objets:
            if entre[1] == i.nom:
                oko = True
        if oko:
            print("l'objet existe deja")
        else:
            perso.lieu.ajout_objet(objet.objet(entre[1], "Objet que vous avez creer", 4))

