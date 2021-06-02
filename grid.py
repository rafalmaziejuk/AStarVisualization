from colors import *

import pygame as pg

class Grid():
    def __init__(self, width, height):
        self.cell_size = 20
        self.width_count = width // self.cell_size
        self.height_count = height // self.cell_size

        self.placing_mode = 0
        self.start = ()
        self.end = ()
        self.wall = []

    def draw_grid(self, window, width, height):
        for i in range(self.height_count):
            pg.draw.line(window, BLACK, (0, i * self.cell_size), (width, i * self.cell_size))

        for j in range(self.width_count):
            pg.draw.line(window, BLACK, (j * self.cell_size, 0), (j * self.cell_size, height))

        if self.start:
            pg.draw.rect(window, GREEN, (self.cell_size * self.start[0], self.cell_size * self.start[1], self.cell_size, self.cell_size))

        if self.end:
            pg.draw.rect(window, RED, (self.cell_size * self.end[0], self.cell_size * self.end[1], self.cell_size, self.cell_size))

        if self.wall:
            for cell in self.wall:
                pg.draw.rect(window, BLACK, (self.cell_size * cell[0], self.cell_size * cell[1], self.cell_size, self.cell_size))

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
        self.wall.clear()

    def place_cell(self, mouse_position):
        x = mouse_position[0] // self.cell_size
        y = mouse_position[1] // self.cell_size
        self.calculate_placing_mode()
        
        if self.placing_mode == 0:
            self.start = (x, y)
        elif self.placing_mode == 1:
            if (x, y) != self.start:
                self.end = (x, y)
        elif self.placing_mode == 2:
            if (x, y) != self.start and (x, y) != self.end and (x, y) not in self.wall:
                self.wall.append((x, y))

    def delete_cell(self, mouse_position):
        x = mouse_position[0] // self.cell_size
        y = mouse_position[1] // self.cell_size

        if (x, y) == self.start:
            self.start = ()
            
        if (x, y) == self.end:
            self.end = ()

        if (x, y) in self.wall:
            self.wall.remove((x, y))