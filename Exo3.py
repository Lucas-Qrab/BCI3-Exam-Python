### Exercice 3  ###
### Cette classe permet de créer un serveur web, et de récuperer toutes les information du système ###
### Elle est appelée dans le fichier Main.py ###
### Elle utilise les librairies flask et psutil qu'il est nécessaire d'installer, plus d'infos dans le fichier readme.txt ###
### Elle utilise les librairies platform et os présentes par default dans python ###

from flask import Flask, render_template
import os
import psutil
import platform


# configuration de l'environnement de la web app
os.environ['FLASK_DEBUG'] = 'true'
os.environ['FLASK_APP'] = 'Exo3.py'
# création de l'objet flask/déclaration de l'application
app = Flask(__name__)


class SystemInfo():
    # constructeur de la classe
    def __init__(self):
        # récupératio des informations du système
        self.os = platform.system()
        self.architecture = platform.architecture()
        self.machine = platform.machine()
        self.processor = platform.processor()
        self.cpu = psutil.cpu_count(logical=False)
        self.thread = psutil.cpu_count(logical=True)
        self.ram = psutil.virtual_memory().total / 1024 ** 3
        self.ramAvailable = psutil.virtual_memory().available / 1024 ** 3
        self.disk = psutil.disk_usage('/').total / 1024 ** 3
        self.frequency = psutil.cpu_freq().current

    # déclaration des getter pour les informations du système
    def get_os(self):
        return self.os
        
    def get_architecture(self):
        return self.architecture

    def get_machine(self):
        return self.machine

    def get_processor(self):    
        return self.processor

    def get_cpu(self):
        return self.cpu

    def get_thread(self):
        return self.thread

    def get_ram(self):
        return self.ram

    def get_disk(self):
        return self.disk
    
    def get_frequency(self):
        return self.frequency
    
    def get_ramAvailable(self):
        return self.ramAvailable


# création de l'objet systeme pour récupérer les informations du système
systeme = SystemInfo()


# déclaration de la route principale
@app.route('/')
def index():
    # création du container pour les informations du système
    container = {
        "os": systeme.get_os(),
        "architecture": systeme.get_architecture(),
        "machine": systeme.get_machine(),
        "processor": systeme.get_processor(),
        "cpu": systeme.get_cpu(),
        "thread": systeme.get_thread(),
        "ram": systeme.get_ram(),
        "disk": systeme.get_disk(),
        "frequency": systeme.get_frequency(),
        "ramAvailable": systeme.get_ramAvailable()
    }
    # retourne le template index.html avec le container en paramètre
    return render_template('index.html', container=container)
