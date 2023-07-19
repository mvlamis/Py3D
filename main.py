import pygame as pg
import numpy
from obj import *
from camera import *
from projection import *

class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 800, 600
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_object()

    def create_object(self):
        self.camera = Camera(self, [0, 0, -10]) # start position
        self.projection = Projection(self)
        self.object = self.get_object_from_file('cube.obj')

    def get_object_from_file(self, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object3D(self, vertex, faces)

    def draw(self):
        self.screen.fill(pg.Color('black'))
        self.object.draw()
        # display position coords in text
        posText = 'x: {:.2f} y: {:.2f} z: {:.2f}'.format(*self.camera.position)
        text = pg.font.SysFont('Arial', 20).render(posText, True, pg.Color('white'))
        self.screen.blit(text, (10, 10))

        # display camera forward, up, right vectors in text
        forwardText = 'forward: {:.2f} {:.2f} {:.2f}'.format(*self.camera.forward)
        upText = 'up: {:.2f} {:.2f} {:.2f}'.format(*self.camera.up)
        rightText = 'right: {:.2f} {:.2f} {:.2f}'.format(*self.camera.right)
        text = pg.font.SysFont('Arial', 20).render(forwardText, True, pg.Color('white'))
        self.screen.blit(text, (10, 30))
        text = pg.font.SysFont('Arial', 20).render(upText, True, pg.Color('white'))
        self.screen.blit(text, (10, 50))
        text = pg.font.SysFont('Arial', 20).render(rightText, True, pg.Color('white'))
        self.screen.blit(text, (10, 70))

        # button to reset camera position and rotation
        resetText = 'reset camera'
        text = pg.font.SysFont('Arial', 20).render(resetText, True, pg.Color('white'))
        textRect = text.get_rect(topleft=(650, 10))
        pg.draw.rect(self.screen, pg.Color('blue'), textRect, 1)
        self.screen.blit(text, (650, 10))
        if textRect.collidepoint(pg.mouse.get_pos()):
            if pg.mouse.get_pressed()[0]:
                self.camera = Camera(self, [0, 0, -10])


        


    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

if __name__ == '__main__':
    app = SoftwareRender()
    app.run()
            