import random
import time
import os
import sys

# Add project root to path, so pslab can be found, even if not installed:
base_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(base_dir, "..", ".."))

import pslab


class Cell:
	
	cover = pslab.Slab(64, 64)
	cover.fill(0xFF0000)
	stcl = pslab.Slab(
		cover.getWidth() - 2,
		cover.getHeight() - 2,
		)
	stcl.fill(0x333333)
	stcl.burnInto(cover, 1, 1)

	
	def __init__(self, image):
		
		self.image = image
		self.image_visible = self.cover
	
	def __eq__(self, other):
		
		return self.image_visible == other.image_visible
	
	def __ne__(self, other):
		
		return not self.__eq__(other)

	
	def flip(self):
		
		if self.image_visible == self.image:
			self.image_visible = self.cover
		else:
			self.image_visible = self.image
	
	def getImage(self):
		
		return self.image_visible
	

	def isCovered(self):
		
		return self.image_visible == self.cover



class Board(list):

	def __init__(self, cells):
		
		super().__init__(cells)
		random.shuffle(self)

		self.position = (0, 0)
		self.grid_dim = (3, 3)
	
	
	def setPosition(self, x, y):
		
		self.position = (x, y)
		

	def isComplete(self):

		for cell in self:
			if cell.isCovered():
				return False
		return True
	

	def burnInto(self, window):

		x, y = self.position
		gd_x, gd_y = self.grid_dim
		
		for i, cell in enumerate(self):
			slab = cell.getImage()
			s_x = x + (i % gd_x) * slab.getWidth()
			s_y = y + (i // gd_y) * slab.getHeight()
			slab.burnInto(window, s_x, s_y)
	

	def posToIdx(self, x, y):

		img = self[0].getImage()
		cell_dim = (img.getWidth(), img.getHeight())

		x, y = [e[0] - e[1] for e in zip((x, y), self.position)]
		x, y = [e[0] // e[1] for e in zip((x, y), cell_dim)]

		gd_w = self.grid_dim[0]

		if x > gd_w - 1 or x < 0:
			return -1

		return x + gd_w * y



class Player:
	
	def __init__(self):

		self.steps_taken = 0
		self.flipped = []
	

	def flipCell(self, cell):

		cell.flip()

		self.steps_taken += 1
		self.flipped.append(cell)


	def flippedNewPair(self):
		
		return len(self.flipped) == 2


	def getPair(self):
		
		return (self.flipped.pop(), self.flipped.pop())

	
	def coverPair(self, cell_pair):
		
		for cell in cell_pair:
			cell.flip()

		

if __name__ == "__main__":

	window = pslab.Window(512, 512)

	player = Player()

	cover = Cell.cover
	images = [pslab.SlabImg(os.path.join("images", f)) for f in os.listdir("images")]

	board = Board([Cell(image) for image in images * 2])
	board.setPosition(150, 150)

	sf = lambda f: os.path.join("sounds", f)
	sound_flip = pslab.Sound(sf("flip.wav")) 
	sound_match = pslab.Sound(sf("match.wav"))
	sound_win = pslab.Sound(sf("win.wav"))


	def getUserInput():

		while True:

			window.processEvents()
			mouse = window.mouse

			if mouse.btnHit("lmb"):
				mp = mouse.getPosition()
				return str(board.posToIdx(mp[0], mp[1]))
			if mouse.btnHit("rmb"):
				return 'q'

			time.sleep(0.032)


	def inputIsValid(user_input):
		return user_input.isdigit() and \
			int(user_input) < len(board) and \
			board[int(user_input)].isCovered()


	def victory_burnInto(slab):

		font_path = os.path.join("fonts", "DejaVuSansMono.ttf")
		text = "You won in {:d} steps.".format(player.steps_taken)
		slab_txt = pslab.SlabText(font_path, 24, 0xFFFFFF, 0, text)
		slab_txt.burnInto(slab, 100, 24)
		slab_txt.setText("Press any mouse button to quit.")
		slab_txt.update()
		slab_txt.burnInto(slab, 45, 400)
	

	

	while True:

		board.burnInto(window)

		if board.isComplete():
			victory_burnInto(window)
			window.update()
			sound_win.play()
			getUserInput()
			break

		window.update()
		window.fill(0)
			

		if player.flippedNewPair():
			a, b = player.getPair()
			if a != b:
				player.coverPair((a, b))
			else:
				sound_match.play()


		user_input = getUserInput()


		if user_input == 'q':
			break


		if inputIsValid(user_input):

			idx = int(user_input)

			player.flipCell(board[idx])
			sound_flip.play()
