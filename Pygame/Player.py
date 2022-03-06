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
        # PieceX = Piece( 0, "Pawn", "White",  self.board, "Down", (0,0))
        # PieceX2 = Piece(1, "Pawn", "Black",  self.board, "Up", (1,2))
        # self.piece.append(PieceX)
        # self.piece.append(PieceX2)
        
    def set_up_Player(self, id_count, direction):
        if direction == "Up":
            i0 = 0
            PieceX = Piece( i0, "Rook", self.color,  self.board, direction, (7,0))
            self.piece.append(PieceX)
            i0+=1
            PieceX2 = Piece( i0, "Horse", self.color,  self.board, direction, (7,1))
            self.piece.append(PieceX2)
            i0+=1
            PieceX3 = Piece( i0, "Bishop", self.color,  self.board, direction, (7,2))
            self.piece.append(PieceX3)
            i0+=1
            PieceX4 = Piece( i0, "King", self.color,  self.board, direction, (7,3))
            self.piece.append(PieceX4)
            i0+=1
            PieceX5 = Piece( i0, "Queen", self.color,  self.board, direction, (7,4))
            self.piece.append(PieceX5)
            i0+=1
            PieceX6 = Piece( i0, "Bishop", self.color,  self.board, direction, (7,5))
            self.piece.append(PieceX6)
            i0+=1
            PieceX7 = Piece( i0, "Horse", self.color,  self.board, direction, (7,6))
            self.piece.append(PieceX7)
            i0+=1
            PieceX8 = Piece( i0, "Rook", self.color,  self.board, direction, (7,7))
            self.piece.append(PieceX8)
            i0 = 8
            while i0 >7 and i0 < 16:
                PieceX = Piece( i0+id_count, "Pawn", self.color,  self.board, direction, (6,i0-8))
                self.piece.append(PieceX)
                i0+=1


        if direction == "Down":
            i0 = 0
            PieceX = Piece( i0+id_count, "Rook", self.color,  self.board, direction, (0,0))
            self.piece.append(PieceX)
            i0+=1
            PieceX2 = Piece( i0+id_count, "Horse", self.color,  self.board, direction, (0,1))
            self.piece.append(PieceX2)
            i0+=1
            PieceX3 = Piece( i0+id_count, "Bishop", self.color,  self.board, direction, (0,2))
            self.piece.append(PieceX3)
            i0+=1
            PieceX4 = Piece( i0+id_count, "King", self.color,  self.board, direction, (0,3))
            self.piece.append(PieceX4)
            i0+=1
            PieceX5 = Piece( i0+id_count, "Queen", self.color,  self.board, direction, (0,4))
            self.piece.append(PieceX5)
            i0+=1
            PieceX6 = Piece( i0+id_count, "Bishop", self.color,  self.board, direction, (0,5))
            self.piece.append(PieceX6)
            i0+=1
            PieceX7 = Piece( i0+id_count, "Horse", self.color,  self.board, direction, (0,6))
            self.piece.append(PieceX7)
            i0+=1
            PieceX8 = Piece( i0+id_count, "Rook", self.color,  self.board, direction, (0,7))
            self.piece.append(PieceX8)
            i0 = 8
            while i0 >7 and i0 < 16:
                PieceX = Piece( i0+id_count, "Pawn", self.color,  self.board, direction, (1,i0-8))
                self.piece.append(PieceX)
                i0+=1
                
        print("Set up game")
        
        # PieceX3 = Piece(2, "Rook", "Black",  self.board, "Up", (7,7))
        # PieceX4 = Piece(3, "Rook", "White",  self.board, "Up", (0,1))
        # self.piece.append(PieceX3)
        # self.piece.append(PieceX4)
        
        # PieceX5 = Piece(4, "Horse", "Black",  self.board, "Up", (3,3))
        # self.piece.append(PieceX5)
        
        # PieceX6 = Piece(5, "Bishop", "Black",  self.board, "Up", (7,4))
        # self.piece.append(PieceX6)
        
        # PieceX7 = Piece(6, "Queen", "Black",  self.board, "Up", (7,5))
        # self.piece.append(PieceX7)
        
        # PieceX8 = Piece(7, "King", "Black",  self.board, "Up", (4,4))
        # self.piece.append(PieceX8)
            
            

