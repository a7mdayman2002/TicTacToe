import numpy as np
import pygame

width, height = 900, 750
screen = pygame.display.set_mode((width, height))

Red = (255, 0, 0)
BG_color = (28, 110, 96)
new_color = (23, 135, 145)
board_row, board_col = 3, 3
board = np.zeros((board_row, board_col))

def bg():
    screen.fill(BG_color)

#horizontal lines
    pygame.draw.line(screen, new_color, (0, 350), (width, 350), 15)
    pygame.draw.line(screen, new_color, (0, 550), (width, 550), 15)
#vertical lines
    pygame.draw.line(screen, new_color, (width - 600, 150), (width - 600, height - 5), 15)
    pygame.draw.line(screen, new_color, (width - 300, 150), (width - 300, height - 5), 15)


def boundaries():
#box horizontal boundaries
    pygame.draw.line(screen, new_color, (10, 150), (width, 150), 15)
    pygame.draw.line(screen, new_color, (10, height - 5), (width, height - 5), 15)
# box vertical boundaries
    pygame.draw.line(screen, new_color, (0, 150), (0, height - 5), 20)
    pygame.draw.line(screen, new_color, (width, 150), (width, height - 5), 20)

def XO():
	for row in range(board_row):
		for col in range(board_col):
			if board[row][col] == 1:
				pygame.draw.circle( screen, Red,(10, 60), (30, 100), 5,20 )
			elif board[row][col] == 2:
				pygame.draw.line(screen, Red, (10, 60), (30, 100), 10)
				pygame.draw.line(screen, Red, (10, 60), (30, 100), 10)

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






