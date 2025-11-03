import os
import time
import random

def clear_screen_windows():
    os.system("cls")

def clear_screen_unix():
    os.system("clear")

def random_boolean():
    return bool(random.getrandbits(1))


# Fonction qui va afficher la grille du Jeu de la Vie
# Marche tant que les attributs `width`, `height` et `grid` sont corrects
def to_string(game_of_life):
    s = "┌" + ("─" * (game_of_life.width * 2)) + "┐\n"
    for y in range(game_of_life.height):
        s += "│"
        for x in range(game_of_life.width):
            if game_of_life.grid[y][x]:
                s += "▓▓"
            else:
                s += "  "
        s += "│\n"
    s += "└" + ("─" * (game_of_life.width * 2)) + "┘\n"
    return s

class GameOfLife:
    def __init__(self, width=50, height=50, prob_alive=0.1):
        self.height = height
        self.width = width

        # Liste dont chaque élément est une cellule de la grille
        self.grid = []

        for i in range(self.height):
            line = []
            for j in range(self.width):
                line.append(random_boolean())
            self.grid.append(line)

game = GameOfLife(50, 50, 0.1)
print(to_string(game))