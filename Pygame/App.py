from pygame import *


import sys



sys.path.append('../')
from Board import *
from Piece import *
from setting_game.download_control import *
from setting_game.screen_control import *

RED = (255, 0, 0)
GRAY = (150, 150, 150)

# pygame.init()


#title
# pygame.display.set_caption("example")
# iconS = pygame.image.load("Image/black_square.png")
# pygame.display.set_icon(iconS)

#size of the window
# screen = pygame.display.set_mode((500,500)) #height X:800  weight Y: 600
                    #start at left up corner

text = ""

offset_m = [0,0]





class App:
    mouse_piece = False #in casee themousee press thee piece or board,seee possibilities
    mouse_control= []
    mouse_possibles = []
    board_Omega = []
    mouse_id = -1 #this is valuuee to register the id of piece

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        w, h = 900, 800
        pygame.display.set_caption("example")
        iconS = pygame.image.load("Image/chess.png")
        pygame.display.set_icon(iconS)
        
        
        # flags = RESIZABLE
        App.screen = pygame.display.set_mode((w, h))
        
        
        #section to use the board and pieces
        boardX = Board()
        self.board_Omega = []
        self.board_Omega.append(boardX)

        # (208, 155)
        PieceX = Piece( 0, "Pawn", "White",  self.board_Omega, "Down", (0,0))
        PieceX2 = Piece(1, "Pawn", "Black",  self.board_Omega, "Up", (1,2))
        self.piece_Omega = []
        self.piece_Omega.append(PieceX)
        self.piece_Omega.append(PieceX2)
        
        PieceX3 = Piece(2, "Rook", "Black",  self.board_Omega, "Up", (7,7))
        PieceX4 = Piece(3, "Rook", "White",  self.board_Omega, "Up", (0,1))
        self.piece_Omega.append(PieceX3)
        self.piece_Omega.append(PieceX4)
        
        PieceX5 = Piece(4, "Horse", "Black",  self.board_Omega, "Up", (3,3))
        self.piece_Omega.append(PieceX5)
        
        PieceX6 = Piece(5, "Bishop", "Black",  self.board_Omega, "Up", (7,4))
        self.piece_Omega.append(PieceX6)
        
        PieceX7 = Piece(6, "Queen", "Black",  self.board_Omega, "Up", (7,5))
        self.piece_Omega.append(PieceX7)
        
        PieceX8 = Piece(7, "King", "Black",  self.board_Omega, "Up", (4,4))
        self.piece_Omega.append(PieceX8)
        
        
        #mouse section variables
        self.mouse_control.append(-1)
        self.mouse_control.append(-1) 
        


        App.running = True
        
        
    def display_board(self, pX, pY, App, loc):
        i0 = 0
        disctance_b = 90
        colorB = True # Tue man whitee while Flase mean Black
        touch_sq = False
        touch_color = None
        touch_loc = (0,0)
        
        while i0 <8:
            i1 = 0
            while i1 < 8:
                pX2 = pX+90*i0
                pY2 = pY+90*i1
                if loc[0] > pX2 and loc[0] < pX2+90 and loc[1] > pY2 and loc[1] < pY2+90:
                    touch_loc =(pX2, pY2)
                    touch_color = colorB
                    touch_sq = True
                    if colorB==True:
                        colorB = False
                    else:
                        colorB = True
                    # board_Omega[0].ret_board_set(i0,i1)
                else:
                    if colorB == True:
                        square_blank(pX2, pY2, False, False, App)
                        colorB = False
                    else:
                        square_black(pX2, pY2, False, False, App)
                        colorB = True
                # print(i0, ",", i1 , "\t", end="")
                i1+=1
            # print()
            i0+=1
            if colorB==True:
                colorB = False
            else:
                colorB = True
        if touch_sq == True:
            if touch_color == True:
                square_blank(touch_loc[0], touch_loc[1], True, False, App )
            else:
                square_black( touch_loc[0], touch_loc[1], True, False, App )
        # print("<><><><><><><><><><><><>><><><>><>><><><>")


    def press_on_board(self, coordinate, loc, mouse_control):
        # coordinate: set location of stating board
        i0 = 0
        
        while i0 <8:
            i1 = 0
            while i1 < 8:
                pX2 = coordinate[0]+90*i0
                pY2 = coordinate[1]+90*i1
                if loc[0] > pX2 and loc[0] < pX2+90 and loc[1] > pY2 and loc[1] < pY2+90:
                    mouse_control[0] = i1
                    mouse_control[1] = i0
                    return True
                i1+=1
            i0+=1
        return False


    def display_board_Possibilities(self, pX,pY, App, possibles):
        i0 = 0
        colorB = True # Tue man whitee while Flase mean Black
        poss = len(possibles) #group of locatoiojn to outshine
        #sequence values regarding correspoding colors
        # print("Len of poss: ", poss, " & POSS: ", possibles)
        i_p = 0
        
        while i0 <8:
            i1 = 0
            while i1 < 8:
                pX2 = pX+90*i0
                pY2 = pY+90*i1
                #remember the coordinatee/location of pieeces are the twisted X/Y or i0/i1
                # if i_p < poss and possibles[i_p][0] == i0 and possibles[i_p][1] == i1:
                #     # print("\tThis happen")
                #     i_p+=1
                #     if colorB == True:
                #         colorB = False
                #     else:
                #         colorB = True
                    
                # else:
                    
                if colorB == True:
                    square_blank(pX2, pY2, False, False, App)
                    colorB = False
                else:
                    square_black(pX2, pY2, False, False, App)
                    colorB = True
                i1+=1
            i0+=1
            if colorB==True:
                colorB = False
            else:
                colorB = True
                
        i_p =0
        while i_p < poss:
            # print("Possibilities => ", possibles[i_p])
            pX2 = pX+90*possibles[i_p][1]
            pY2 = pY+90*possibles[i_p][0]
            color_S = None
            # print("\tCoordinates => ", pX2, " & ", pY2)
            if (possibles[i_p][0]%2 ==0 and possibles[i_p][1]%2 == 1) or (possibles[i_p][1]%2 ==0 and possibles[i_p][0]%2 == 1) :
                # print("\t False")
                color_S =   False
            else:
                color_S = True
            if color_S == True:
                square_blank(pX2, pY2, True , True, App)
            else:
                square_black( pX2, pY2, True , True, App )
            i_p+=1
            



    def display_piece(self, loc, App):
        i0 = 0
        sp_loc=[0,0]
        lenX = len(self.piece_Omega)
        while i0 < lenX:
            loc = self.piece_Omega[i0].ret_loc()
            sp_loc[0] = 118+90*loc[1]
            sp_loc[1] = 65+90*loc[0]
            # print(i0 , " and length ", lenX)
            # print("\tPrint coordinate ", sp_loc )
            # print("\tColor 2: ", self.piece_Omega[i0].ret_color() )
            # print("\tNamee 2: ", self.piece_Omega[i0].ret_name() )
            if self.piece_Omega[i0].ret_active():
                if self.piece_Omega[i0].ret_name() == "Pawn":
                    pawn_P(sp_loc[0], sp_loc[1], self.piece_Omega[i0].ret_color(), App)
                elif self.piece_Omega[i0].ret_name() == "Rook":
                    rook_P(sp_loc[0], sp_loc[1], self.piece_Omega[i0].ret_color(), App)
                elif self.piece_Omega[i0].ret_name() == "Horse":
                    horse_P(sp_loc[0], sp_loc[1], self.piece_Omega[i0].ret_color(), App)
                elif self.piece_Omega[i0].ret_name() == "Bishop":
                    bishop_P(sp_loc[0], sp_loc[1], self.piece_Omega[i0].ret_color(), App)
                elif self.piece_Omega[i0].ret_name() == "Queen":
                    queen_P(sp_loc[0], sp_loc[1], self.piece_Omega[i0].ret_color(), App)
                elif self.piece_Omega[i0].ret_name() == "King":
                    king_P(sp_loc[0], sp_loc[1], self.piece_Omega[i0].ret_color(), App)
                    
            i0+=1
        # print("<><><><><><><>")
            
    def print_location_board(self, loc):
        print("Location Board: ")
        print("\t X: ", loc[0])
        print("\t Y: ", loc[1])
        
    def print_location_possibilities(self, loc):
        i0=0
        lenX = len(loc)
        while i0< lenX:
            print("\tPossibilities Locatiion: ")
            print("\t\t X: ", loc[i0][0])
            print("\t\t Y: ", loc[i0][1])   
            i0+=1


    def run(self):
        while App.running:
            mx, my = pygame.mouse.get_pos()
            rot = 0
            loc = [mx , my]
            
            for event in pygame.event.get():
                # if event.type == QUIT:
                if event.type == pygame.QUIT:
                    App.running = False
                    # running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        print("location is ", loc)
                        if self.mouse_piece == False:
                            if self.press_on_board( (100, 50) , loc , self.mouse_control):
                                self.mouse_piece = True
                                # self.mouse_possibles.clear()
                                # self.mouse_possibles.append((self.mouse_control[0], self.mouse_control[1]))
                                self.mouse_id = self.board_Omega[0].ret_id(self.mouse_control[1], self.mouse_control[0])
                                
                                #veerify that id is on limit indicates
                                if self.mouse_id < len(self.piece_Omega):
                                    print("Print board, active mouse; ID=> ", self.mouse_id)
                                    
                                    if self.mouse_id >=0:
                                        print("This is the id: ",self.mouse_id)
                                        self.piece_Omega[self.mouse_id].poss_movement(self.mouse_possibles)
                                else:
                                    print("The ID si not respected  to the set pieces")
                            else:
                                print("MISS BOARDD")
                                self.mouse_possibles.clear()
                                self.mouse_id = -1
                        else:
                            if self.press_on_board( (100, 50) , loc , self.mouse_control):
                                print("Press possibility")
                                print("\t Mouse Control ", self.mouse_control)
                                print("\t Mouse Possibility ", self.mouse_possibles)
                                #confirm if kill piece
                                
                                if self.mouse_control in self.mouse_possibles and self.mouse_id != -1:
                                    print("\tPossibility on This  id: ",self.mouse_id)
                                    
                                    #section to kill a piece
                                    if self.board_Omega[0].ret_id(self.mouse_control[1], self.mouse_control[0]) != -1:
                                        kill_id = self.board_Omega[0].ret_id(self.mouse_control[1], self.mouse_control[0])
                                        print("A kill should happen on ID => ", kill_id)
                                        self.piece_Omega[kill_id].set_active(False)
                                        #kill color on location
                                        self.board_Omega[0].set_color(self.mouse_control[1], self.mouse_control[0], "n" )
                                        
                                        
                                    
                                    moveX = self.piece_Omega[self.mouse_id].movement(self.mouse_control[0], self.mouse_control[1])
                                    print("\t\t M=> ", moveX)
                                    if moveX == 99:
                                        print("RANK UP")
                                self.mouse_piece = False
                                self.mouse_id = -1
                            else:
                                print("MISS BOARDD")
                                self.mouse_possibles.clear()
                                self.mouse_id = -1
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        None
                        # print("Button rise")
                    

                #if keystroke press
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print("Left arrrow press")
                        
                    if event.key == pygame.K_RIGHT:
                        print("Right key is press")

                    if event.key == pygame.K_UP:
                        print("Up key is press")

                    if event.key == pygame.K_DOWN:
                        print("Down key is press")
                        
                    if event.key == pygame.K_SPACE:
                        print("Space key button")
                        
                    if event.key == pygame.K_DELETE:
                        print("Delete key button")

                    if event.key == pygame.K_RETURN:
                        print("Enter buttoon is pressed")
                    
                    if event.key == pygame.K_a:
                        print("Key a has been pressed")
                        self.piece_Omega[0].board[0].print_cordinate()
                        
                
                
                    if event.key == pygame.K_b:
                            print("Key b has been pressed")
                            # self.piece_Omega[0].set_dirrection("Up")
                            # self.piece_Omega[0].locate_piece(7,0, self.piece_Omega[0].ret_color())
                            # self.piece_Omega[0].board[0].print_piece_set()
                
                    if event.key == pygame.K_c:
                        print("Key c has been pressed")
                        self.board_Omega[0].print_id()
                
                    if event.key == pygame.K_d:
                        print("Key d has been pressed")
                        self.board_Omega[0].print_color()
                        
                            
                        
                    if event.key == pygame.K_e:
                        print("Key e has been pressed")
                        
                        
                    if event.key == pygame.K_f:
                        print("Key f has been pressed")
                        print("This is the mouse ID=> ", self.mouse_id)
                        print("<><><><><><><><><><><><><><><><>")
                        
                    if event.key == pygame.K_g:
                        print("Key g has been pressed")
                        ik = 0
                        while ik < len(self.piece_Omega):
                            self.piece_Omega[ik].print_piece()
                            print("<><><><><><><><><><>")
                            ik+=1

                    if event.key == pygame.K_h:
                        print("Key h has been pressed")
                        
                    if event.key == pygame.K_i:
                        print("Key i => Information")
                        
                    if event.key == pygame.K_j:
                        print("Key j has been pressed")
                        
                    if event.key == pygame.K_k:
                        print("Key k has been pressed")
                        
                    if event.key == pygame.K_l:
                        print("Key l has been pressed")
                        self.print_location_board(self.mouse_control) 
                        
                    if event.key == pygame.K_m:
                        print("Key m has been pressed")
                
                    if event.key == pygame.K_n:
                        print("Key n has been pressed")
                        
                    if event.key == pygame.K_o:
                        print("Key o has been pressed")
                        
                    if event.key == pygame.K_p:
                        print("Key p has been pressed")
                        self.print_location_possibilities(self.mouse_possibles)
                        
                    if event.key == pygame.K_q:
                        print("Key q has been pressed")
                        
                    if event.key == pygame.K_r:
                        print("Key r has been pressed")
                        
                    if event.key == pygame.K_s:
                        print("Key s has been pressed")
                        
                    if event.key == pygame.K_t:
                        print("Key t has been pressed")
                        
                    if event.key == pygame.K_u:
                        print("Key u has been pressed")

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        print("Left arrrow release")

                    if event.key == pygame.K_RIGHT:
                        print("Right arrrow release")

                    if event.key == pygame.K_UP:
                        print("Up arrrow release")

                    if event.key == pygame.K_DOWN:
                        print("Down arrow release")
                    if event.key == pygame.K_DELETE:
                        print("Delete key")       

            
            App.screen.fill(GRAY)
            #if bellow screen.fill, then the image will be bellow the color
            #here start the display image

            # self.display_board(100, 50, App, loc)
            
            if self.mouse_piece == False:
                 self.display_board( 100, 50, App, loc)
            else:
                self.display_board_Possibilities(100, 50, App, self.mouse_possibles)
            self.display_piece(loc, App)
            
            # pygame.draw.rect(App.screen, RED, App.rect, 1)
            pygame.display.update()
            
        pygame.quit()
        
        
if __name__ == '__main__':
    App().run()