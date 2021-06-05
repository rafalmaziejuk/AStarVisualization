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

def calculate_heuristic(current, goal):
    """Manhattan distance heuristic (4 directions of movement)."""
    (x1, y1) = current
    (x2, y2) = goal

    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(draw, grid, start, current):
    while current != start:
        current = current.parent
        
        # the shortest path nodes (PURPLE)
        if current != start:
            grid[current.y][current.x] = 4

        draw()

def astar(draw, grid, start_position, end_position):
    start = Node(start_position, None)
    end = Node(end_position, None)
    open = [start] # set of unexplored nodes adjacent to explored nodes
    closed = [] # set of explored nodes
    
    while len(open) > 0:
        open.sort()
        current = open.pop(0) # get node with the lowest f value
        closed.append(current)
        
        if current == end:
            reconstruct_path(draw, grid, start, current)
            return True

        (x, y) = (current.x, current.y)
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

        for next in neighbors:
            # check if node is within search space bounds
            if next[1] > (len(grid) - 1) or next[1] < 0 or next[0] > (len(grid[len(grid) - 1]) - 1) or next[0] < 0:
               continue

            # check if node is a wall
            if grid[next[1]][next[0]] == 1:
                continue
            
            neighbor = Node(next, current)
            
            # if node has been already explored (ORANGE) - skip
            if neighbor in closed:
                grid[current.y][current.x] = 3
                continue
            
            neighbor.g = current.g + 1 # weight of every edge is 1
            neighbor.h = calculate_heuristic((neighbor.x, neighbor.y), (end.x, end.y))
            neighbor.f = neighbor.g + neighbor.h
            
            # add current node's neighbors to the open set
            if neighbor not in open:
                open.append(neighbor)

                # nodes in open set (YELLOW)
                if neighbor != end:
                    grid[neighbor.y][neighbor.x] = 2

        draw()

    return False