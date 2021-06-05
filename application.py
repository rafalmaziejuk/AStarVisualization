from colors import WHITE
from grid import Grid
from astar import astar

import pygame as pg
import sys

class Application():
    
    def __init__(self, window_title="A* Visualization", width=1280, height=720, FPS=60):
        pg.init()
        self.window = pg.display.set_mode((width, height))
        pg.display.set_caption(window_title)
        self.width = width
        self.height = height
        self.is_running = True
        self.clock = pg.time.Clock()
        self.FPS = FPS
        self.grid = Grid(width, height)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.grid.place_cell(event.pos)

                if event.button == 3:
                    self.grid.delete_cell(event.pos)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.is_running = False

                if event.key == pg.K_SPACE:
                    if not self.grid.is_empty():
                        astar(lambda: self.grid.draw_grid(self.window, self.width, self.height), self.grid.nodes, self.grid.start, self.grid.end)

                if event.key == pg.K_r:
                    self.grid.reset()

    def draw(self):
        self.window.fill(WHITE)
        self.grid.draw_grid(self.window, self.width, self.height)
        self.clock.tick(self.FPS)

    def run(self):
        while self.is_running:
            self.draw()
            self.handle_events()

        pg.quit()
        sys.exit()