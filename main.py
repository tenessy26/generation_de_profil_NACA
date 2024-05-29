
def menu():

    num_profil = input("Numéro du profil NACA 4 chiffres symétrique : ")
    longueur_corde = float(input("Corde du profil (en mètre): "))
    num_points = input("Nombre de points le long de la corde pour le tracé: ")
    distrib_type = input("Type de distribution des points (linéaire ou non-uniforme): ").strip().lower()
    return

menu()