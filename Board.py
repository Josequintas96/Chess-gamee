


from re import I


class Board():
    coordinates =[]
    board_set = {}
    piece_set ={}
    id_set =[]
    
    def __init__(self):
        self.coordinates = []
        self.set_cordinates()
        i0 = 0
        while i0 < 8:
            i1 = 0
            pp = []
            while i1 < 8:
                pp.append(-1)
                i1+=1
            self.id_set.append(pp)
            i0+=1
        
    def print_cordinate(self):
        #print the coorrdinates number of thee board
        i0 = 0
        while i0 <8:
            i1 = 0
            while i1 <8:
                print(self.board_set[(i1,i0)], "\t", end="")
                i1+=1
            print()
            i0+=1
            
    def print_id(self):
        #print the coorrdinates number of thee board
        i0 = 0
        while i0 <8:
            i1 = 0
            while i1 <8:
                if self.id_set[i1][i0] == -1:
                    print( "_\t", end="")
                else:
                    print(self.id_set[i1][i0], "\t", end="")
                i1+=1
            print()
            i0+=1
            
    def print_piece_set(self):
        #print the coorrdinates number of thee board
        i0 = 0
        while i0 <8:
            i1 = 0
            while i1 <8:
                print(self.piece_set[(i1,i0)], "\t", end="")
                i1+=1
            print()
            i0+=1
        
    def set_cordinates(self):
        roundX = 0
        i0=0
        while i0<8:
            i1=0
            while i1<8:
                self.board_set[(i1,i0)] = i0+i1+ roundX
                self.piece_set[(i1,i0)] = -1 #-1 mean the piece is empty
                i1+=1
            i0+=1
            roundX+=7
            
    def set_locate(self, pX, pY, nameX):
        if nameX =="White":
            print("This happeen")
            self.piece_set[(pY,pX)] = 1 
        elif nameX== "Black":
            self.piece_set[(pY,pX)] = 2
        return self.board_set[(pY,pX)]
    
    def set_id(self, i1,i0,id):
        self.id_set[i1][i0] = id
        
    def ret_id(self, i1,i0):
        return self.id_set[i1][i0]
            
    def ret_board_set(self, pX, pY):
        print("\tThis board => ", self.board_set[(pX, pY)] )
        if self.piece_set[(pY, pX)] == -1:
            print("\t\t No piece " )



