from turtle import circle
import pygame


#image download paths:
image_special_R = "Image/special_R/"
sq_blank = pygame.image.load(image_special_R + "blank_square.png")
sq_black = pygame.image.load(image_special_R + "black_square.png")
special_blank = pygame.image.load(image_special_R + "spcial_square_blank.png")
special_black = pygame.image.load(image_special_R + "spcial_square_black.png")
special2_blank = pygame.image.load(image_special_R + "spcial2_square_blank.png")
special2_black = pygame.image.load(image_special_R + "spcial2_square_black.png")
Sboard = pygame.image.load(image_special_R + "Sboard.png")

Rhorse = pygame.image.load(image_special_R + "R_Horse.png")
Rbishop = pygame.image.load(image_special_R + "R_Bishop.png")
RQueen = pygame.image.load(image_special_R + "R_Queen.png")
RRook = pygame.image.load(image_special_R + "R_Rook.png")
Rsquare = pygame.image.load(image_special_R + "R_square.png")

lett_p = pygame.image.load(image_special_R + "p_64.png")
one_p = pygame.image.load(image_special_R + "one_64.png")
two_p = pygame.image.load(image_special_R + "two_64.png")
circle_p = pygame.image.load(image_special_R + "circle.png")
green_square = pygame.image.load(image_special_R + "S_square_board.png")
check_d = pygame.image.load(image_special_R + "CHECK.png")
mate_d = pygame.image.load(image_special_R + "MATE.png")
winner_d = pygame.image.load(image_special_R + "WINNER.png")
p1_d  = pygame.image.load(image_special_R + "P1.png")
p2_d  = pygame.image.load(image_special_R + "P2.png")

border_s = pygame.image.load(image_special_R + "Cheess_portrait.png")


#pieces
image_piece = "Image/pieces/"
black_pawn = pygame.image.load(image_piece + "Sblack_pawn64.png")
black_horse = pygame.image.load(image_piece + "Sblack_horse64.png")
black_bishop = pygame.image.load(image_piece + "Sblack_bishop64.png")
black_king = pygame.image.load(image_piece + "Sblack_king64.png")
black_queen = pygame.image.load(image_piece + "Sblack_queen64.png")
black_rook = pygame.image.load(image_piece + "Sblack_rook64.png")

white_pawn = pygame.image.load(image_piece + "Swhite_pawn64.png")
white_horse = pygame.image.load(image_piece + "Swhite_horse64.png")
white_bishop = pygame.image.load(image_piece + "Swhite_bishop64.png")
white_king = pygame.image.load(image_piece + "Swhite_king64.png")
white_queen = pygame.image.load(image_piece + "Swhite_queen64.png")
white_rook = pygame.image.load(image_piece + "Swhite_rook64.png")


# congratulation = pygame.image.load(image_special_R + "congratulation_512.png")