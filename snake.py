import pygame
import random
from pygame.locals import *
from screen import *


class Snake(Screen):

    def  __init__(self, _snake=0, _apple="pomme", _background=0 , _sprite=0, _apple1=0, _snake_x=0, _snake_y = 0, _snake_segments=None, _snake_length=0, _direction_x =0,_direction_y =0, _apple_x=0, _apple_y=0, _running=False, _score=0, _obstacle_x=0, _obstacle_y=0):
        super().__init__()
        self._snake = _snake
        self._apple = _apple
        self._background = _background
        self._sprite = _sprite
        self._apple1 = _apple1
        self._snake_x = _snake_x
        self._snake_y = _snake_y
        self._snake_segments = _snake_segments if _snake_segments is not None else []
        self._snake_length = _snake_length
        self._snake_speed = 7
        self._direction_x = _direction_x 
        self._direction_y = _direction_y 
        self._apple_x = _apple_x
        self._apple_y = _apple_y
        self._running = _running
        self._score = _score
        self._obstacle_x = _obstacle_x
        self._obstacle_y = _obstacle_y
        print("Partie lancée")

    def __del__(self):
        print("Partie terminée")
      
    def game(self):
        pygame.display.set_caption("Snake Game")  # Titre de la fenêtre

        # Chargement des images
        self._background = pygame.Surface(self._screen.get_size())  # Création d'une surface pour le fond
        self._background.fill((0, 0, 0)) # Remplir le fond avec une couleur noire
        self._sprite = pygame.Surface((self._grid_size, self._grid_size))  # Surface pour le serpent
        self._sprite.fill((0, 255, 0))  # Couleur verte pour le serpent
        self._apple1 = pygame.Surface((self._grid_size, self._grid_size))  # Surface pour la pomme
        self._apple1.fill((255, 0, 0))  # Couleur rouge pour la pomme

        # Position initiale du serpent
        self._snake_x = random.randint(0, self._grid_width -1) * self._grid_size  # Position X initiale du serpent
        self._snake_y = random.randint(0, self._grid_height -1)* self._grid_size  # Position Y initiale du serpent
        
        # Initialiser la liste des segments du serpent
        self._snake_segments.append((self._snake_x, self._snake_y))  # Ajoute la position initiale à la liste
        self._snake_length = 1  # Longueur initiale du serpent
        self._snake_speed=7

        # Position de la pomme (initiale)
        self._apple_x = random.randint(0, self._grid_width - 1) * self._grid_size  # Position aléatoire sur l'axe X
        self._apple_y = random.randint(0, self._grid_height - 1) * self._grid_size  # Position aléatoire sur l'axe Y    

        # Position de l'obstacle (initiale)
        self._obstacle_x = random.randint(0, self._grid_width - 1) * self._grid_size  # Position aléatoire sur l'axe X
        self._obstacle_y = random.randint(0, self._grid_height - 1) * self._grid_size  # Position aléatoire sur l'axe Y  

    def lancer_partie(self):
        # Boucle principale du jeu
            self._running = True
            while self._running:
                for event in pygame.event.get():  # Parcours des événements
                    if event.type == pygame.QUIT:  # Si l'utilisateur ferme la fenêtre
                        self._running = False  # Quitter la boucle

                    # Gestion des touches de direction
                    if event.type == KEYDOWN:  # Si une touche est pressée
                        if event.key == K_LEFT and self._direction_x == 0:  # Aller à gauche
                            self._direction_x = -self._grid_size  # Déplacer à gauche d'une case
                            self._direction_y = 0  # Pas de mouvement vertical
                        if event.key == K_RIGHT and self._direction_x == 0:  # Aller à droite
                            self._direction_x = self._grid_size  # Déplacer à droite d'une case
                            self._direction_y = 0  # Pas de mouvement vertical
                        if event.key == K_UP and self._direction_y == 0:  # Aller en haut
                            self._direction_x = 0  # Pas de mouvement horizontal
                            self._direction_y = -self._grid_size  # Déplacer vers le haut d'une case
                        if event.key == K_DOWN and self._direction_y == 0:  # Aller en bas
                            self._direction_x = 0  # Pas de mouvement horizontal
                            self._direction_y = self._grid_size  # Déplacer vers le bas d'une case

                # Mise à jour de la position du serpent
                self._snake_x += self._direction_x  # Met à jour la position X du serpent
                self._snake_y += self._direction_y  # Met à jour la position Y du serpent

                # Vérifie si le serpent sort de l'écran
                if (self._snake_x < 0 or self._snake_x >= self._window_width or
                    self._snake_y < 0 or self._snake_y >= self._window_height):
                    print("Le serpent est sorti de l'écran!")  # Log pour le débogage
                    self._running = False  # Arrêter le jeu si le serpent sort de l'écran

                # Ajouter la nouvelle position à la liste des segments
                self._snake_segments.insert(0, (self._snake_x, self._snake_y))

                # Vérifie si le serpent a mangé une pomme
                if self._snake_x == self._apple_x and self._snake_y == self._apple_y:
                    #print("Pomme touchée")
                    self._score += 1   
                                        # Générer une nouvelle position pour la pomme
                    self._apple_x = random.randint(0, self._grid_width - 1) * self._grid_size
                    self._apple_y = random.randint(0, self._grid_height - 1) * self._grid_size
                    self._snake_length += 1  # Augmenter la longueur du serpent
                    self._snake_speed +=1
                    # Générer une nouvelle position pour l'obstacle
                    self._obstacle_x = random.randint(0, self._grid_width - 1) * self._grid_size
                    self._obstacley = random.randint(0, self._grid_height - 1) * self._grid_size
                else:
                    # Retirer le dernier segment si la pomme n'est pas mangée
                    self._snake_segments.pop()
                
                # Vérifie si le serpent a touché un obstacle
                if self._snake_x == self._obstacle_x and self._snake_y == self._obstacle_y:
                    print("Le serpent a touché un obstacle!")
                    self._running = False  # Arrêter le jeu si le serpent a touché un obstacle                   
                    
                # Dessin des éléments sur l'écran
                self._screen.fill((0, 0, 0))  # Effacer l'écran avec noir
                if (self._snake_x, self._snake_y) in self._snake_segments[1:]:
                    print("Le serpent a touché sa propre queue!")  
                    self._running = False  # Arrêter le jeu si le serpent touche sa queue
                
                 # Dessiner le serpent
                for segment in self._snake_segments:
                    pygame.draw.rect(self._screen, (0, 255, 0), (segment[0], segment[1], self._grid_size, self._grid_size))  # Segment du serpent

                 # Dessiner la pomme
                pygame.draw.rect(self._screen, (255, 0, 0), (self._apple_x, self._apple_y, self._grid_size, self._grid_size)) # Pomme
                
                 # Dessiner l'obstacle
                pygame.draw.rect(self._screen, (0, 149, 182), (self._obstacle_x, self._obstacle_y, self._grid_size, self._grid_size)) # Obstacle

                pygame.display.update()  # Met à jour l'affichage
                
                # Limiter la vitesse du jeu
                pygame.time.Clock().tick(10)  
            print ("Score = ",end="")    
            print(self._score)      
                
    def quitter_partie(self):
        # Quitter Pygame
        pygame.quit()  # Ferme Pygame lorsque la boucle est terminée


