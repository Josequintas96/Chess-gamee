from turtle import color
from Board import *

class Piece:
    name = ""
    color = ""
    active = None
    id = -1 #number to identify the piece on the list
    location = -1 #location of piece
    loc = (-1, -1) #location of piece on pX,pY
    board = None #board reference to board collection
    direction = "" #Down or Up
    poss_loc = []
    pawn_fm = False #this mark if pawn, tthe first movee has yet happen

    def __init__(self,idX, nameX, colorX, boardX, directionX, locX):
        self.id = idX
        self.name = nameX
        self.color = colorX
        self.active = True
        self.board = boardX
        self.direction = directionX
        self.loc = locX
        self.locate_piece(self.loc[1], self.loc[0], self.color)
        print("Piece ID: ", self.id)
        self.board[0].set_id(self.loc[1], self.loc[0], self.id)
        if self.color == "White":
            self.board[0].set_color(self.loc[1], self.loc[0], "W")
        elif self.color == "Black":
            self.board[0].set_color(self.loc[1], self.loc[0], "B")
        
    def set_name(self, nameX):
        self.name = nameX
    
    def set_color(self, colorX):
        self.color = colorX
    
    def set_active(self, activeX):
        #Alive => True
        #Death => False
        self.active = activeX
    
    def set_location(self, locationX):
        self.location = locationX
    
    def set_loc(self, locX):
        self.loc = locX
    
    def set_dirrection(self, directionX):
        self.direction = directionX
    
    
    def ret_name(self):
        return self.name
    
    def ret_color(self):
        return self.color
    
    def ret_active(self):
        return self.active
    
    def ret_location(self):
        return self.location
    
    def ret_loc(self):
        return self.loc
    
    def ret_dirrection(self):
        return self.direction
    
    def print_poss(self):
        print("This is a poss: ", self.poss_loc)
    
    def set_up_poss_mov(self):
        self.poss_movement(self.poss_loc)
    
    
    def poss_movement(self, poss):
        if self.name == "Pawn":
            self.poss_movePawn(poss)
        elif self.name == "Horse":
            self.poss_moveHorse(poss)    
        elif self.name == "Rook":
            self.poss_moveRook(poss) 
        elif self.name == "Bishop":
            self.poss_moveBishop(poss)
        elif self.name == "Queen":
            self.poss_moveQueen(poss)
        elif self.name == "King":
            self.poss_moveKing(poss)




    def movement(self, pX,pY):
        if self.name == "Pawn":
            return self.movePawn (pX,pY)
        elif self.name == "Horse":
            self.movePiece(pX, pY)
        elif self.name == "Rook":
            self.movePiece(pX, pY)
        elif self.name == "Bishop":
            self.movePiece(pX, pY)
        elif self.name == "Queen":
            self.movePiece(pX, pY)
        elif self.name == "King":
            self.movePiece(pX, pY)
        
            
    def poss_movePawn(self, poss):
        print("Location: [", self.loc[0], " , ", self.loc[1], "]")
        poss.clear()
        
        
        if self.direction == "Down":
            if self.loc[0] == 7:
                return None
            # pre_poss = self.loc
            #remeember the X/Y on board/Pieces are twisted compared to the display => therefore you must twist before returnning
            
            if self.pawn_fm == False:
                poss0 = [-1,-1]
                poss0[0] = self.loc[0]+2
                poss0[1] = self.loc[1]
                poss.append(poss0)
                
                poss0 = [-1,-1]
                poss0[0] = self.loc[0]+1
                poss0[1] = self.loc[1]
                poss.append(poss0)
                
            else:
                poss0 = [-1,-1]
                poss0[0] = self.loc[0]+1
                poss0[1] = self.loc[1]
                poss.append(poss0)
                
                
            if self.loc[0] >=0 and self.loc[0] <7:
                if self.loc[1] >=0 and self.loc[1]<7:
                    if self.color == "White":
                        print("\tMoving a white piece")
                        if self.board[0].ret_color(self.loc[1]+1, self.loc[0]+1) == "B":
                            print("Black kill must be possibility")
                            poss0 = [-1,-1]
                            poss0[0] = self.loc[0]+1
                            poss0[1] = self.loc[1]+1
                            poss.append(poss0)
                    elif self.color == "Black":
                        print("Moving a Black piece")
                        if self.board[0].ret_color(self.loc[1]+1, self.loc[0]+1) == "W":
                            print("White kill must be possibility")
                            poss0 = [-1,-1]
                            poss0[0] = self.loc[0]+1
                            poss0[1] = self.loc[1]+1
                            poss.append(poss0)
                if self.loc[1] >0 and self.loc[1]<=7:
                    if self.color == "White":
                        print("Moving a white piece")
                        if self.board[0].ret_color(self.loc[1]+1, self.loc[0]-1) == "B":
                            print("\tBlack kill must be possibility")
                            poss0 = [-1,-1]
                            poss0[0] = self.loc[0]+1
                            poss0[1] = self.loc[1]-1
                            poss.append(poss0)
                    elif self.color == "Black":
                        print("Moving a Black piece")
                        if self.board[0].ret_color(self.loc[1]+1, self.loc[0]-1) == "W":
                            print("White kill must be possibility")
                            poss0 = [-1,-1]
                            poss0[0] = self.loc[0]+1
                            poss0[1] = self.loc[1]-1
                            poss.append(poss0)
        if self.direction == "Up":
            if self.loc[0] == 0:
                return None
            
            if self.pawn_fm == False:
                poss0 = [-1,-1]
                poss0[0] = self.loc[0]-2
                poss0[1] = self.loc[1]
                poss.append(poss0)
                
                poss0 = [-1,-1]
                poss0[0] = self.loc[0]-1
                poss0[1] = self.loc[1]
                poss.append(poss0)
                
            else:
                poss0 = [-1,-1]
                poss0[0] = self.loc[0]-1
                poss0[1] = self.loc[1]
                poss.append(poss0)
                
            if self.loc[0] <=7 and self.loc[0] >0:
                if self.loc[1] >=0 and self.loc[1]<7:
                    if self.color == "White":
                        print("Moving a white piece")
                        if self.board[0].ret_color(self.loc[1]+1, self.loc[0]-1) == "B":
                            print("\tBlack kill must be possibility")
                            poss0 = [-1,-1]
                            poss0[0] = self.loc[0]-1
                            poss0[1] = self.loc[1]+1
                            poss.append(poss0)
                    elif self.color == "Black":
                        print("Moving a Black piece")
                        if self.board[0].ret_color(self.loc[1]+1, self.loc[0]-1) == "W":
                            print("White kill must be possibility")
                            poss0 = [-1,-1]
                            poss0[0] = self.loc[0]-1
                            poss0[1] = self.loc[1]+1
                            poss.append(poss0)
                if self.loc[1] >0 and self.loc[1]<=7:
                    if self.color == "White":
                        print("Moving a white piece")
                        if self.board[0].ret_color(self.loc[1]-1, self.loc[0]-1) == "B":
                            print("\tBlack kill must be possibility")
                            poss0 = [-1,-1]
                            poss0[0] = self.loc[0]-1
                            poss0[1] = self.loc[1]-1
                            poss.append(poss0)
                    elif self.color == "Black":
                        print("Moving a Black piece")
                        if self.board[0].ret_color(self.loc[1]-1, self.loc[0]-1) == "W":
                            print("White kill must be possibility")
                            poss0 = [-1,-1]
                            poss0[0] = self.loc[0]-1
                            poss0[1] = self.loc[1]-1
                            poss.append(poss0)
            
            
            # print("\tLocationC: ", self.loc)
            # print("\tPossibleC: ",possX)
        print("Possibles: ", poss)
        print("<><><><><><><><><><><>")
        
        # return "move"
        

    def poss_moveHorse(self, poss):
        print("\tStage 2 Move Horse")
        poss.clear()
        print("\t\tLocation: [", self.loc[0], " , ", self.loc[1], "]")
        #set up the compass
        #North:
        i0 = self.loc[0]-2
        if i0 >=0:
            i1 = self.loc[1]
            if i1+1 <=7:
                poss0=[-1,-1]
                poss0[0] = i0
                poss0[1] = i1+1
                strX = self.board[0].ret_color(poss0[1], poss0[0])
                if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                    print("\t\t\t Reach Opp piece")
                    poss.append(poss0)
                elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                    print("\t\t\t Reach Same piece")
                else:
                    print("\t\t\t Move piece")
                    poss.append(poss0) 
            if i1-1>=0:
                poss0=[-1,-1]
                poss0[0] = i0
                poss0[1] = i1-1
                strX = self.board[0].ret_color(poss0[1], poss0[0])
                if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                    print("\t\t\t Reach Opp piece")
                    poss.append(poss0)
                elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                    print("\t\t\t Reach Same piece")
                else:
                    print("\t\t\t Move piece")
                    poss.append(poss0)
        #South
        i0 = self.loc[0]+2
        if i0 <8:
            i1 = self.loc[1]
            if i1+1 <=7:
                poss0=[-1,-1]
                poss0[0] = i0
                poss0[1] = i1+1
                strX = self.board[0].ret_color(poss0[1], poss0[0])
                if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                    print("\t\t\t Reach Opp piece")
                    poss.append(poss0)
                elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                    print("\t\t\t Reach Same piece")
                else:
                    print("\t\t\t Move piece")
                    poss.append(poss0) 
            if i1-1>=0:
                poss0=[-1,-1]
                poss0[0] = i0
                poss0[1] = i1-1
                strX = self.board[0].ret_color(poss0[1], poss0[0])
                if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                    print("\t\t\t Reach Opp piece")
                    poss.append(poss0)
                elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                    print("\t\t\t Reach Same piece")
                else:
                    print("\t\t\t Move piece")
                    poss.append(poss0)
        
        #East
        i1 = self.loc[1]+2
        if i1 <8:
            i0 = self.loc[0]
            if i0+1 <=7:
                poss0=[-1,-1]
                poss0[0] = i0+1
                poss0[1] = i1
                strX = self.board[0].ret_color(poss0[1], poss0[0])
                if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                    print("\t\t\t Reach Opp piece")
                    poss.append(poss0)
                elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                    print("\t\t\t Reach Same piece")
                else:
                    print("\t\t\t Move piece")
                    poss.append(poss0) 
            if i0-1>=0:
                poss0=[-1,-1]
                poss0[0] = i0-1
                poss0[1] = i1
                strX = self.board[0].ret_color(poss0[1], poss0[0])
                if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                    print("\t\t\t Reach Opp piece")
                    poss.append(poss0)
                elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                    print("\t\t\t Reach Same piece")
                else:
                    print("\t\t\t Move piece")
                    poss.append(poss0)
                    
        #Weast
        i1 = self.loc[1]-2
        if i1 >=0:
            i0 = self.loc[0]
            if i0+1 <=7:
                poss0=[-1,-1]
                poss0[0] = i0+1
                poss0[1] = i1
                strX = self.board[0].ret_color(poss0[1], poss0[0])
                if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                    print("\t\t\t Reach Opp piece")
                    poss.append(poss0)
                elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                    print("\t\t\t Reach Same piece")
                else:
                    print("\t\t\t Move piece")
                    poss.append(poss0) 
            if i0-1>=0:
                poss0=[-1,-1]
                poss0[0] = i0-1
                poss0[1] = i1
                strX = self.board[0].ret_color(poss0[1], poss0[0])
                if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                    print("\t\t\t Reach Opp piece")
                    poss.append(poss0)
                elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                    print("\t\t\t Reach Same piece")
                else:
                    print("\t\t\t Move piece")
                    poss.append(poss0)
        print("\t\ttPossibles: ", poss)
        print("<><><><><><><><><><><>")
        
            
    def poss_moveBishop(self, poss):
        print("\tStage 2 Move Bishop")
        poss.clear()
        print("\t\tLocation: [", self.loc[0], " , ", self.loc[1], "]")
        #Angle: 45
        i0 = self.loc[0]
        i1 = self.loc[1]
        while i0>0 and i1 >0:
            poss0=[-1,-1]
            poss0[0] = i0-1
            poss0[1] = i1-1
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0 = -1
                i1 = -1
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0 = -1
                i1 = -1
            else:
                print("\t\t\t Move piece")
                poss.append(poss0)
                i0 -= 1
                i1 -= 1
            
            
        
        
        #Angle 135
        i0 = self.loc[0]
        i1 = self.loc[1]
        while i0>0 and i1 <7:
            poss0=[-1,-1]
            poss0[0] = i0-1
            poss0[1] = i1+1
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0 = -1
                i1 = 7
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0 = -1
                i1 = 7
            else:
                print("\t\t\t Move piece")
                poss.append(poss0)
                i0 -= 1
                i1 += 1        
        
        
        #Angle 225
        i0 = self.loc[0]
        i1 = self.loc[1]
        while i0<7 and i1 <7:
            poss0=[-1,-1]
            poss0[0] = i0+1
            poss0[1] = i1+1
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0 = 7
                i1 = 7
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0 = 7
                i1 = 7
            else:
                print("\t\t\t Move piece")
                poss.append(poss0)
                i0 += 1
                i1 += 1   
        
        #Angle 315
        i0 = self.loc[0]
        i1 = self.loc[1]
        while i0<7 and i1 >0:
            poss0=[-1,-1]
            poss0[0] = i0+1
            poss0[1] = i1-1
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0 = 7
                i1 = 7
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0 = 7
                i1 = 7
            else:
                print("\t\t\t Move piece")
                poss.append(poss0)
                i0 += 1
                i1 -= 1
        
        print("\t\ttPossibles: ", poss)
        print("<><><><><><><><><><><>")
        
        
        
    def poss_moveRook(self, poss):
        print("\tStagee 2 Move Rook")
        poss.clear()
        print("\t\tLocation: [", self.loc[0], " , ", self.loc[1], "]")
        
        #set up the compass
        #North:
        i0 = self.loc[0]
        i_m = 1
        while i0 >0:
            poss0=[-1,-1]
            poss0[0] = self.loc[0]-i_m
            poss0[1] = self.loc[1]
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0=-1
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0=-1
            else:
                poss.append(poss0)
                i0-=1
                i_m +=1
        #South
        i0 = self.loc[0]
        i_m = 1
        while i0 < 7:
            poss0=[-1,-1]
            poss0[0] = self.loc[0]+i_m
            poss0[1] = self.loc[1]
            print("For possition: ", poss0)
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0=8
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece ", self.id, " and ", i0)
                i0 = 8
            else:
                poss.append(poss0)
                i0+=1
                i_m +=1
        #East
        i0 = self.loc[1]
        i_m = 1
        while i0 <7:
            poss0=[-1,-1]
            poss0[0] = self.loc[0]
            poss0[1] = self.loc[1]+i_m
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0=8
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0=8
            else:
                poss.append(poss0)
                i0+=1
                i_m +=1

        #West
        i0 = self.loc[1]
        i_m = 1
        while i0 >0:
            poss0=[-1,-1]
            poss0[0] = self.loc[0]
            poss0[1] = self.loc[1]-i_m
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0=0
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0= -1
            else:
                poss.append(poss0)
                i0-=1
                i_m +=1
        
        
        print("\t\ttPossibles: ", poss)
        print("<><><><><><><><><><><>")
        
        
    def poss_moveQueen(self, poss):
        print("\tStage 2 Move Queen")
        poss.clear()
        print("\t\tLocation: [", self.loc[0], " , ", self.loc[1], "]")
        
        #set up the compass
        #North:
        i0 = self.loc[0]
        i_m = 1
        while i0 >0:
            poss0=[-1,-1]
            poss0[0] = self.loc[0]-i_m
            poss0[1] = self.loc[1]
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0=-1
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0=-1
            else:
                poss.append(poss0)
                i0-=1
                i_m +=1
        #South
        i0 = self.loc[0]
        i_m = 1
        while i0 < 7:
            poss0=[-1,-1]
            poss0[0] = self.loc[0]+i_m
            poss0[1] = self.loc[1]
            print("For possition: ", poss0)
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0=8
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece ", self.id, " and ", i0)
                i0 = 8
            else:
                poss.append(poss0)
                i0+=1
                i_m +=1
        #East
        i0 = self.loc[1]
        i_m = 1
        while i0 <7:
            poss0=[-1,-1]
            poss0[0] = self.loc[0]
            poss0[1] = self.loc[1]+i_m
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0=8
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0=8
            else:
                poss.append(poss0)
                i0+=1
                i_m +=1

        #West
        i0 = self.loc[1]
        i_m = 1
        while i0 >0:
            poss0=[-1,-1]
            poss0[0] = self.loc[0]
            poss0[1] = self.loc[1]-i_m
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0=0
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0=-1
            else:
                poss.append(poss0)
                i0-=1
                i_m +=1
                
        
        #Angle: 45
        i0 = self.loc[0]
        i1 = self.loc[1]
        while i0>0 and i1 >0:
            poss0=[-1,-1]
            poss0[0] = i0-1
            poss0[1] = i1-1
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0 = -1
                i1 = -1
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0 = -1
                i1 = -1
            else:
                print("\t\t\t Move piece")
                poss.append(poss0)
                i0 -= 1
                i1 -= 1
            
            
        
        
        #Angle 135
        i0 = self.loc[0]
        i1 = self.loc[1]
        while i0>0 and i1 <7:
            poss0=[-1,-1]
            poss0[0] = i0-1
            poss0[1] = i1+1
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0 = -1
                i1 = 7
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0 = -1
                i1 = 7
            else:
                print("\t\t\t Move piece")
                poss.append(poss0)
                i0 -= 1
                i1 += 1        
        
        
        #Angle 225
        i0 = self.loc[0]
        i1 = self.loc[1]
        while i0<7 and i1 <7:
            poss0=[-1,-1]
            poss0[0] = i0+1
            poss0[1] = i1+1
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0 = 7
                i1 = 7
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0 = 7
                i1 = 7
            else:
                print("\t\t\t Move piece")
                poss.append(poss0)
                i0 += 1
                i1 += 1   
        
        #Angle 315
        i0 = self.loc[0]
        i1 = self.loc[1]
        while i0<7 and i1 >0:
            poss0=[-1,-1]
            poss0[0] = i0+1
            poss0[1] = i1-1
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
                i0 = 7
                i1 = 7
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
                i0 = 7
                i1 = 7
            else:
                print("\t\t\t Move piece")
                poss.append(poss0)
                i0 += 1
                i1 -= 1
                
        print("\t\ttPossibles: ", poss)
        print("<><><><><><><><><><><>")

    
    def poss_moveKing(self, poss):
        print("\tStage 2 Move Queen")
        poss.clear()
        print("\t\tLocation: [", self.loc[0], " , ", self.loc[1], "]")
        
        #Up
        i0 = self.loc[0]
        if i0 >0:
            i1 = self.loc[1]
            if i1 >0:
                poss0=[-1,-1]
                poss0[0] = i0-1
                poss0[1] = i1-1
                strX = self.board[0].ret_color(poss0[1], poss0[0])
                if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                    print("\t\t\t Reach Opp piece")
                    poss.append(poss0)
                elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                    print("\t\t\t Reach Same piece")
                else:
                    print("\t\t\t Move piece")
                    poss.append(poss0)
            if i1<7:
                poss0=[-1,-1]
                poss0[0] = i0-1
                poss0[1] = i1+1
                strX = self.board[0].ret_color(poss0[1], poss0[0])
                if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                    print("\t\t\t Reach Opp piece")
                    poss.append(poss0)
                elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                    print("\t\t\t Reach Same piece")
                else:
                    print("\t\t\t Move piece")
                    poss.append(poss0)
                    
            poss0=[-1,-1]
            poss0[0] = i0-1
            poss0[1] = i1
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
            else:
                print("\t\t\t Move piece")
                poss.append(poss0)
                
        
        #Down
        i0 = self.loc[0]
        if i0 <7 :
            i1 = self.loc[1]
            if i1 >0:
                poss0=[-1,-1]
                poss0[0] = i0+1
                poss0[1] = i1-1
                strX = self.board[0].ret_color(poss0[1], poss0[0])
                if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                    print("\t\t\t Reach Opp piece")
                    poss.append(poss0)
                elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                    print("\t\t\t Reach Same piece")
                else:
                    print("\t\t\t Move piece")
                    poss.append(poss0)
            if i1<7:
                poss0=[-1,-1]
                poss0[0] = i0+1
                poss0[1] = i1+1
                strX = self.board[0].ret_color(poss0[1], poss0[0])
                if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                    print("\t\t\t Reach Opp piece")
                    poss.append(poss0)
                elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                    print("\t\t\t Reach Same piece")
                else:
                    print("\t\t\t Move piece")
                    poss.append(poss0)
                    
            poss0=[-1,-1]
            poss0[0] = i0+1
            poss0[1] = i1
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
            else:
                print("\t\t\t Move piece")
                poss.append(poss0)
               
 
        #Side L
        i1 = self.loc[1]
        if i1 >0:
            poss0=[-1,-1]
            poss0[0] = i0
            poss0[1] = i1-1
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
            else:
                print("\t\t\t Move piece")
                poss.append(poss0)
                
                
        #Side R
        i1 = self.loc[1]
        if i1 <7:
            poss0=[-1,-1]
            poss0[0] = i0
            poss0[1] = i1+1
            strX = self.board[0].ret_color(poss0[1], poss0[0])
            if (strX == "W" and self.color == "Black") or (strX == "B" and self.color == "White") :
                print("\t\t\t Reach Opp piece")
                poss.append(poss0)
            elif (strX == "W" and self.color == "White") or (strX == "B" and self.color == "Black"):
                print("\t\t\t Reach Same piece")
            else:
                print("\t\t\t Move piece")
                poss.append(poss0)
                
                
         
        print("\t\ttPossibles: ", poss)
        print("<><><><><><><><><><><>")

            

    def movePawn(self, pX, pY ):
        self.board[0].set_id(self.loc[1], self.loc[0], -1)
        self.board[0].set_color(self.loc[1], self.loc[0], "n")
        print("HERE IS A PAWN => ", pX, " $ ", pY)
        self.loc = (pX, pY)
        self.board[0].set_id(self.loc[1], self.loc[0], self.id)
        if self.color == "White":
            self.board[0].set_color(self.loc[1], self.loc[0], "W")
        else:
            self.board[0].set_color(self.loc[1], self.loc[0], "B")
        
        if self.direction == "Up" and self.loc[0] == 0:
            print("\t\tRANK UP")
            return "Rank Up"
        elif self.direction == "Down" and self.loc[0] == 7:
            print("\t\tRANK UP")
            return "Rank Up"
        if self.pawn_fm == False:
            self.pawn_fm = True
        
        return "Move"
        
    def movePiece(self, pX, pY):
        #clean the color and the location on board
        self.board[0].set_id(self.loc[1], self.loc[0], -1)
        self.board[0].set_color(self.loc[1], self.loc[0], "n")
        print("\tHERE IS A " , self.name, " => ", pX, " & ", pY)
        self.loc = (pX, pY)
        self.board[0].set_id(self.loc[1], self.loc[0], self.id)
        if self.color == "White":
            self.board[0].set_color(self.loc[1], self.loc[0], "W")
        else:
            self.board[0].set_color(self.loc[1], self.loc[0], "B")
            
        print("NEW PIECE LOCATION: ", self.loc)
        return "Move"
        
    def callPiece(self):
        print("Name: ", self.name)
        print("Color: ", self.color)
        print("Location: ", self.color)
        print("<><><><><><><><><><><><><><><><><>")
    
    def locate_piece(self,pY,pX, nameX):
        # Change location on board and save the X/Y location on Piece
        # Remember X and Y inverse on pieces
        # self.location = self.board[0].set_locate(pX,pY, nameX)
        # save thee location of pieece
        self.loc = (pX,pY)
    
    def print_piece(self):
        print("Name: ", self.name)
        print("Color: ", self.color)
        print("ID: ", self.id)
        print("Loc:  ", self.loc)
    
    
    
    
        