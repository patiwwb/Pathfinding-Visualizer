import sys
import pygame

INFINITY = sys.maxsize

INKWELL = (94, 97,109)
BUTTERCREAM = (239, 225, 206)
DESERT_MIST = (224, 181, 137)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (200, 200, 200)
TURQUOISE = (64, 224, 208)
WILLOW = (154, 139, 79)
PINK = (255,192,203)

class Node:
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = BUTTERCREAM
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows
		self.distance = INFINITY
		self.visited = False
		self.previous = None

	def get_pos(self):
		return self.row, self.col

	def is_closed(self):
		return self.color == RED

	def is_open(self):
		return self.color == DESERT_MIST

	def is_wall(self):
		return self.color == BLACK

	def is_start(self):
		return self.color == ORANGE

	def is_end(self):
		return self.color == WILLOW

	def reset(self):
		self.color = BUTTERCREAM

	def make_start(self):
		self.color = ORANGE

	def make_closed(self):
		self.color = RED

	def make_open(self):
		self.color = DESERT_MIST

	def make_wall(self):
		self.color = BLACK

	def make_end(self):
		self.color = WILLOW

	def make_path(self):
		self.color = INKWELL
	
	def make_color(self):
		self.color = PINK

	def mark(self):
		self.color = YELLOW

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_wall(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_wall(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def update_unvisited_neighbors(self,grid):
		#Get unvisited neighbors
		self.unvisited_neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall(): # DOWN
			self.unvisited_neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_wall(): # UP
			self.unvisited_neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall(): # RIGHT
			self.unvisited_neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_wall(): # LEFT
			self.unvisited_neighbors.append(grid[self.row][self.col - 1])		
		self.unvisited_neighbors = [node for node in self.unvisited_neighbors if node.visited==False]
		#Update unvisited neighbors
		for neighbor in self.unvisited_neighbors:
			neighbor.distance = self.distance + 1
			neighbor.previous = self

	def __lt__(self, other):
		return False