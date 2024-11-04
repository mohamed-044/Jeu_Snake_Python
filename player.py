#import pygame.freetype 
import os
from snake import *

class Player(Snake):
    def __init__(self, _name="Unknown", _score=0, _nbgames=0, _highscore=0, _list_players=None, _score_players=None):
        super().__init__()
        self._name = _name
        input("Nom : ")
        self._score = _score
        self._nbgames = _nbgames
        self.highscore = _highscore
        self._list_players = _list_players if _list_players is not None else []
        self._score_players = _score_players if _score_players is not None else []

    def __del__(self):
        print("Fin")

    def listplayers(self):
        # Charger la liste des joueurs à partir du fichier
        if os.path.exists("names.txt"):
            #print("Le fichier existe")
            with open('names.txt', 'r') as f:
                self._list_players = f.read().splitlines()  # Charger chaque ligne comme un nom de joueur
        else:
            with open('names.txt', 'w') as f:
                f.write("Unknown\n")  # Écrire un joueur par défaut
                self._list_players = ["Unknown"]

        # Ajouter le nom du joueur si non déjà présent dans la liste
        if self._name not in self._list_players:
            self._list_players.append(self._name)
            # Mettre à jour le fichier avec la nouvelle liste de joueurs
            with open('names.txt', 'a') as f:  # 'a' pour append
                f.write(self._name + "\n")

        #print(self.list_players)
        return self._list_players


    def scoreplayers(self):
        # Vérifie si le fichier highscore existe et charge le highscore
        try:
            with open("highscore.txt", "r") as f:
                self._highscore = int(f.read())
        except FileNotFoundError:
            print("Aucun record trouvé, initialisation à 0.")
            self._highscore = 0

        # Compare le score actuel avec le highscore
        if self._score > self._highscore:
            self._highscore = self._score
            print(f"Nouveau record : {self._highscore}")
            # Met à jour le fichier highscore
            with open("highscore.txt", "w") as f:
                f.write(str(self._highscore))
        else:
            print(f"Score actuel : {self._score}")
            print(f" Le record à battre est : {self._highscore}")

        return self._highscore





J1 = Player()
J1.window() 
J1.game()    
J1.lancer_partie()  
J1.quitter_partie()  
J1.listplayers()     
J1.scoreplayers()   
