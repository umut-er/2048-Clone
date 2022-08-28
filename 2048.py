#11 remastered with pygame
import pygame
import os
import random
import sys
import old11

pygame.font.init()

WIDTH, HEIGHT = 900, 700

WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #surface
pygame.display.set_caption("2048")

BOARD_CONSTANT = 10

FPS = 60

FONT = pygame.font.SysFont("comicsans", 400)

class COLORS:
	WHITE = (255,255,255)
	BLACK = (0,0,0)
	GREY = (128,128,128)
	RED = (255,0,0)

class TILES:
	TILE0 = pygame.image.load(os.path.join('assets', '0.png'))
	TILE1 = pygame.image.load(os.path.join('assets', '2.png'))
	TILE2 = pygame.image.load(os.path.join('assets', '4.png'))
	TILE3 = pygame.image.load(os.path.join('assets', '8.png'))
	TILE4 = pygame.image.load(os.path.join('assets', '16.png'))
	TILE5 = pygame.image.load(os.path.join('assets', '32.png'))
	TILE6 = pygame.image.load(os.path.join('assets', '64.png'))
	TILE7 = pygame.image.load(os.path.join('assets', '128.png'))
	TILE8 = pygame.image.load(os.path.join('assets', '256.png'))
	TILE9 = pygame.image.load(os.path.join('assets', '512.png'))
	TILE10 = pygame.image.load(os.path.join('assets', '1024.png'))
	TILE11 = pygame.image.load(os.path.join('assets', '2048.png'))
		
def convert(tile):
	if tile.val == 0:
		return TILES.TILE0 
	if tile.val == 1:
		return TILES.TILE1
	if tile.val == 2:
		return TILES.TILE2
	if tile.val == 3:
		return TILES.TILE3
	if tile.val == 4:
		return TILES.TILE4
	if tile.val == 5:
		return TILES.TILE5
	if tile.val == 6:
		return TILES.TILE6
	if tile.val == 7:
		return TILES.TILE7
	if tile.val == 8:
		return TILES.TILE8
	if tile.val == 8:
		return TILES.TILE8
	if tile.val == 9:
		return TILES.TILE9
	if tile.val == 10:
		return TILES.TILE10
	if tile.val == 11:
		return TILES.TILE11

def draw_board(board,rect):
	#Leftmost piece (235,135)
	WIN.fill(COLORS.GREY)
	for tile in board.board:
		img = convert(tile)
		WIN.blit(img, ((WIDTH//2-BOARD_CONSTANT//2*3-2*100)+(100+BOARD_CONSTANT)*tile.x, HEIGHT//2+BOARD_CONSTANT//2*3+100-(100+BOARD_CONSTANT)*tile.y))
	
	pygame.display.update(rect)
	
def gameend():
	text = FONT.render("Ez.", 1, COLORS.RED)
	WIN.blit(text, ((WIDTH-text.get_size()[0])//2,(HEIGHT-text.get_size()[1])//2))
	pygame.display.update()

def main():
	board = old11.classes.Board()
	old11.functions.initialize(board)
	run = True
	clock = pygame.time.Clock()
	game_area = pygame.Rect(WIDTH//2-BOARD_CONSTANT//2*3-2*100, HEIGHT//2-BOARD_CONSTANT//2*3-2*100, 4*100+3*BOARD_CONSTANT, 4*100 + 3*BOARD_CONSTANT)
	WIN.fill(COLORS.BLACK)
	pygame.display.update()
	while run:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					if board.horMove("a"):
						board.addTile()
				if event.key == pygame.K_d:
					if board.horMove("d"):
						board.addTile()
				if event.key == pygame.K_w:
					if board.verMove("w"):
						board.addTile()
				if event.key == pygame.K_s:
					if board.verMove("s"):
						board.addTile()
				if event.key == pygame.K_RCTRL:
					run = False
					gameend()
					current_time = pygame.time.get_ticks()
					while pygame.time.get_ticks()-current_time<3000:
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								run = False
								pygame.quit()
								sys.exit()
		
		draw_board(board,game_area)
						
		if board.end():
			gameend()
			current_time = pygame.time.get_ticks()
			while pygame.time.get_ticks()-current_time<3000:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						run = False
						pygame.quit()
						sys.exit()
			break

	main()
	
if __name__ == '__main__':
 	main() 
