from colors import *

import time

class Node:
    def __init__(self, position=(), parent=()):
        (self.x, self.y) = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

    def __lt__(self, other):
         return self.f < other.f

def calculate_heuristic(position1, position2):
    (x1, y1) = position1
    (x2, y2) = position2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(draw, grid, start, current):
    while current != start:
        current = current.parent
        if current != start:
            grid[current.y][current.x] = 3

        draw()

def astar(draw, grid, start_position, end_position):
    start = Node(start_position, None)
    end = Node(end_position, None)
    open = [start]
    closed = []
    
    while len(open) > 0:
        open.sort()
        current = open.pop(0)
        closed.append(current)
        
        if current == end:
            reconstruct_path(draw, grid, start, current)
            return True

        (x, y) = (current.x, current.y)
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for next in neighbors:
            if next[1] > (len(grid) - 1) or next[1] < 0 or next[0] > (len(grid[len(grid) - 1]) - 1) or next[0] < 0:
               continue

            if grid[next[1]][next[0]] == 1:
                continue
            
            neighbor = Node(next, current)
            
            if neighbor in closed:
                continue
            
            neighbor.g = current.g + 1
            neighbor.h = calculate_heuristic((neighbor.x, neighbor.y), (end.x, end.y))
            neighbor.f = neighbor.g + neighbor.h
            
            if neighbor not in open:
                open.append(neighbor)
                if neighbor != start and neighbor != end:
                    grid[neighbor.y][neighbor.x] = 2

        if current != start:
            grid[current.y][current.x] = 4
        
        draw()

    return False