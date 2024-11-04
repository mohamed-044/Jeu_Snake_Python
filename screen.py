import pygame
import random
from pygame.locals import *

class Screen:

    def  __init__(self, _grid_size =0, _grid_width=0 , _grid_height=0, _screen_info=0, _screen_width=0, _screen_height=0, _window_width=0, _window_height=0, _screen=0 ):
        self._grid_size = _grid_size
        self._grid_height = _grid_height 
        self._grid_width = _grid_width
        self._screen_info = _screen_info
        self._screen_width = _screen_width
        self._screen_height = _screen_height
        self._window_width = _window_width
        self._window_height = _window_height
        self._screen = _screen

        print("Fenetre lancé")
    
    def __del__(self):
        print("Fenetre fermée")

    def window(self):
        #p1= Screen()
        pygame.init() # Initialisation de Pygame
        self._screen = pygame.display.set_mode((self._window_width, self._window_height))     # Création de la fenêtre
        self._screen_info = pygame.display.Info()    # Récupérer la résolution de l'écran
        self._screen_width = self._screen_info.current_w   # Largeur actuelle de l'écran
        self._screen_height = self._screen_info.current_h  # Hauteur actuelle de l'écran
        # Définir la taille de la grille
        self._grid_size = 30
        self._grid_width = 12
        self._grid_height = 12
        
        # Créer une fenêtre légèrement plus petite que l'écran
        self._window_width = self._screen_width -100        # Créer une fenêtre légèrement plus petite que l'écran
        self._window_height = self._screen_height-100       # Réduit la hauteur de 100 pixels
        

#p1= Screen()   
#p1.window()  
