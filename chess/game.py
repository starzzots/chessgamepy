import pygame
from constants import *


class Game():
    def __init__(self):
        pass

    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = TAN
                else:
                    color = BROWN
                rect = (col * SQUARE_SIZE, row * SQUARE_SIZE,
                        SQUARE_SIZE, SQUARE_SIZE)

                pygame.draw.rect(surface, color, rect)
