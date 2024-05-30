import numpy as np
def afficher_forme_prfil():

    return
def construire_tableau(num_profil,longueur_corde, nb_points, distrib_type):

    xx = num_profil[-2] + num_profil[-1]
    t = float(xx) / 100.0

    if distrib_type == 'linéaire':
        xc = np.linspace(0, 1, nb_points)
    elif distrib_type == 'non-uniforme':
        theta = np.linspace(0, np.pi, nb_points)
        xc = 0.5 * (1 - np.cos(theta))

    up = np.zeros((nb_points,2))
    down = np.zeros((nb_points,2))

    for i in range(len(xc)):
        yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)
        xup = xc[i]*longueur_corde
        up[i] += [xup,yt]
        down[i] += [xup,yt]

    print("Matrice up \n", up)
    print("Matrice down \n", down)
    return

def main():

    num_profil = input("Saississez le numéro du profil NACA a 4 chiffres symétrique : ")
    longueur_corde = float(input("Entrez la longueur de la corde du profil (en mètre): "))
    nb_points = int(input("Choisissez le nombre de points souhaité le long de la corde pour le tracé: "))
    distrib_type = input("Choisissez un type de distribution (linéaire ou non-uniforme): ").strip().lower()
    construire_tableau(num_profil, longueur_corde, nb_points, distrib_type)

    return
