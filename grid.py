from random import randint
import numpy as np
import pygame

width, height = 900, 750
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ahmed's Tic Tac Toc")


Red = (94, 3, 16)
white = (255, 255, 255)
purple = (129, 9, 107)
green = (50, 150, 20)
Old_BG_color = (28, 110, 96)
Old_line_color = (23, 135, 145)
New_BG_color1 = (118, 110, 96)
New_Line_color2 = (153, 135, 145)
denmark_Bg , denmark_lines = (154, 25, 24) , (225, 156, 165)
unkown1 , Unkown1 = (191, 144, 247) , (58, 58, 142)
unkown2 , Unkown2 = (26, 72, 195) , (22, 215, 233)
unkown3 , Unkown3 = (68, 33, 36) , (57, 176, 155)
blue_BG ,blue_line =(37, 35, 99) , (42, 72, 171)
pink_line = (162, 87, 155)
New_BG_color = (randint(0, 180), randint(0, 180), randint(0, 180))
New_Line_color = (randint(0, 180), randint(0, 180), randint(0, 180))
print(New_BG_color , ",", New_Line_color)

board_row, board_col = 3, 3
board = np.zeros((board_row, board_col))


def bg():
    screen.fill(New_BG_color)

    # horizontal lines
    hl1 = pygame.draw.line(screen, New_Line_color, (0, height - 500), (width, height - 500), 15)
    hl2 = pygame.draw.line(screen, New_Line_color, (0, height - 250), (width, height - 250), 15)
    # vertical lines
    vl1 = pygame.draw.line(screen, New_Line_color, (width - 600, 0), (width - 600, height), 15)
    vl2 = pygame.draw.line(screen, New_Line_color, (width - 300, 0), (width - 300, height), 15)


def Xo():
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col] == 1:
                x = 150 + 300 * col
                y = 125 + 250 * row
                pygame.draw.line(screen, Red, (x + 50, y + 50), (x - 50, y - 50), 10)
                pygame.draw.line(screen, Red, (x - 50, y + 50), (x + 50, y - 50), 10)

            elif board[row][col] == 2:
                pygame.draw.circle(screen, white, ((col * 300 + 150), (row * 250 + 125)), 50, 10)


def mark_square(row, col, player):
    board[row][col] = player


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(board_row):
        for col in range(board_col):
            if board[row][col] == 0:
                return False

    return True


def horizontal_line(col, player):
    PosY = col * 300 + 150
    if player == 1:
        color = purple
    elif player == 2:
        color = green
    pygame.draw.line(screen, color, (PosY, 15), (PosY, height - 15), 10)


def vertical_line(row, player):
    PosX = row * 250 + 125
    if player == 1:
        color = purple
    elif player == 2:
        color = green
    pygame.draw.line(screen, color, (15, PosX), (width - 15, PosX), 10)


def diagonal1(player):
    if player == 1:
        color = purple
    elif player == 2:
        color = green
    pygame.draw.line(screen, color, (0, 0), (width, height), 10)


def diagonal2(player):
    if player == 1:
        color = purple
    elif player == 2:
        color = green
    pygame.draw.line(screen, color, (0, height), (width, 0), 10)


def check_win(player):
    for row in range(board_row):
        if board[row][0] == board[row][1] == board[row][2] == player:
            vertical_line(row, player)
            return True
    for col in range(board_col):
        if board[0][col] == board[1][col] == board[2][col] == player:
            horizontal_line(col, player)
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        diagonal1(player)
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        diagonal2(player)
        return True
    return False


def restart():
    bg()
    for row in range(board_row):
        for col in range(board_col):
            board[row][col] = 0
