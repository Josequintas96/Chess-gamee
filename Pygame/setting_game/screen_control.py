
from pygame import *

import sys
sys.path.append('../')
from App import *


def square_black(pX, pY, sizeT, poss, App):
    # design of the back card
    IMAGE_SIZE= (110,110)
    if sizeT == True:
        # print("\tRise Square => ", pX, " ", pY)
        # sq_black_t = pygame.transform.scale(sq_black, (IMAGE_SIZE))
        # App.screen.blit(special_black,(pX-5, pY-5))
        if poss == False:
            App.screen.blit(special_black,(pX, pY))
        else:
            App.screen.blit(special2_black,(pX, pY))
    else:
        App.screen.blit(sq_black,(pX, pY))
        
def square_blank(pX, pY, sizeT, poss, App):
    # design of the back card
    IMAGE_SIZE= (110,110)
    if sizeT == True:
        # print("\tRise Square => ", pX, " ", pY)
        # sq_blank_t = pygame.transform.scale(sq_blank, (IMAGE_SIZE))
        # App.screen.blit(special_blank,(pX-5, pY-5))
        if poss == False:
            App.screen.blit(special_blank,(pX, pY))
        else:
            App.screen.blit(special2_blank,(pX, pY))
    else:
        App.screen.blit(sq_blank,(pX, pY))
        
def square_board(pX, pY, App, loc):
    #pX = 280
    #pY = 275
    #sizeof the pieces = 100
    App.screen.blit( Sboard, (pX,pY))
    pX2 = pX+40
    pY2 = pY+120

    App.screen.blit(RRook, (pX2, pY2))
    i0 = 1
    App.screen.blit(Rhorse, (pX2+120*i0, pY2))
    i0 += 1
    App.screen.blit(Rbishop, (pX2+120*i0, pY2))
    i0 += 1
    App.screen.blit(RQueen, (pX2+120*i0, pY2))
    
    i0 =0
    while i0< 4:
        if loc[1] > pY2 and loc[1] < pY2+100:
            if loc[0] > pX2+120*i0 and loc[0]< pX2+120*i0+100:
                App.screen.blit(Rsquare, (pX2+120*i0, pY2))
        i0+=1

        
def pawn_P(pX, pY, color, App):
    if color == "White":
        App.screen.blit( white_pawn, (pX-5, pY-5))
    elif color == "Black":
        App.screen.blit( black_pawn, (pX-5, pY-5))

def horse_P(pX, pY, color, App):
    if color == "White":
        App.screen.blit( white_horse, (pX-5, pY-5))
    elif color == "Black":
        App.screen.blit( black_horse, (pX-5, pY-5))        


def rook_P(pX, pY, color, App):
    if color == "White":
        App.screen.blit( white_rook, (pX-5, pY-5))
    elif color == "Black":
        App.screen.blit( black_rook, (pX-5, pY-5))


def bishop_P(pX, pY, color, App):
    if color == "White":
        App.screen.blit( white_bishop, (pX-5, pY-5))
    elif color == "Black":
        App.screen.blit( black_bishop, (pX-5, pY-5))
        
def queen_P(pX, pY, color, App):
    if color == "White":
        App.screen.blit( white_queen, (pX-5, pY-5))
    elif color == "Black":
        App.screen.blit( black_queen, (pX-5, pY-5))
        
def king_P(pX, pY, color, App):
    if color == "White":
        App.screen.blit( white_king, (pX-5, pY-5))
    elif color == "Black":
        App.screen.blit( black_king, (pX-5, pY-5))


