### Exercice 1 ###
### Cette classe permet de gérer un tableau de citations ###
### Elle permet d'afficher une citation aléatoire, ou d'en ajouter une ###
### Elle est appelée dans le fichier Main.py ###
### Elle utilise la librairie random présente par défaut dans python ###

import random 

class exoTableau:
    # déclaration du tableau de valeurs en statique pour l'exercice
    tab = [
        "Pourquoi essayer de faire semblant d'avoir l'air de travailler ? C'est de la fatigue inutile ! -Pierre Dac",
        "Un concerné n'est pas obligatoirement un imbécile encerclé. -Pierre Dac",
        "La vie est un mystère qu'il faut vivre, et non un problème à résoudre. -Gandhi",
        "J'ai la Gaule les gars! -Jules César",
        "Faire les soldes c'est comme draguer bourré. Tu finis avec des trucs que t'aurais jamais ramené à la maison dans des conditions normales. -Fussoir",
        "Je pense que les week-ends sont fabriqués Chine cars ils durent jamais assez longtemps. -Fussoir",
    ]
    
    # décalration des getter et setter pour le tableau
    def getTab(self):
        return self.tab
    
    def setTab(self, tab):
        self.tab = tab


    # déclaration des méthodes de la classe

    # méthode d'affichage d'une citation aléatoire
    def affichage (self, pointer):
        print ("Citation n°", pointer+1, ":", end="\n")
        print(self.getTab()[pointer], end="\n")
        return self.menu()
    
    # méthode d'ajout d'une citation
    def remplissage(self):
        quotes = ""
        verif = 1 
        while ( verif == 1 ):
            quotes = input("entrer une citation, ou 'exit' pour terminer: \n")
            if (quotes == "exit"):
                verif = 0
            else:
                tab = self.getTab() + [quotes]
                self.setTab(tab)
                print("Citation ajoutée avec succès !" , end="\n")
        
        return self.tab, self.menu()


    # méthode de sélection d'une citation aléatoire
    def random(self):
        length = len(self.getTab())
        i = random.randint(0,length-1)
        return self.affichage(i)
    
    # méthode de sélection de l'action a effectuer
    def switch(self, option):
        if (option == "1"):
            return self.random()
        elif (option == "2"):
            return self.remplissage()
        
    
    # méthode d'affichage du menu
    def menu(self):
        print("Bienvenue dans l'exercice n°1 du devoir de python BCI3", end="\n")
        print("Veuillez selectionner une option:", end="\n")
        print("1. Afficher une citation aléatoire", end="\n")
        print("2. Ajouter une citation", end="\n")
        option = ""
        while (option != "1" and option != "2" and option != "exit"):
            print("Tapez 'exit' pour quitter le programme.")
            option = input("Entrer le numéro de l'option: \n")
            if (option == "exit"):
                print("Au revoir !")
                return 
            elif (option != "1" and option != "2"):
                print("Veuillez entrer une option valide !")
            
        return self.switch(option)
    

        
