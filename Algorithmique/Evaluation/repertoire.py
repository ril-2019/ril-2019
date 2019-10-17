"""
Construire un algorithme, sous forme pseudo-code, permettant de calculer la taille d'un répertoire. Cet algorithme prendra en paramètre une variable de type repertoire.

La taille d'un répertoire est égale à la somme de la taille de ses sous-répertoires et de ses fichiers.

La profondeur de l'arborescence n'est pas connue.

Outre les types standards (entier, car, booléen, réel), vous pouvez utiliser les 3 types spécifiques suivants:

    repertoire: représente un répertoire dans une arborescence de fichiers
    fichier: représente un fichier dans une arborescence de fichiers
    element: représente un élément du système de fichiers, qui peut être un repertoire ou un fichier

Outre les opérateurs arithmétiques courants (+-/*) et les structures de base de l'algorithmique, vous pouvez utiliser les instructions spécifiques suivantes:

    récupérerContenu(repertoire):tableau[]d'element
        renvoie un tableau d'element
        le paramètre doit être un repertoire
    estRepertoire(element):booléen
        renvoie vrai si element est un repertoire
        renvoie faux si element est autre chose qu'un repertoire
    tailleFichier(fichier):entier
        renvoie la taille du fichier passé en paramètre


Le pseudo-code est à rendre au format texte, avec l'extension .txt (attention à l'indentation, respecter au maximum la syntaxe exalgo).
"""

import os
import os.path
from os import walk 

def tailleRepertoire(dir):
    contenu = os.listdir(dir)
    taille = 0

    for (dirpath, dirnames, filenames) in walk(dir):
        for f in filenames:
            if (os.path.isfile(dirpath + '\\' + f)):
                taille += os.stat(contenu[i]).st_size
            else:
                taille = tailleRepertoire(os.path.abspath(contenu[i]))
            print(dirpath)
            print(filenames)

    return taille
print('Taille :', tailleRepertoire('C:\\Users\\strus\\OneDrive\\Code\\CESI\\ril-2019'))