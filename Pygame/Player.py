from turtle import color
from Board import *
from Piece import *

class Player:
    name = ""
    number = 0
    color = ""
    Pieces = []

    def __init__(self, nameX, colorX,  pieceX, boardX):
        self.name = nameX
        self.color = colorX
        self.piece = pieceX
        self.board = boardX
        PieceX = Piece( 0, "Pawn", "White",  self.board, "Down", (0,0))
        PieceX2 = Piece(1, "Pawn", "Black",  self.board, "Up", (1,2))
        self.piece.append(PieceX)
        self.piece.append(PieceX2)
        
        PieceX3 = Piece(2, "Rook", "Black",  self.board, "Up", (7,7))
        PieceX4 = Piece(3, "Rook", "White",  self.board, "Up", (0,1))
        self.piece.append(PieceX3)
        self.piece.append(PieceX4)
        
        PieceX5 = Piece(4, "Horse", "Black",  self.board, "Up", (3,3))
        self.piece.append(PieceX5)
        
        PieceX6 = Piece(5, "Bishop", "Black",  self.board, "Up", (7,4))
        self.piece.append(PieceX6)
        
        PieceX7 = Piece(6, "Queen", "Black",  self.board, "Up", (7,5))
        self.piece.append(PieceX7)
        
        PieceX8 = Piece(7, "King", "Black",  self.board, "Up", (4,4))
        self.piece.append(PieceX8)
            
            

