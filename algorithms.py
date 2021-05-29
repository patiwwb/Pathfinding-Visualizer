import pygame
import time
import queue
from node import *
from queue import PriorityQueue
from grid import *
from rendering import *

def AStarAlgorithm(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {node: float("inf") for row in grid for node in row}
	g_score[start] = 0
	f_score = {node: float("inf") for row in grid for node in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path_aStar(came_from, end, draw)
			end.make_end()
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False

def BFSAlgorithm(draw,grid,start_node,end_node):
	
	size = start_node.total_rows
	visited = [False] * size * size
	
	q = queue.Queue()
	q.put(start_node)
	myqueue = PriorityQueue()
	myqueue.put(start_node)
	
	visited[start_node.row * size + start_node.col] = True

	while not q.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = q.get()
		current.update_neighbors(grid)
		

		#time.sleep(1)
		color_grid(grid,visited)

		if current == end_node:
			reconstruct_path_BFS(start_node, end_node, draw)
			end_node.make_end()
			return True

		for neighbor in current.neighbors:
			if (visited[neighbor.row * size + neighbor.col]==False):
				q.put(neighbor)
				visited[neighbor.row * size + neighbor.col] = True
				neighbor.previous = current
				neighbor.make_open()
		current.mark()
		draw()

def DijkstraAlgorithm(draw,grid,start_node:Node,end_node:Node):
	visitedNodes = []
	came_from = {}
	start_node.distance = 0
	unvisitedNodes = GetAllNodes(grid)
	#print(len(unvisitedNodes))

	while (len(unvisitedNodes)!=0):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
			draw()
			unvisitedNodes.sort(key=get_distance)
			closest_node = unvisitedNodes.pop(0)
			#print(len(unvisitedNodes))
			if(closest_node.is_wall()): 
				print("wall") 
				continue
			if(closest_node.distance==INFINITY): return visitedNodes
			closest_node.visited = True
			closest_node.make_open()
			visitedNodes.append(closest_node)
			#print(closest_node.get_pos())
			if(closest_node==end_node): 
				reconstruct_path_dijkstra(start_node, end_node, draw)
				end_node.make_end()
				return True
			closest_node.update_unvisited_neighbors(grid)