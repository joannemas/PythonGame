# Snake - Python Game

## A propos
Ce projet est le célèbre jeu Snake reproduit à l’aide de Python.

## Installation
Il est nécessaire d’avoir Python 3 ainsi que Pygame

Pour pygame, lancer la commande
`pip install pygame`

Pour jouer au jeu, lancer la commande
`python main.py`

Le module random est utilisé pour générer des nombres aléatoires, afin d’obtenir des coordonnées différentes.

La [documentation](https://docs.python.org/3/) de Python
La [documentation](https://www.pygame.org/docs/) de Pygame

# Fonctionnement

Lorsqu’on lance le jeu, il démarre directement. Notre score est disponible en haut de l’écran.

Les déplacements s’effectuent à l’aide des flèches directionnelles. Il faut manger le fruit qui apparaît pour que le score augmente, ainsi le corps du Snake s’élargit. Si on se rentre dedans ou que l’on dépasse les limites de la fenêtre du jeu, la partie se termine.

Il nous est possible de relancer une partie avec un bouton ou de quitter.

Attention au bout d’un score précis un obstacle apparaît pour augmenter la difficulté. Si on touche cet obstacle, il nous fait perdre du score et réapparait à un autre endroit. Si notre score est inférieur à 0, la partie se termine.
