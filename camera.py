import pygame as pg
import numpy
from matrix_functions import *

class Camera:
    def __init__(self, render, position):
        self.render = render
        self.position = np.array([*position, 1.0])
        self.forward = np.array([0, 0, 1, 1])
        self.up = np.array([0, 1, 0, 1])
        self.right = np.array([1, 0, 0, 1])
        self.hFov = math.pi / 3
        self.vFov = self.hFov * self.render.HEIGHT / self.render.WIDTH
        self.nearPlane = 0.1 
        self.farPlane =  100
        self.speed = 0.02
        self.sensitivity = 0.01

    def control(self):
        key = pg.key.get_pressed()
        if key[pg.K_a]:
            self.position -= self.right * self.speed

        if key[pg.K_d]:
            self.position += self.right * self.speed

        if key[pg.K_w]:
            self.position += self.forward * self.speed

        if key[pg.K_s]:
            self.position -= self.forward * self.speed

        if key[pg.K_SPACE]:
            self.position += self.up * self.speed

        if key[pg.K_LSHIFT]:
            self.position -= self.up * self.speed

        if key[pg.K_LEFT]:
            self.camera_yaw(-self.sensitivity)

        if key[pg.K_RIGHT]:
            self.camera_yaw(self.sensitivity)

        if key[pg.K_UP]:
            self.camera_pitch(-self.sensitivity)

        if key[pg.K_DOWN]:
            self.camera_pitch(self.sensitivity)


    def camera_yaw(self, angle):
        rotate = rotate_y(angle)
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate

    def camera_pitch(self, angle):
        rotate = rotate_x(angle)
        self.forward = self.forward @ rotate
        self.right = self.right @ rotate
        self.up = self.up @ rotate

    def translate_matrix(self):
        x, y, z, w = self.position
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]
        ])
    
    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        ux, uy, uz, w = self.up
        fx, fy, fz, w = self.forward

        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]
        ])
    
    def camera_matrix(self):
        return self.rotate_matrix() @ self.translate_matrix()