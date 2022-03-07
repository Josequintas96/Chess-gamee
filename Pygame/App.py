from pygame import *


import sys



sys.path.append('../')
from Board import *
from Piece import *
from Player import *
from setting_game.download_control import *
from setting_game.screen_control import *

RED = (255, 0, 0)
GRAY = (150, 150, 150)
BOARD_X = 250 #BOARD S=X AXIS
BOARD_Y = 50 #BOARD Y AXIS
GREEN = (34,139,34)

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
    player_Omega1 = None
    player_Omega2 = None
    rank_occurence = -1 #this is a value in case that RANK UP occur
    rank_string = []
    express = 0
    expressY = 0
    #control the turn of the game
    black_turn = False
    white_turn = True
    #control if there is a CHECK on Player
    check_p1 = False
    check_p2 = False 
    
    #control if winner happen => king has being killed
    win_p1 = False
    win_p2 = False
    
    #savee the localization of mouse press when happen
    mouse_click = [-1,-1]
    

    def __init__(self):
        """Initialize pygame and the application."""
        pygame.init()
        w, h = 1200, 800
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
        self.piece_Omega=[]
        self.player_Omega1 = Player("1", "White", self.piece_Omega, self.board_Omega)
        self.player_Omega2 = Player("2", "Black", self.piece_Omega, self.board_Omega)
        
        self.player_Omega1.set_up_Player(0, "Up")
        self.player_Omega2.set_up_Player(16, "Down")
        
        print("Thiis is  the length ==> ", len(self.piece_Omega))
        
        self.set_up_all_pieces_movements()
        
        
        #mouse section variables
        self.mouse_control.append(-1)
        self.mouse_control.append(-1) 
        


        App.running = True
        
    def display_rank_board(self, pX, pY, App, loc):
        square_board(pX, pY, App, loc)

    def display_Check(self, pX, pY, App):
        check_D(pX, pY, App) 
    
    def display_Win(self, pX, pY, App, winner):
        winner_board(pX, pY, App,  winner)       
        
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


    def press_on_board(self, coordinate, loc, mouse_control, mouse_click):
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
                    mouse_click[0]  = i1
                    mouse_click[1] =  i0
                    return True
                i1+=1
            i0+=1
        return False
    
    def press_on_rank(self, loc, str_rank):
        # (pX2+64*i0+10, pY2)
        print("Rank control")
        pX = BOARD_X + 90+40
        pY = 275+120
        if loc[1] > pY and pY < pY+64:
            if loc[0] > pX and loc[0]< pX+100:
                str_rank.append("Rook")
            elif loc[0] > pX+120 and loc[0]< pX+220:
                str_rank.append("Horse")
            elif loc[0] > pX+240 and loc[0]< pX+340:
                str_rank.append("Bishop")
            elif loc[0] > pX+360 and loc[0]< pX+460:
                str_rank.append("Queen")
                


    def display_board_Possibilities(self, pX,pY, App, possibles, mouse_click):
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
            
        pX2 = pX+90*mouse_click[1]
        pY2 = pY+90*mouse_click[0]
        square_green(pX2, pY2, App)  
            



    def display_piece(self, loc, App):
        i0 = 0
        sp_loc=[0,0]
        lenX = len(self.piece_Omega)
        while i0 < lenX:
            loc = self.piece_Omega[i0].ret_loc()
            sp_loc[0] = BOARD_X+18+90*loc[1]
            sp_loc[1] = BOARD_Y +15+90*loc[0]
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
            
    def set_up_all_pieces_movements(self):
        i0=0
        while i0 < len(self.piece_Omega):
            if self.piece_Omega[i0].ret_active():
                self.piece_Omega[i0].set_up_poss_mov()
            else:
                self.piece_Omega[i0].no_poss_mov()
            i0+=1
            
    
    def player_display1(self, pX ,pY, App):
        p_D(pX, pY, App)
        one_D(pX+50, pY, App)
        
        
    def player_display2(self, pX, pY, App):
        p_D(pX, pY, App)
        two_D(pX+50, pY, App)
        
    def circle_display(self, pX, pY, App):
        circle_D(pX, pY, App)
    

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
                        
                        
                        #This section is to reference the RANK UP situation
                        if self.rank_occurence == 1:
                            print("RANK SET UP")
                            self.rank_string.clear()
                            self.press_on_rank(loc, self.rank_string)
                            if len(self.rank_string)==1:
                                print("You have Rank up => ", self.mouse_id , " to " , self.rank_string[0])
                                self.piece_Omega[self.mouse_id].set_name(self.rank_string[0])
                                self.rank_occurence = -1
                                
                            
                        
                        
                        elif self.mouse_piece == False:
                            if self.press_on_board( (BOARD_X, BOARD_Y) , loc , self.mouse_control, self.mouse_click):
                                
                                # self.mouse_possibles.clear()
                                # self.mouse_possibles.append((self.mouse_control[0], self.mouse_control[1]))
                                self.mouse_id = self.board_Omega[0].ret_id(self.mouse_control[1], self.mouse_control[0])
                                print("Print board, active mouse; ID=> ", self.mouse_id)
                                
                                #veerify that id is on limit indicates
                                if self.mouse_id < len(self.piece_Omega):
                                    # print("\tPrint board, active mouse; ID=> ", self.mouse_id)
                                    
                                    if self.mouse_id >=0:
                                        print("This is the id: ",self.mouse_id)
                                        self.mouse_piece = True
                                        #This work foor turn respective
                                        if self.white_turn and self.player_Omega1.is_on_play(self.mouse_id):
                                            
                                            print("White Hello")
                                        elif self.black_turn and self.player_Omega2.is_on_play(self.mouse_id):
                                            print("Black Hello2")
                                            
                                        else:
                                            #in case press the piece an not be rregardding turrn; moouse id is sealed
                                            print("Horriblee eerror, you are using wrong piece")
                                            self.mouse_id = -1
                                            self.mouse_piece = False
                                        
                                        # self.set_up_all_pieces_movements()
                                        
                                else:
                                    print("The ID si not respected  to the set pieces")
                            else:
                                print("MISS BOARDD")
                                self.mouse_possibles.clear()
                                self.mouse_id = -1
                        else:
                            #In this section wheen we press the piece, we are moving the piecee
                            poss_click = [-1,-1]
                            if self.press_on_board( (BOARD_X, BOARD_Y) , loc , self.mouse_control, poss_click):
                                print("Press possibility")
                                print("\t Mouse Control ", self.mouse_control)
                                print("\t Mouse Possibility ", self.mouse_possibles)
                                #confirm if kill piece
                                
                                # if self.mouse_control in self.mouse_possibles and self.mouse_id != -1:
                                if self.mouse_id != -1 and (self.mouse_control in self.piece_Omega[self.mouse_id].poss_loc[self.mouse_id]) :
                                    print("\tPossibility on This  id: ",self.mouse_id)
                                    
                                    #section to kill a piece
                                    if self.board_Omega[0].ret_id(self.mouse_control[1], self.mouse_control[0]) != -1:
                                        kill_id = self.board_Omega[0].ret_id(self.mouse_control[1], self.mouse_control[0])
                                        print("A kill should happen on ID => ", kill_id)
                                        self.piece_Omega[kill_id].set_active(False)
                                        #kill color on location
                                        self.board_Omega[0].set_color(self.mouse_control[1], self.mouse_control[0], "n" )
                                        
                                        #check if piece killed is not a KING  => game Over
                                        if self.player_Omega1.game_over():
                                            self.win_p2 = True
                                        if self.player_Omega2.game_over():
                                            self.win_p1 = True
                                        
                                        
                                    #Move piece operation
                                    moveX = self.piece_Omega[self.mouse_id].movement(self.mouse_control[0], self.mouse_control[1])
                                    
                                    
                                    #select the new possibilitiees of pieceson change board
                                    print("\t\t M=> ", moveX)
                                    if moveX == "Rank Up":
                                        self.rank_occurence = 1
                                        print("RANK UP XXXX")
                                    self.set_up_all_pieces_movements()
                                    
                                    
                                    #Change of player turn
                                    if self.white_turn:
                                        self.white_turn = False
                                        self.black_turn = True
                                    else:
                                        self.white_turn = True
                                        self.black_turn = False
                                        
                                    #Check if check occurr
                                    if self.player_Omega1.check():
                                        self.check_p1 = True
                                    else:
                                        self.check_p1 = False
                                        
                                    if self.player_Omega2.check():
                                        self.check_p2 = True
                                    else:
                                        self.check_p2 = False
                                        
                                    
                                    
                                    
                                if self.rank_occurence == -1:    
                                    #I neeed to save the ID, to know which piiecee is being RANK UP    
                                    self.mouse_id = -1
                                self.mouse_piece = False
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
                        self.express -=10
                        
                    if event.key == pygame.K_RIGHT:
                        print("Right key is press")
                        self.express +=10

                    if event.key == pygame.K_UP:
                        print("Up key is press")
                        self.expressY -=10

                    if event.key == pygame.K_DOWN:
                        print("Down key is press")
                        self.expressY +=10
                        
                    if event.key == pygame.K_SPACE:
                        print("Space key button")
                        
                    if event.key == pygame.K_DELETE:
                        print("Delete key button")

                    if event.key == pygame.K_RETURN:
                        print("Enter buttoon is pressed")
                        print("Circle control")
                        print("\tX => " , self.express )
                        print("\tY => " , self.expressY)
                    
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
                        self.piece_Omega[0].set_up_poss_mov()
                        print("This is a poss oof the " , self.mouse_id , "  => ")
                        self.piece_Omega[0].print_poss()
                        
                        
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
                        i0 =0
                        while i0 < len(self.piece_Omega):
                            self.piece_Omega[i0].print_poss()
                            i0 +=1
                        
                    if event.key == pygame.K_i:
                        print("Key i => Set up possibilities")
                        self.set_up_all_pieces_movements()
                        
                    if event.key == pygame.K_j:
                        print("Key j has been pressed")
                        self.piece_Omega[self.mouse_id].print_piece()
                        
                        
                    if event.key == pygame.K_k:
                        print("Key k has been pressed")
                        if self.player_Omega1.check2():
                            print("YOU ARE IN CHECK P1")
                        else:
                            print("YOU ARE NOT CHECK, P1")
                        if self.player_Omega2.check2():
                            print("YOU ARE IN CHECK, Player2")
                        else:
                            print("YOU ARE NOT CHECK, P2")
                        
                    if event.key == pygame.K_l:
                        print("Key l has been pressed")
                        self.print_location_board(self.mouse_control) 
                        
                    if event.key == pygame.K_m:
                        print("Key m has been pressed")
                        self.player_Omega1.print_king()
                        self.player_Omega2.print_king()
                
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

            
            App.screen.fill(GREEN)
            #if bellow screen.fill, then the image will be bellow the color
            #here start the display image

            # This is thee display section
            
            border_potrait(BOARD_X-10, BOARD_Y-10, App)
            if self.mouse_piece == False:
                 self.display_board( BOARD_X, BOARD_Y, App, loc)
            else:
                self.display_board_Possibilities(BOARD_X, BOARD_Y , App, self.piece_Omega[self.mouse_id].poss_loc[self.mouse_id], self.mouse_click)
            self.display_piece(loc, App)
            
            if self.rank_occurence == 1:
                self.display_rank_board(BOARD_X +90, 275, App, loc)
                
                
            self.player_display1( 55,200, App)
            
            self.player_display2( 1015 , 200, App)
            
            if self.white_turn:
                self.circle_display( 40, 160, App)
            else:
                self.circle_display( 1000, 160 , App)
                
            # P1 => x=50, y=110
            # P2 => x=1010, y=110
            if self.check_p1:
                px_c = 50
                py_c = 110
                self.display_Check(px_c, py_c, App)
            elif self.check_p2:
                px_c = 1010
                py_c = 110
                self.display_Check(px_c, py_c, App)
                
            if self.win_p2 == True:
                self.display_Win(BOARD_X +90, 275, App, "P2")
            elif self.win_p1 == True:
                self.display_Win(BOARD_X +90, 275, App, "P1")
                
            
                
            
            # pygame.draw.rect(App.screen, RED, App.rect, 1)
            pygame.display.update()
            
        pygame.quit()
        
        
if __name__ == '__main__':
    App().run()