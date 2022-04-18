#Same as the old classes
import random
class Tile:
	def __init__(self,x,y,val=0):
		self.x = x
		self.y = y
		self.val = val
		
	def __str__(self):
		"""Hello world"""
		# return "x = " + str(self.x) + "\ny = " + str(self.y) + "\nval = " + str(self.val)
		return str(self.val)
		
	def __eq__(self, t):
		return self.val==t.val

class Board:
	def __init__(self):
		self.board = [Tile(x,y) for y in range(0,4) for x in range(0,4)]
		self.empty = [x for x in range(0,16)]
		
	def addTile(self):
		self.findEmpty()
		pos = random.choice(self.empty)
		self.empty.remove(pos)
		rand = random.randint(1,10)
		if rand < 10:
			self.board[pos].val = 1
		else:
			self.board[pos].val = 2 
		
	def findEmpty(self):
		self.empty = []
		for i in range(0,16):
			if self.board[i].val == 0:
				self.empty.append(i)
		
	def verMove(self,dir): #direction: "s"->aşağı 1->yukarı
		tempboard = Board()
		for i in range(16):
			tempboard.board[i].val = self.board[i].val
		
		if dir == "w":
			iterdir=-1
		elif dir == "s":
			iterdir = 1
			
		for x in range(0,4):
			if dir == "w":
				itery=4
				emptysq = 4
			else:
				itery=-1
				emptysq = -1
				
			lastval = -1	
			
			while True:
				itery += iterdir
				if itery not in range(0,4):
					break
				if emptysq in range(0,4):
					if self.board[4*itery+x].val:
						if lastval != self.board[4*itery+x].val:
							lastval = self.board[4*itery+x].val
							self.board[4*itery+x].val = 0
							self.board[4*emptysq+x].val = lastval
							emptysq += iterdir
						else:
							self.board[4*(emptysq-iterdir)+x].val=lastval+1
							self.board[4*itery+x].val = 0
							lastval = -1
				else:
					if self.board[4*itery+x].val==0:
						emptysq = itery
					else:
						if lastval != self.board[4*itery+x].val: 
							lastval = self.board[4*itery+x].val
						else:
							self.board[4*(itery-iterdir)+x].val = lastval +1
							self.board[4*itery+x].val = 0
							emptysq = itery
							lastval = -1
		
		if self.board == tempboard.board:
			return 0
		return 1
									
	def horMove(self,dir): #direction "a"->sol, "d"->sağ
		tempboard = Board()
		for i in range(16):
			tempboard.board[i].val = self.board[i].val
		
		if dir == "d":
			iterdir = -1
		elif dir == "a":
			iterdir = 1
			
		for y in range(0,4):
			if dir == "d":
				iterx = 4
				emptysq = 4
			else:
				iterx = -1
				emptysq = -1
				
			lastval = -1	
			
			while True:
				iterx += iterdir
				if iterx not in range(0,4):
					break
				if emptysq in range(0,4):
					if self.board[4*y+iterx].val:
						if lastval != self.board[4*y+iterx].val:
							lastval = self.board[4*y+iterx].val
							self.board[4*y+iterx].val = 0
							self.board[4*y+emptysq].val = lastval
							emptysq += iterdir
						else:
							self.board[4*y+(emptysq-iterdir)].val=lastval+1
							self.board[4*y+iterx].val = 0
							lastval = -1
				else:
					if self.board[4*y+iterx].val==0:
						emptysq = iterx
					else:
						if lastval != self.board[4*y+iterx].val: 
							lastval = self.board[4*y+iterx].val
						else:
							self.board[4*y+(iterx-iterdir)].val = lastval +1
							self.board[4*y+iterx].val = 0
							emptysq = iterx
							lastval = -1
		
		if self.board == tempboard.board:
			return 0
		return 1
							
	def end(self):
		if len(self.empty):
			return 0
		
		for y in range(0,4):
			for x in range(0,4):
				if x != 3:
					if self.board[4*y+x].val == self.board[4*y+x+1].val:
						return 0
				if y != 3:
					if self.board[4*y+x].val == self.board[4*y+x+4].val:
						return 0
		return 1