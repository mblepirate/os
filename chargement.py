from lieu import lieu
from objet import objet
from evenement import evenement

def chargement_principal():
    dico_objet = chargement_objet()
    lieux = chargement_lieu(dico_objet)
    crea_graphe(lieux)
    even = evenement(chargement_even())

    return lieux, even



def chargement_lieu(dico_objet):
    fichier = open("ressources/lieu.csv", 'r', encoding= "UTF-8")
    liste = [] # liste a renvoyer avec les valeurs demandé
    for i in fichier:
        if len(i)>1:
            liste.append( i.strip().split(";"))
    fichier.close()
    lieux = []
    for i in liste[1:]:
        i[3] = int(i[3])
        if i[1] in dico_objet.keys():
            lieux.append(lieu(i[0], dico_objet[i[1]],[], objet(i[1], i[2], i[3]), i[3]))
        else:
            lieux.append(lieu(i[0], [] ,[], objet(i[1], i[2], i[3]), i[3]))
    return lieux

def chargement_objet():
    fichier = open("ressources/objet.csv", 'r', encoding= "UTF-8")
    liste = [] # liste a renvoyer avec les valeurs demandé
    for i in fichier:
        if len(i)>1:
            liste.append( i.strip().split(";"))
    fichier.close()

    dico_objet = {}
    for i in liste[1:]:
        i[3] = int(i[3])
        if i[1] in dico_objet.keys():
            dico_objet[i[1]].append(objet(i[0], i[2], i[3]))
        else:
            dico_objet[i[1]] = [objet(i[0], i[2], i[3])]
    return dico_objet

def crea_graphe(lieux):
    fichier = open("ressources/graphelieu.txt", 'r', encoding='UTF-8')
    liste = []
    for i in fichier:
        if len(i)>1:
            liste.append(i.strip().split(" "))
    fichier.close()

    for i in liste:
        s = int(i[0])
        for j in i[1:]:
            lieux[s].aj_enfants(lieux[int(j)])
            lieux[int(j)].parents(lieux[s])

def chargement_even():
    fichier = open("ressources/even.csv", 'r', encoding= "UTF-8")
    liste = [] # liste a renvoyer avec les valeurs demandé
    for i in fichier:
        if len(i)>1:
            liste.append(i.strip().split(";"))
    fichier.close()
    return liste[1:]
