from colors import WHITE
from grid import Grid

import pygame as pg
import sys
import math

class Application():
    
    def __init__(self, window_title="A* Visualization", width=1280, height=720, FPS=60):
        pg.init()
        self.window = pg.display.set_mode((width, height))
        pg.display.set_caption(window_title)
        self.width = width
        self.height = height
        self.is_running = True
        self.show_fps = True
        self.font = pg.font.Font(None, 25)
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

                if event.key == pg.K_f:
                    self.show_fps = not self.show_fps

                if event.key == pg.K_r:
                    self.grid.reset()

    def draw(self):
        self.window.fill(WHITE)

        if self.show_fps:
            fps = str(int(self.clock.get_fps()))
            fps_text = self.font.render(fps, True, pg.Color('black'))
            self.window.blit(fps_text, (10, 10))

        self.grid.draw_grid(self.window, self.width, self.height)

        pg.display.update()
        self.clock.tick(self.FPS)

    def run(self):
        while self.is_running:
            self.draw()
            self.handle_events()

        pg.quit()
        sys.exit()