import os


class Piece():

    def __init__(self, name, color, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=80):
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')

    def add_moves(self, move):
        self.moves.append(move)


class Pawn(Piece):

    def __init__(self, color):
        if color == 'white':
            self.dir = -1
        else:
            self.dir = 1
        super().__init__('pawn', color)


class Rook(Piece):

    def __init__(self, color):
        super().__init__('rook', color)


class Bishop(Piece):

    def __init__(self, color):
        super().__init__('bishop', color)


class Knight(Piece):

    def __init__(self, color):
        super().__init__('knight', color)


class Queen(Piece):

    def __init__(self, color):
        super().__init__('queen', color)


class King(Piece):

    def __init__(self, color):
        super().__init__('king', color)
