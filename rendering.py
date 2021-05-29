import pygame
import random
from node import *

def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
	win.fill(BUTTERCREAM)

	for row in grid:
		for node in row:
			node.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


def color_grid(grid,visited):
	for row in grid:
		for node in row:
			size = node.total_rows
			if(visited[node.row * size + node.col] == True):
				node.make_color()

def draw_random_weights(grid,draw):
		for row in grid:
			for node in row:
				size = node.total_rows
				break
		for i in range(100):
			rd_row = random.randint(0,size-1)
			rd_col = random.randint(0,size-1)
			grid[rd_row][rd_col].make_wall()
			draw()


def reconstruct_path_aStar(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

def reconstruct_path_BFS(start_node, current_node, draw):
	start_node.make_start()
	while (current_node.previous != start_node):
		current_node = current_node.previous
		#print("current".format(current.get_pos()))
		current_node.make_path()
		draw()

def reconstruct_path_dijkstra(start,current, draw):
	start.make_start()
	while (current.previous != start):
		current = current.previous
		#print("current".format(current.get_pos()))
		current.make_path()
		draw()

