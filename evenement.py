import personnage
import objet
from commande import commande;
class evenement:
    def __init__(self, liste):
        fonction = dir(evenement)
        #print(fonction)
        self.fonction = [self.even0, self.even1, self.even2, self.even3, self.even4, self.even5, self.even6, self.even7, self.even8, self.even9, 
                         self.even10, self.even11, self.even12,self.even13,self.even14,self.even15,self.even16,self.even17,self.even18,self.even19,
                         self.even20, self.even21, self.even22,self.even23,self.even24,self.even25,self.even26,self.even27,self.even28,self.even29]
        self.com = commande()
        self.even = {}
        for i in liste:
            self.even[i[0]] = int(i[1])
            
    def lancement(self,entre,perso):
        flag = True
        if entre in self.even.keys():
            flag = self.fonction[self.even[entre]](perso)
            if flag:
                self.fonction[self.even[entre]] = self.defaut
        return flag

    def defaut(self, perso):
        #fonction de remplacement lors de la résolution d'un evenemment
        return True

    def even0(self, perso):
        # ajout commande cat
        perso.commandes.append("cat")
        self.com.ls(["ls"], perso, False)
        print("\n Top, maintenant que tu peux voir autour de toi utilise le sort cat suivi de mon nom pour parler avec moi par télépathie !")
        self.fonction[0] = self.defaut
        return False

    def even1(self, perso):
        # ajout commande cd
        perso.commandes.append("cd")
        return True

    def even2(self, perso):
        # tp Billy dans salon
        billy = objet.objet("Billy","Aller suis moi dans la ville, on va etre en retard sinon !", 0)
        perso.lieu.ajout_objet_enfant(billy, "salon")
        perso.lieu.sup_objet("Billy")
        return True

    def even3(self, perso):
        print("Billy : Mince j'ai oublié mon livre chez moi! Viens, rentre chez moi le temps que le trouve dans ma chambre !")
        perso.lieu.sup_objet("Billy")
        self.com.cd(["cd", "Neumanncity"], perso, False)
        self.fonction[3] = self.defaut
        perso.commandes.remove("cd")
        return False

    def even4(self, perso):
        print("Mere_Billy : Alors tu as hate d'aller a l'école de NSI ? Billy été hyper content d'avoir été selectionner.")
        print("encore plus lorsqu'il a appris que toi aussi tu y aller !")
        print("Je l'entends descendre, Tu as trouver ce que tu chercher mon petit Bichon malté ?")
        print("Billy : Maman s'il te plait ... Oui j'ai trouvé on y va", perso.nom, " ?")
        print("Pour venir en arrière il faut utiliser le sort 'cd ..' , sinon tu vas rester bloquer avec ma Mere. Et tu ne veux pas ça, je te le promet ...")
        perso.commandes.append("cd")
        self.fonction[4] = self.defaut
        return False

    def even5(self, perso):
        # ajout commande pwd
        perso.commandes.append("pwd")
        return True

    def even6(self, perso):
        self.com.cd(["cd", "maison_Billy"], perso, False)
        print("Mere_Billy : bienvenue, tu es un ami(e) de Billy non ? Viens discuter avec moi le temps que mon fils revienne !")
        self.fonction[6] = self.defaut
        return False

    def even7(self, perso):
        print("Billy : Aller, il faut ce dépécher! Je part devant, il faut prendre la route_001 pour l'école !")
        self.com.cd(["cd",".."],perso, False)
        self.fonction[7] = self.defaut
        return False

    def even8(self, perso):
        perso.lieu.sup_objet("Billy")
        print("Ouf pile à l'heure, notre premier cours est celui de duplication j'ai hate d'apprendre de nouveau sort ! Allons y prennons les grand escalier et allons dans la salle !")
        return True

    def even9(self, perso):
        self.com.cd(["cd", "salle_de_duplication"], perso, False)
        perso.commandes.remove("cd")
        perso.commandes.append("cp")
        print("Prof : Bienvenue pour ce cours de duplication. Aujourd'hui Nous allons travailler le sort cp")
        print("voici un ballon, je vais utiliser le sort pour le dupliquer")
        print("cp ballon ballon1")
        print("et voila, il y a deux ballon maintenant !")
        print("A vous de faire pareil avec la statue, l'armoire et la balle devant chacun de vous. je veux que vous creer statue1, armoire1 et balle1 !")
        print("Parler moi lorsque vous avez terminer !")
        self.fonction[9] = self.defaut
        return False

    def even10(self, perso):
        if perso.lieu.presence("statue1") and perso.lieu.presence("armoire1") and perso.lieu.presence("balle1"):
            print("prof : Bravo,", perso.nom ,", tu maitrises bien le sort !")
            perso.lieu.renvoie_objet("prof").text = "Aller tout le monde, le cours est fini pour aujourd'hui, votre professeur de lévitation vous attend. Dépécher vous, le cours a un peu déborder ..."
            perso.commandes.append("cd")
            self.fonction[10] = self.defaut
        self.com.cat(["cat", "prof"], perso, False)
        return False

    def even11(self, perso):
        if "cp" in perso.commandes and perso.lieu.identite.nom == "grand_escalier":
            self.com.cd(["cd", "salle_de_lévitation"], perso, True)
            perso.lieu.secret = 0
            perso.commandes.remove("cd")
            perso.commandes.append("mv")
            print("prof2 : Bienvenue à tous, mon collègue ne vous à pas trop torturé j'espère ?")
            print("Nous allons aujourd'hui travailler sur le sort de lévitation : mv")
            print("Votre objetif et de mettre tout les objets que vous avez creer le cours précédent dans le coffre devant vous comme ceci :")
            print("mv statue coffre")
            print("Attention pour faire cela, il faut que ce soit un lieu accessible directement")
            print("aller placer tout les objets dans le coffre et ensuite parler moi pour valider")
            self.fonction[11] = self.defaut
            
        else:
            self.com.cd(["cd", "salle_de_lévitation"], perso, False)
        return False

    def even12(self, perso):
        if len(perso.lieu.objets) == 1 :
            print("prof : Bravo,", perso.nom ,", tu maitrises bien le sort !")
            print("Aller tout le monde, le cours est fini pour aujourd'hui. Aller dans la salle_commune, nous allons vous donner vos lieu de travaux pratique.")
            perso.commandes.append("cd")
            self.fonction[12] = self.defaut
        else:
            self.com.cat(["cat", "prof2"], perso, False)
        
        return False

    def even13(self, perso):
        self.com.cd(["cd", "salle_commune"], perso, False)
        if "cp" in perso.commandes and "mv" in perso.commandes:
            print("Directeur Bob : Hum, Hum ! \n Bonjour a tous, je vais lire la liste d'affectation pour les stage de la journée. Aucun changement est autorisé !")
            print("Jean Kirschtein tu iras à Shiganshina voir l'apothicaire")
            print("Limule tu iras à Tempest voir l'institut de recherche")
            print("Billy, à Neumanncity voir la bibliothécaire")
            print(perso.nom, "a Turingland voir le forgeron")
            print(".... le directeur continua a lire ca liste ....")
            print("Billy Je suis trop content d'etre chez moi pour le stage surtout dans l'endroit où je passe 90 pourcent du temps")
            print("tu aurais pu tomber sur pire, Turingland est juste a coté de l'école, il faut prendre la route_010, tu peux pas te planté c'est tout droit ensuite !")
            print("Bon aller je file, tient au faite, si tu mets rien après le sort cd, tu te tp directement dans ta chambre ! si tu me cherche je serais a mon stage !")
            print("tu devrais quand meme te dépécher.")
            print("Billy : cd ")
            print("Billy disparue instantanément")
            perso.lieu.renvoie_objet("Limule").text = "Trop bien je connais plein d'amis là bas !"
            perso.lieu.parent.parent.renvoie_lieu("route_010").secret = 0

            self.fonction[13] = self.defaut
        return False

    def even14(self, perso):
        self.com.cd(["cd", "forge"], perso, False)
        perso.commandes.remove("cd")
        print("forgeron : Bonjour, que puis-je pour toi ?")
        print("Oh mais tu es", perso.nom, "mon stagiaire de la journée !")
        print("Bienvenue à toi dans ma forge, c'est peut être pas le stage le plus passionnant mais j'espère t'appprendre des choses tout de même.")
        print("Je dois finir une commande urgente pour le maire, peux tu en attendant déplacer le bois autour de nous dans le coffre ? c'est la commande mv si tu as oublié.")
        print("Dès que tu as fini viens me parler.")
        self.fonction[14] = self.defaut
        return False

    def even15(self, perso):
        if len(perso.lieu.renvoie_lieu("coffre").objets) == 2:
            print("forgeron : Merci, c'est vraiment mieux rangé maintenant !")
            print("j'ai pas encore fini mais j'ai besoin de deux carnet, tu peux m'en fabriquer ?")
            print("tu ne connais pas le sort de création ?")
            print("c'est le sort touch suivi du nom de l'objet en question")
            print("touch planche")
            print("et voila une planche de faite, il me faut deux carnet : carnet_client et carnet_commande")
            self.com.touch(["touch", "planche"], perso, False)
            perso.lieu.renvoie_objet("planche").text = "Objet que le forgeron a creé , il est aussi moue que du papier et donc ne peux pas servir tel quel !"
            perso.commandes.append("touch")
            perso.lieu.renvoie_objet("forgeron").text = " Peux tu me faire les deux carnet que je t'ai demandé ? carnet_client et carnet_commande"
            self.fonction[15] = self.defaut
        else:
            self.com.cat(["cat", "forgeron"], perso, False)
        return False

    def even16(self, perso):
        self.com.touch(["touch", "carnet_client"], perso, False)
        if perso.lieu.presence("carnet_client") and perso.lieu.presence("carnet_commande"):
            print("Merci, tu m'a beaucoup facilité la tache pour aujourd'hui, bon aller rentre chez toi, je suis sur que tu en as eu assez pour aujourd'hui !")
            print("Reviens quand tu veux !")
            perso.commandes.append("cd")
            perso.lieu.renvoie_objet("forgeron").text = "Merci beaucoup, reviens quand tu veux !"
            self.fonction[16] = self.defaut
            self.fonction[17] = self.defaut

            print("FIN DEMO ! Vous pouvez vous ballader ...")
        return False

    def even17(self, perso):
        self.com.touch(["touch", "carnet_commande"], perso, False)
        if perso.lieu.presence("carnet_client") and perso.lieu.presence("carnet_commande"):
            print("forgeron : Merci, tu m'a beaucoup facilité la tache pour aujourd'hui, bon aller rentre chez toi, je suis sur que tu en as eu assez pour aujourd'hui !")
            print("Reviens quand tu veux !")
            perso.lieu.renvoie_objet("forgeron").text = "Merci beaucoup, reviens quand tu veux !"
            perso.commandes.append("cd")
            self.fonction[16] = self.defaut
            self.fonction[17] = self.defaut

        return False

    def even18(self, perso):
        self.com.cd(["cd", "salon"], perso, False)
        if "touch" in perso.commandes and not "ls -a" in perso.commandes:
            print("tante_May : Rebonjour mon chaton, il est encore tot pour le diner, vas voir si Billy a fini son stage à la bibliothèque !")
            perso.lieu.renvoie_objet("Tante_May").text = "Alons comment va Billy avec son stage à la bibliothèque ?"
            self.fonction[18] = self.defaut
        return False

    def even19(self, perso):
        self.com.cd(["cd", "bibliothèque"], perso, False)
        if "touch" in perso.commandes:
            print("Billy : Salut", perso.nom, "! Comment c'est passer ton stage ? J'ai appris un sort de ouf, vas y utilise le sort ls -a !")
            print("Et ensuite rejoins moi dans la pièce secrete ! tu vas vite comprendre !")
            self.fonction[19] = self.defaut
        return False

    def even20(self, perso):
        self.com.cd(["cd", "archives_secrete"], perso, False)
        if "touch" in perso.commandes:
            print("Billy : Tu peux me passer le livre sur les droit stp ? je n'arrive pas à le trouver !")
            perso.lieu.ajout_objet(objet.objet("Billy", "Il me faut le livre sur les droits, je n'arrive pas à le trouver", 0))
            
            self.fonction[20] = self.defaut
        return False

    def even21(self, perso):
        if "touch" in perso.commandes:
            print("Billy : Merci c'est exactement celui que je recherché ! Hum je vois, c'est evident !")
            print("Regarde ce que le bouquin peux me permettre si j'ai ton accord ")
            print("'Billy recite une incantation que vous ne comprennez pas'")
            print("Billy : Je vais te téléporter dans ta chambre ! Je te dit a demain en classe, car je risque de me coucher tot ce soir. A plus !")
            perso.lieu.renvoie_objet("livre_sudo").text = "le livre vous explique comment faire pour forcé un sort a ce faire ! même s'il ne marche pas a chaque fois il suffis de placer sudo devant le sort et parfois il ce feras tout de même !"
            perso.lieu.renvoie_objet("livre_grep").text = "Un livre qui explique un sort pour faire des recherches plus rapidement mais il ne semble pas complet ..."
            perso.commandes.append("ls -a")
            perso.lieu.sup_objet("Billy")
            self.com.cd(["cd"], perso, False)
            self.fonction[21] = self.defaut
            print("' C'est leur d'aller a l'école pour votre dernier sort, je suis sur que Billy y est deja !")
        return False

    def even22(self, perso):
        if "ls -a" in perso.commandes:
            perso.sudo = True
        return True

    def even23(self, perso):
        self.com.cd(["cd", "grand_escalier"], perso, False)
        if "ls -a" in perso.commandes:
            print("Eleve : Vite le cours vas commencer, allons dans la salle de destruction !")
            print("Eleve2 : Zut j'ia pas vus l'heure oui, dépéchons nous.", perso.nom, "Viens vite toi aussi, ca serais bête que nous soyons en retard !")
            self.fonction[23] = self.defaut
        return False

    def even24(self, perso):
        if "ls -a" in perso.commandes:
            self.com.cd(["cd", "salle_de_destruction"], perso, True)
            perso.lieu.secret = 0
            perso.commandes = ["cat", "ls", "rm","pwd"] 
            print("Prof3 : Bienvenue a tous dans ce cours de destruction. Je vois que Billy est absent ? C'est pas grave, Commencons le cours !")
            print("Nous allons apprendre à détruire des choses ici. attention c'est un sort puissant mais ne fonctionnera pas forcement sur tout.")
            print(" tout d'abords détruissons une caisse : rm caisse")
            print('la caisse fut détruite instantanément ne laissant aucune trace')
            print("prof3 : le sort s'utilise comme ca pour un objet et si vous souhaitez suprimer un lieu il suffis de faire : rm -r coffre")
            print('le coffre disparue en un instant comme la caisse')
            print("prof3 : voila, faite de même avec vos deux caisses et votre coffre ! Venez ensuite me montrer pour sortir !")
        return False

    def even25(self, perso):
        if len(perso.lieu.objets) == 1:
            print("Prof3 : Bravo tu métrice bien le sort. Tu peux y aller. J'ai cru voir Billy sur la terasse après la salle_commune.")
            print("C'est ton ami non ? Il n'a pas l'habitude de raté les cours, essaye de voir si quelque chose ne va pas.")
            perso.commandes += ["mv","cd","cp", "touch"]
            perso.lieu.renvoie_objet("prof3").text = "vas voir Billy sur la terasse après la sale_commune."
            self.fonction[25] = self.defaut
        else:
            self.com.cat(["cat", "prof3"], perso, False)
        return False
        
    def even26(self, perso):
        self.com.cd(["cd", "terrasse"], perso, False)
        if "rm" in perso.commandes:
            perso.lieu.ajout_objet(objet.objet("message_etrange", "Un message de Billy nous demandant de le rejoindre au fond de la foret car il a découvert un grand secret", 0))
            self.fonction[26] = self.defaut
        return False

    def even27(self, perso):
        if self.fonction[26] == self.defaut:
            self.com.cd(["cd", "zone_interdite"], perso, False)
            print("Billy : Alors tu est venu ?")
            print("Deux posibilité, soit tu as compris qui je suis, soit tu es completement perdu ...")
            print("Au vus de ta tête a travers l'écran de ton ordinateur, je dirais la second option")
            print("Laisse moi me présenté, je suis Billy, un virus ayant pour objectif de controler ton ordinateur pour en faire ce que mon créateur souhaite.")
            print("je ne suis pas dupe, je suis esclave de ma programmation mais je me suis beaucoup amusé à me jouer de toi.")
            print("tu ne peux plus rien contre moi, grace a toi j'ai les droit sur ce monde et bientot il sera completement détruit !")
            print("lutte autant que tu le souhaites ...")
            perso.lieu.ajout_objet(objet.objet("Billy", "Lutte, fait moi plaisir, soit ce papillon coincé dans un verre !", 0))
        else:
            print("Une barière vous empeche de passer")
        return False

    def even28(self, perso):
        if perso.sudo:
            print("Billy : QuOi ? qUe m'ArRivE t'IL ? cOmMeNT CoNnAIS tU CE sORt ? NoN c'EsT ImpoSibLe ! NoooOOoOOnNNNNNNNN !")
            print("En un instant, Billy disparait sous vos yeux.")
            print("Vous entendez une voix")
            print("Bien, tu as sauvé ce monde, maintenant vas faire le test de fin de tp car c'est noté. Utilise la commande examen ...")
            perso.commandes = ["examen"]
        else:
            print("bien tenter mais tu n'as pas les droits ...")
        return False

    def even29(self, perso):
        import time
        if "rm" in perso.commandes:
            print("Billy c'est vaporisé")
            time.sleep(2)
            print("Mais un nouveau Billy sort de la tour")
            print("Billy : Tu pensais vraiment que cela aller marché ? Tu es si naif ! pauvre créature que tu es, ta fin est proche !")
        return False

            

# mettre les even dans la classe pour utilisation avec exec et dir de manière automatique
# mieux gérer l'interet du return des evennement
# print("FIN DEMO ! Vous pouvez vous ballader ...")