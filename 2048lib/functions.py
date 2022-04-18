#Old initialize with minor changes
import random
def initialize(board):
	x1 = random.randint(0,3)
	y1 = random.randint(0,3)
	x2 = random.randint(0,2)
	y2 = random.randint(0,2)
	
	if x2>=x1:
		x2+=1
	if y2>=y1:
		y2+=1
	
	t1val = random.randint(1,2)
	if t1val == 2:
		t2val = 1
	else:
		t2val = random.randint(1,2)	
	
	board.board[4*y1+x1].val=t1val
	board.board[4*y2+x2].val=t2val
	
	#board.findEmpty() ile aynı şey
	board.empty.remove(4*y1+x1)
	board.empty.remove(4*y2+x2)
	
	# print("Tile 1 coordinates: (", x1, ",", y1, ")\nTile 2 coordinates: (", x2,",", y2, ")\nTile 1 value: ", t1val, "\nTile 2 value: ", t2val, "\nEmpty indexes: ", board.empty, sep="")
	