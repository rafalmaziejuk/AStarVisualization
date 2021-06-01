from colors import *

import pygame as pg

class Grid():
    def __init__(self, width, height):
        self.cell_size = 20
        self.width_count = width // self.cell_size
        self.height_count = height // self.cell_size

    def draw_grid(self, window, width, height):
        for i in range(self.height_count):
            pg.draw.line(window, BLACK, (0, i * self.cell_size), (width, i * self.cell_size))

        for j in range(self.width_count):
            pg.draw.line(window, BLACK, (j * self.cell_size, 0), (j * self.cell_size, height))