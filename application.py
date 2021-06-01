import pygame as pg
import sys
import math

class Application():
    
    def __init__(self, window_title="A* Visualization", width=1280, height=720):
        self.width = width
        self.height = height
        self.is_running = True

        pg.init()
        self.window = pg.display.set_mode((width, height))
        pg.display.set_caption(window_title)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.is_running = False

    def draw(self):
        self.window.fill((255, 255, 255))

        pg.display.update()

    def run(self):
        while self.is_running:
            self.draw()
            self.handle_events()

        pg.quit()
        sys.exit()