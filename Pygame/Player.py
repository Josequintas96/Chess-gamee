from turtle import color
from Board import *
from Piece import *

class Player:
    name = ""
    number = 0 #numbeer of player playing game
    id_control = -1
    color = ""
    Pieces = []
    king_id = -1
    

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
        self.id_control = id_count
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
            PieceX5 = Piece( i0, "Queen", self.color,  self.board, direction, (7,3))
            self.piece.append(PieceX5)
            i0+=1
            PieceX4 = Piece( i0, "King", self.color,  self.board, direction, (7,4))
            self.piece.append(PieceX4)
            self.king_id = i0
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
            self.king_id = i0+id_count
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
        


    def is_on_play(self, id_piece):
        if id_piece >= self.id_control and id_piece <= self.id_control+15:
            return True
        return False


    def check(self):
        # print("King piece loc=> ", self.piece[self.king_id].ret_loc())
        i0 = -1
        if self.king_id < 16:
            i0 =16
        else:
            i0 =0
        locX = self.piece[self.king_id].ret_loc()
        loc = [locX[0], locX[1]]
        i1 = 0
        while i1 < 16:
            # print("\t", i0 , "  Poss is => ", self.piece[i0].poss_loc[i0] )
            # print("loc => ",  loc)
            #reemeber poss_loc is a reference of all possibilities of all pieces
            if loc in self.piece[i0].poss_loc[i0]:
                print("You arre on CHECK by ", i0)
                
                return True
            i0+=1
            i1+=1
        # print("<><><><><><><><><><><><><><><><><>")
        return False
    
    def check2(self):
        # print("King piece loc=> ", self.piece[self.king_id].ret_loc())
        i0 = -1
        if self.king_id < 16:
            i0 =16
        else:
            i0 =0
        locX = self.piece[self.king_id].ret_loc()
        loc = [locX[0], locX[1]]
        i1 = 0
        while i1 < 16:
            # print("\t", i0 , "  Poss is => ", self.piece[i0].poss_loc[i0] )
            # print("loc => ",  loc)
            #reemeber poss_loc is a reference of all possibilities of all pieces
            if loc in self.piece[i0].poss_loc[i0]:
                print("You arre on CHECK by ", i0)
                
                return True
            i0+=1
            i1+=1
        # print("<><><><><><><><><><><><><><><><><>")
        return False
    
    def game_over(self):
        if self.piece[self.king_id].ret_active():
            return False
        return True
    
    def print_king(self):
        print("KING of P", self.number, " => ",  self.king_id)

                    

