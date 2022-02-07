import numpy as np
import pygame

width, height = 900, 750
screen = pygame.display.set_mode((width, height))

Red = (255, 0, 0)
white = (255,255,255)
purple = (100,0,100)
BG_color = (28, 110, 96)
new_color = (23, 135, 145)
board_row, board_col = 3, 3
board = np.zeros((board_row, board_col))


def bg():
    screen.fill(BG_color)

#horizontal lines
    hl1 = pygame.draw.line(screen, new_color, (0, height - 500), (width, height - 500), 15)
    hl2 = pygame.draw.line(screen, new_color, (0, height - 250), (width, height - 250), 15)
#vertical lines
    vl1 = pygame.draw.line(screen, new_color, (width - 600, 0), (width - 600, height), 15)
    vl2 = pygame.draw.line(screen, new_color, (width - 300, 0), (width - 300, height), 15)



def Xo():
	for row in range(board_row):
		for col in range(board_col):
			if board[row][col] == 1:

				pygame.draw.line(screen, Red, ((col * 300 + 150), (row * 250 + 250 - 200)),((col * 300 + 300 - 200), (row * 250 + 175)), 10)
				pygame.draw.line(screen, Red, ((col * 300 + 300 - 200), (row * 250 + 250 - 200)), ((col * 300 + 150), (row * 250 + 175)), 10)




			elif board[row][col] == 2:
				pygame.draw.circle(screen, white, (int(col * 300 + 150), int(row * 250 + 125)), 50, 10)




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

def horizontal_line(col,player):
	PosY = col * 300 + 150
	if player == 1:
		color = Red
	elif player == 2:
		color = white
	pygame.draw.line(screen, color, (PosY, 15), (PosY, height-15), 10)

def vertical_line(row, player):
	PosX = row * 250 + 125
	if player == 1:
		color = Red
	elif player == 2:
		color = white
	pygame.draw.line(screen, color, (15, PosX), (width - 15, PosX), 10)

def diagonal1(player):
	if player == 1:
		color = Red
	elif player == 2:
		color = white
	pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), 10)

def diagonal2(player):
	if player == 1:
		color = Red
	elif player == 2:
		color = white
	pygame.draw.line(screen, color, (15, height - 15), (width, 15), 10)

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
		return  True
	if board[0][2] == board[1][1] == board[2][0] == player:
		diagonal2(player)
		return  True
	return  False

def restart():
	bg()
	Xo()
	for row in range(board_row):
		for col in range(board_col):
			board[row][col] = 0

