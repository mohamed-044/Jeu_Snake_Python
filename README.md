# Snake en Python

Ce projet consiste à recréer le célèbre jeu **Snake** en utilisant le langage Python et la librairie graphique [Pygame](https://www.pygame.org/docs/). Le jeu propose des fonctionnalités de contrôle du serpent, de collecte de pommes, et des défis croissants en fonction de la taille et de la vitesse du serpent.

## Fonctionnalités

1. **Contrôles Simples**
   - Le joueur contrôle un serpent qui se déplace dans quatre directions : haut, bas, gauche et droite.
   - Le changement de direction est instantané lorsque le joueur appuie sur une touche de direction.

2. **Collecte de Pommes**
   - L'objectif du jeu est de diriger le serpent pour qu'il mange des pommes.
   - Chaque pomme mangée fait grandir le serpent d'une case.
   - Le score augmente à chaque pomme collectée.

3. **Croissance du Serpent**
   - À chaque pomme consommée, le serpent s'allonge, augmentant ainsi la difficulté du jeu, car il devient plus difficile de se déplacer sans se heurter à soi-même.

4. **Évitement des Obstacles**
   - Le serpent ne doit pas entrer en collision avec son propre corps, sinon c'est la fin de la partie.
   - Une version avancée du jeu peut inclure des obstacles supplémentaires, comme des murs ou des barrières fixes, pour rendre le jeu plus difficile.

5. **Vitesse Évolutive**
   - La vitesse du serpent augmente progressivement au fur et à mesure que le joueur avance, rendant le jeu plus difficile.

6. **Scoring et Leaderboard**
   - Le score est basé sur la quantité de pommes consommées ou la longueur atteinte par le serpent.
   - Une version plus avancée peut inclure un système de leaderboard pour suivre les meilleurs scores.

## Prérequis

- **Python 3.x**
- **Pygame** : Vous pouvez installer la librairie en utilisant la commande suivante :
  ```bash
  pip install pygame

## Installation et Lancement

  Clonez le repository :

    git clone https://github.com/mohamed-044/Jeu_Snake_Python.git
    cd snake-game

## Exécutez le jeu :

    python snake.py

## Instructions de Jeu

  Utilisez les touches de direction (Flèche Haut, Flèche Bas, Flèche Gauche, Flèche Droite) pour contrôler le mouvement du serpent.
  Mangez les pommes pour grandir et augmenter votre score.
  Évitez de heurter les murs (si activés) et de toucher votre propre corps, sinon la partie se termine.
  Le jeu devient progressivement plus rapide, testez vos réflexes pour atteindre le meilleur score possible !

## Améliorations Futures (Suggestions)

  Ajout d'obstacles : Intégrer des obstacles fixes dans le champ de jeu pour augmenter la difficulté.
  Leaderboard : Ajouter un leaderboard pour sauvegarder les meilleurs scores.
  Différents niveaux de difficulté : Offrir différents niveaux de difficulté avec des paramètres de vitesse et des tailles de plateau variables.

## Captures d'Écran

![Capture d’écran du 2024-11-04 16-52-04](https://github.com/user-attachments/assets/464b93df-4a33-4d71-b774-e0738fd6a635)

![Capture d’écran du 2024-11-04 16-51-08](https://github.com/user-attachments/assets/24f3b366-99c0-4c8b-9243-add35c44070b)

## Contribuer

Les contributions sont les bienvenues ! N'hésitez pas à soumettre des issues pour proposer des améliorations ou des pull requests pour ajouter de nouvelles fonctionnalités.  
