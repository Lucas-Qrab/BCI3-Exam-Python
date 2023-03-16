### fichier Maitre du devoir de python BCI3 ###
### Il permet de lancer les exercices 1, 2 et 3 ###
### Il utilise les fichiers Exo1.py, Exo2.py et Exo3.py ###
### Auteur: Barq Lucas ###

from Exo1 import exoTableau
import json 
from Exo2 import ExoDictionnaire
import Exo3 as exo3


# Mise en place du menu de démarrage permettant de naviguer entre les exercices 
print("Bienvenue dans le programme du devoir de python BCI3", end="\n")
print("Veuillez selectionner un exercice:", end="\n")
print("1. Exercice 1", end="\n")
print("2. Exercice 2", end="\n")
print("3. Exercice 3", end="\n")
# récupération de l'exercice à lancer
exo = input("Entrer le numéro de l'exercice: ")

# déclaration des fonctions permettant de lancer les exercices
def exoUn():
    return exoTableau().menu()
def exoDeux():
    return print(json.dumps(ExoDictionnaire().getCompagnon(), indent=4))
def exoTrois():
    exo3.app.run()


# switch permettant de lancer l'exercice demandé
if (exo == "1"):
    exoUn()
elif (exo == "2"):
    exoDeux()
elif (exo == "3"):
    exoTrois()
else:
    print("Veuillez entrer un exercice valide !")
