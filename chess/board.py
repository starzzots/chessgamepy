from constants import *
from square import Square
from piece import *
import numpy as np


class Board():
    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        if color == 'white':
            row_pawn, row_other = (6, 7)
        else:
            row_pawn, row_other = (1, 0)

        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

            if self.squares[row_other][col] == self.squares[row_other][0] or self.squares[row_other][col] == self.squares[row_other][-1]:
                self.squares[row_other][col] = Square(
                    row_other, col, Rook(color))

            if self.squares[row_other][col] == self.squares[row_other][1] or self.squares[row_other][col] == self.squares[row_other][-2]:
                self.squares[row_other][col] = Square(
                    row_other, col, Knight(color))

            if self.squares[row_other][col] == self.squares[row_other][2] or self.squares[row_other][col] == self.squares[row_other][-3]:
                self.squares[row_other][col] = Square(
                    row_other, col, Bishop(color))

            if self.squares[row_other][col] == self.squares[row_other][3]:
                self.squares[row_other][col] = Square(
                    row_other, col, Queen(color))

            if self.squares[row_other][col] == self.squares[row_other][4]:
                self.squares[row_other][col] = Square(
                    row_other, col, King(color))
