from colors import *

import pygame as pg

CELL_SIZE = 20

class Grid():
    def __init__(self, width, height):
        self.width_count = width // CELL_SIZE
        self.height_count = height // CELL_SIZE

        self.placing_mode = 0
        self.nodes = [[0 for x in range(self.width_count)] for y in range(self.height_count)]
        self.start = ()
        self.end = ()

    def is_empty(self):
        return not (self.start and self.end)

    def draw_grid(self, window, width, height):
        if self.start:
            pg.draw.rect(window, GREEN, (CELL_SIZE * self.start[0], CELL_SIZE * self.start[1], CELL_SIZE, CELL_SIZE))

        if self.end:
            pg.draw.rect(window, RED, (CELL_SIZE * self.end[0], CELL_SIZE * self.end[1], CELL_SIZE, CELL_SIZE))

        for y in range(len(self.nodes)):
            for x in range(len(self.nodes[y])):
                if self.nodes[y][x] != 0:
                    color = ()
                    if self.nodes[y][x] == 1:
                        color = BLACK
                    elif self.nodes[y][x] == 2:
                        color = YELLOW
                    elif self.nodes[y][x] == 3:
                        color = ORANGE
                    elif self.nodes[y][x] == 4:
                        color = PURPLE

                    pg.draw.rect(window, color, (CELL_SIZE * x, CELL_SIZE * y, CELL_SIZE, CELL_SIZE))

        for i in range(self.height_count):
            pg.draw.line(window, BLACK, (0, i * CELL_SIZE), (width, i * CELL_SIZE))

        for j in range(self.width_count):
            pg.draw.line(window, BLACK, (j * CELL_SIZE, 0), (j * CELL_SIZE, height))

        pg.display.update()

    def calculate_placing_mode(self):
        if not self.start:
            self.placing_mode = 0
        elif not self.end:
            self.placing_mode = 1
        elif self.start and self.end:
            self.placing_mode = 2

    def reset(self):
        self.placing_mode = 0
        self.start = ()
        self.end = ()

        for y in range(len(self.nodes)):
            for x in range(len(self.nodes[y])):
                self.nodes[y][x] = 0

    def place_cell(self, mouse_position):
        x = mouse_position[0] // CELL_SIZE
        y = mouse_position[1] // CELL_SIZE
        self.calculate_placing_mode()
        
        if self.placing_mode == 0:
            self.start = (x, y)
        elif self.placing_mode == 1:
            if (x, y) != self.start:
                self.end = (x, y)
        elif self.placing_mode == 2:
            if (x, y) != self.start and (x, y) != self.end and self.nodes[y][x] == 0:
                self.nodes[y][x] = 1

    def delete_cell(self, mouse_position):
        x = mouse_position[0] // CELL_SIZE
        y = mouse_position[1] // CELL_SIZE

        if (x, y) == self.start:
            self.start = ()
            
        if (x, y) == self.end:
            self.end = ()

        if self.nodes[y][x] == 1:
            self.nodes[y][x] = 0