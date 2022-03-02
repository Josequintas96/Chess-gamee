# import pygame
from setting_game.download_control import *

# from settings_game.collection_object import *
# from settings_game.display_control import *
import sys


sys.path.append('../')
from Board import *
from Piece import *


pygame.init()


#title
pygame.display.set_caption("Chess")
iconS = pygame.image.load("Image/chess.png")
pygame.display.set_icon(iconS)

#size of the window
screen = pygame.display.set_mode((900,800)) #height X:800  weight Y: 600
                    #start at left up corner


            
            




text = ""

offset_m = [0,0]


def square_blank(pX, pY, sizeT):
    # design of the back card
    IMAGE_SIZE= (110,110)
    if sizeT == True:
        # print("\tRise Square => ", pX, " ", pY)
        sq_blank_t = pygame.transform.scale(sq_blank, (IMAGE_SIZE))
        screen.blit(sq_blank_t,(pX-5, pY-5))
    else:
        screen.blit(sq_blank,(pX, pY))

    
def square_black(pX, pY, sizeT):
    # design of the back card
    IMAGE_SIZE= (110,110)
    if sizeT == True:
        # print("\tRise Square => ", pX, " ", pY)
        sq_black_t = pygame.transform.scale(sq_black, (IMAGE_SIZE))
        screen.blit(sq_black_t,(pX-5, pY-5))
    else:
        screen.blit(sq_black,(pX, pY))
        
        
def pawn_P(pX, pY, color):
    if color == "White":
        screen.blit( white_pawn, (pX-5, pY-5))
    elif color == "Black":
        screen.blit( black_pawn, (pX-5, pY-5))

# def score_d(pX,pY,numb):
#     if numb ==0:
#         screen.blit(numb_0,(pX, pY))
#     elif numb ==1:
#         screen.blit(numb_1,(pX, pY))
#     elif numb==2:
#         screen.blit(numb_2,(pX, pY))
#     elif numb ==3:
#         screen.blit(numb_3,(pX, pY))
#     elif numb==4:
#         screen.blit(numb_4,(pX, pY))
#     elif numb==5:
#         screen.blit(numb_5,(pX, pY))
#     elif numb==6:
#         screen.blit(numb_6,(pX, pY))
#     elif numb==7:
#         screen.blit(numb_7,(pX, pY))
#     elif numb==8:
#         screen.blit(numb_8,(pX, pY))
#     elif numb==9:
#         screen.blit(numb_9,(pX, pY))




def display_board(pX,pY, loc, board_Omega):
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
                    square_blank(pX2, pY2, False)
                    colorB = False
                else:
                    square_black(pX2, pY2, False)
                    colorB = True
            i1+=1
        i0+=1
        if colorB==True:
            colorB = False
        else:
            colorB = True
    if touch_sq == True:
        if touch_color == True:
            square_blank(touch_loc[0], touch_loc[1], True)
        else:
            square_black( touch_loc[0], touch_loc[1], True )
            
            
def display_board_Possibilities(pX,pY, board_Omega, possibles):
    i0 = 0
    colorB = True # Tue man whitee while Flase mean Black
    poss = len(possibles) #group of locatoiojn to outshine
    #seequence values regarding correspoding colors
    coord = []
    color_coor = []
    i_p = 0
    
    while i0 <8:
        i1 = 0
        while i1 < 8:
            pX2 = pX+90*i0
            pY2 = pY+90*i1
            #remember the coordinatee/location of pieeces are the twisted X/Y or i0/i1
            if i_p < poss and possibles[i_p][0] != i1 and possibles[i_p][1] != i0:
                if colorB == True:
                    square_blank(pX2, pY2, False)
                    colorB = False
                else:
                    square_black(pX2, pY2, False)
                    colorB = True
            else:
                coord.append((pX2,pY2))
                color_coor.append(colorB)
                i_p+=1
                if colorB == True:
                    square_blank(pX2, pY2, False)
                    colorB = False
                else:
                    square_black(pX2, pY2, False)
                    colorB = True
            i1+=1
        i0+=1
        if colorB==True:
            colorB = False
        else:
            colorB = True
            
    i_p =0
    while i_p < poss:
        if color_coor[i_p] == True:
            square_blank(coord[i_p][0], coord[i_p][1], True)
        else:
            square_black( coord[i_p][0], coord[i_p][1], True )
        i_p+=1
            


def press_on_board(coordinate, loc, mouse_control):
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
            
            i1+=1
        i0+=1
            
    

def display_piece(loc, piece_Omega):
    sp_loc = piece_Omega[0].ret_coordinate()
    if piece_Omega[0].ret_name() == "Pawn":
        pawn_P(sp_loc[0], sp_loc[1], piece_Omega[0].ret_color())
        
def print_location_board(loc):
    print("Location Board: ")
    print("\t X: ", loc[0])
    print("\t Y: ", loc[1])        
   



running = True

#create the board variable
boardX = Board()
board_Omega = []
board_Omega.append(boardX)

PieceX = Piece("Pawn", "White",  board_Omega, (118, 65))
piece_Omega = []
piece_Omega.append(PieceX)

#mouse control settings
mouse_piece = False #in casee themousee press thee piece or board,seee possibilities
mouse_control= []
#in case of press a squaree with a piecee then save X/Y location of board
mouse_control.append(-1)
mouse_control.append(-1) 
mouse_possibles = []

while running:
    
    mx, my = pygame.mouse.get_pos()
    rot = 0
    loc = [mx , my]
    
    #screen.blit(pygame.transform.rotate(img,rot),(loc[0]+offset_m[0], loc[1]+offset[1]))
    
    
    # #print("Super Array => ", gameX.array_illustration())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("location is ", loc)
                if mouse_piece == False:
                    press_on_board( (100, 50) , loc , mouse_control)
                    mouse_piece = True
                    mouse_possibles.append((mouse_control[0], mouse_control[1]))
                else:
                    mouse_piece = False
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                print("Button rise")
                #print("\tLocation when button rise: ", loc) 
                
            

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
                piece_Omega[0].board[0].print_cordinate()

            if event.key == pygame.K_b:
                print("Key b has been pressed")
                piece_Omega[0].locate_piece(4,6)
                piece_Omega[0].board[0].print_piece_set()
                
            if event.key == pygame.K_c:
                print("Key c has been pressed")
                
            if event.key == pygame.K_d:
                print("Key d has been pressed")
                
            if event.key == pygame.K_e:
                print("Key e has been pressed")
                
            if event.key == pygame.K_f:
                print("Key f has been pressed")
                
            if event.key == pygame.K_g:
                print("Key g has been pressed")

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
                print_location_board(mouse_control)
                
            if event.key == pygame.K_m:
                print("Key m has been pressed")
                
            if event.key == pygame.K_n:
                print("Key n has been pressed")
                
            if event.key == pygame.K_o:
                print("Key o has been pressed")
                
            if event.key == pygame.K_p:
                print("Key p has been pressed")
                
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

    
    screen.fill((155 , 155, 155))
    #if bellow screen.fill, then the image will be bellow the color
    #heere start the display image

    if mouse_piece == False:
        display_board(100, 50, loc, board_Omega)
    else:
        display_board_Possibilities(100, 50, board_Omega, mouse_possibles)
    display_piece(loc, piece_Omega)

    
    pygame.display.update()
    
pygame.quit()
 
