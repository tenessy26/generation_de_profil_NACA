# Programme de calcul des points de coordonnées d'un profil d'aile selon les spécifications données par l'utilisateur

import numpy as np
import matplotlib.pyplot as plt
def afficher_forme_profil(intrados, extrados):

    # Paramètres du graphique
    plt.rcParams['font.size'] = 10
    plt.rcParams['figure.autolayout'] = True  # s'assure que tout rentre dans la figure
    plt.rcParams['figure.dpi'] = 90

    # Bloc de code pour le trace des courbes
    plt.plot(extrados[:,0], extrados[:,1])  # on trace la courbe de l'extrados
    plt.plot(intrados[:,0], intrados[:,1])  # on trace la courbe de l'intrados

    plt.legend(["extrados", "intrados"], loc="upper right")
    plt.xlabel('coordonnées en x')  # on définit le label de l'axe x
    plt.ylabel('coordonnées en y')  # on définit le label de l'axe y
    plt.grid()  # on spécifie que l'on veut une grille
    plt.title("Forme du profil d'aile symétrique")
    plt.show()  # on affiche la courbe pour l'objet plt
    return
def calculer_position_max(up,down,nb_points,longueur_corde):

    # Calcul et affichage de l'épaisseur max
    max = np.max(up[:,1])  # extraction de la valeur max de l'extrados en y
    min = np.min(down[:,1]) # extraction de la valeur max de l'intrados en y
    epaisseur = max - min # obtention de la distance entre ymax et ymin
    print("L'épaisseur max du profil d'aile calculé est de " + str(epaisseur) + " mètres.\n")

    # Calcul et affichage de la position de ce max
    indice_max = np.argmax(up[:,1]) # extraction de l'indice de la valeur max de l'extrados en y (le profil est symétrique donc on a besoin seulement d'un seul tableau)
    pourcentage_de_corde = (indice_max*100)/nb_points  # Calcul de sa valeur en pourcentage de corde
    position_max = (pourcentage_de_corde*longueur_corde)/100
    print("La position de ce maximum est à " + str(pourcentage_de_corde) +"% de la longueur totale de la corde, soit à "+str(position_max)+" mètres.")
    return
def construire_tableau(num_profil = '0033',longueur_corde = float(6), nb_points = 150, distrib_type = "linéaire"):

    xx = num_profil[-2] + num_profil[-1]  # On récupère seulement les 2 derniers éléments du numéro de profil
    t = float(xx) / 100.0

    if distrib_type == 'linéaire':       # Choix du type de distrib comme précisé dans l'énoncé
        xc = np.linspace(0, 1, nb_points)   # On utilise la méthode 'linspace()' pour créer notre vecteur de 'nb_points' valeurs entre 0 et 1
    elif distrib_type == 'non-uniforme':
        teta = np.linspace(0, np.pi, nb_points)
        xc = 0.5 * (1 - np.cos(teta))

    up = np.zeros((nb_points,2),dtype=float)  # initialisation du nparray pour les coordonnnées de l'extrados
    down = np.zeros((nb_points,2),dtype=float) # initialisation du nparray pour les coordonnnées de l'intrados

    for i in range(len(xc)):   # Affectation des valeurs grace aux formules donnés dans l'énoncé
        yt = 5 * t * (0.2969 * np.sqrt(xc[i]) - 0.1260 * xc[i] - 0.3516 * xc[i] ** 2 + 0.2843 * xc[i] ** 3 - 0.1036 * xc[i] ** 4)
        xup = xc[i]*longueur_corde

        up[i,0] += float(xup)       # 1 ere colonne stockant les valeurs sur l'axe x
        up[i,1] += float(yt*longueur_corde)  # 2 ème colonne stockant les valeurs sur l'axe y
        down[i,0] += float(xup)     # 1 ere colonne stockant les valeurs sur l'axe x
        down[i,1] += float(-yt*longueur_corde)  # 2 ème colonne stockant les valeurs sur l'axe y (profil symétrique donc on change simplement le signe de y)

    calculer_position_max(up, down, nb_points, longueur_corde)
    afficher_forme_profil(down, up)
    return

def main():

    #num_profil = input("Saississez le numéro du profil NACA a 4 chiffres symétrique : ")
    #longueur_corde = float(input("Entrez la longueur de la corde du profil (en mètre): "))
    #nb_points = int(input("Choisissez le nombre de points souhaité le long de la corde pour le tracé: "))
    #distrib_type = input("Choisissez un type de distribution (linéaire ou non-uniforme): ").strip().lower()
    construire_tableau()
    return

main()