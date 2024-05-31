import numpy as np
import matplotlib.pyplot as plt
def afficher_forme_profil(intrados, extrados):

    # quelques parametre pour le graphique
    #plt.rcParams['font.size'] = 9
    #plt.rcParams['figure.autolayout'] = True  # s'assure que tout rentre dans la figure
    #plt.rcParams['figure.dpi'] = 100

    # Bloc de code pour le trace
    plt.plot(intrados[:,0], intrados[:,1], label='intrados')  # on trace une courbe
    plt.plot(extrados[:,0], extrados[:,1], label='extrados')  # on trace une autre courbe
    plt.xlabel('x')  # on définit le label de l'axis x
    plt.ylabel('y')  # on définit le label de l'axis y
    plt.legend()  # on spécifie que l'on veut une légende
    plt.grid()  # on spécifie que l'on veut une grille
    plt.title("Forme du profil d'aile")  # on spécifie que l'on veut un titre
    plt.show()  # on affiche la sourbe pour l'objet plt en cours de modification
    return
def construire_tableau(num_profil,longueur_corde, nb_points, distrib_type):

    xx = num_profil[-2] + num_profil[-1]
    t = float(xx) / 100.0

    if distrib_type == 'linéaire':
        xc = np.linspace(0, 1, nb_points)
    elif distrib_type == 'non-uniforme':
        theta = np.linspace(0, np.pi, nb_points)
        xc = 0.5 * (1 - np.cos(theta))

    up = np.zeros((nb_points,2),dtype=float)
    down = np.zeros((nb_points,2),dtype=float)

    for i in range(len(xc)):
        yt = 5 * t * (0.2969 * np.sqrt(xc[i]) - 0.1260 * xc[i] - 0.3516 * xc[i] ** 2 + 0.2843 * xc[i] ** 3 - 0.1036 * xc[i] ** 4)
        xup = xc[i]*longueur_corde

        up[i,0] += float(xup)
        up[i,1] += float(yt*longueur_corde)
        down[i,0] += float(xup)
        down[i,1] += float(-yt*longueur_corde)

    afficher_forme_profil(up, down)

    return

def main():

    num_profil = input("Saississez le numéro du profil NACA a 4 chiffres symétrique : ")
    longueur_corde = float(input("Entrez la longueur de la corde du profil (en mètre): "))
    nb_points = int(input("Choisissez le nombre de points souhaité le long de la corde pour le tracé: "))
    distrib_type = input("Choisissez un type de distribution (linéaire ou non-uniforme): ").strip().lower()
    construire_tableau(num_profil, longueur_corde, nb_points, distrib_type)
    return

main()