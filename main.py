import pygame
import math
import time
from node import *
from rendering import draw_grid, draw, color_grid, draw_random_weights
from rendering import reconstruct_path_aStar, reconstruct_path_BFS, reconstruct_path_dijkstra
from grid import h, make_grid, get_clicked_pos, get_distance, GetAllNodes
from algorithms import *

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Path Finding Algorithms Comparator")

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_wall()

            elif pygame.mouse.get_pressed()[2]: # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and start and end:
                    start_time = time.time()
                    algo = DijkstraAlgorithm(lambda: draw(win, grid, ROWS, width),grid,start,end)
                    #print(algo)
                   
                    end_time = time.time()
                    print("Dijkstra :{} s".format(end_time - start_time))
                
                if event.key == pygame.K_b and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    start_time = time.time()
                    algo = BFSAlgorithm(lambda: draw(win, grid, ROWS, width),grid,start,end)
                    #print(algo)
                   
                    end_time = time.time()
                    print("BFS :{} s".format(end_time - start_time))

                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbors(grid)
                    start_time = time.time()
                    AStarAlgorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    end_time = time.time()
                    print("A* :{} s".format(end_time - start_time))
                if event.key == pygame.K_d:
                    draw_random_weights(grid,(lambda: draw(win, grid, ROWS, width)))
                
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()

main(WIN, WIDTH)



