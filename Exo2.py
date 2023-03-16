### Exercice 2  ###
### Cette classe permet de gérer un dictionnaire ###
### Elle est appelée dans le fichier Main.py ###
### Elle utilise la librairie json présente par défaut dans python ###

class ExoDictionnaire:
    # constructeur de la classe
    def __init__(self):
        # déclaration du dictionnaire pour l'exercice 
        proprietaire = {
            "nom" : "Fussoir",
            "adresse" : "Rue de la paix",
            "ville" : "Paris",
            "code postal" : 75000,
            "pays" : "France",
            "telephone" : 123456789,
        }
        self.compagnon = { 
            "nom" : "Rex",
            "age" : 3,
            "espece" : "chien",
            "race" : "berger allemand",
            "couleur" : "noir et blanc",
            "poids" : 30,
            "taille" : 70,
            "proprietaire" : proprietaire
        }
    
    # déclaration des getter et setter pour le dictionnaire
    def getCompagnon(self):
        return self.compagnon
    
    def setCompagnon(self, compagnon):
        self.compagnon = compagnon


    

        
