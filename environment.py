import pygame as py
from config import WIDTH, HEIGHT, screen, RED
import random as rn

class Enemy:
    def __init__(self, x, y, speed=3, big=False):
        self.dx = x
        self.dy = y
        self.width = 50 + big*25
        self.height = 50 + big*25
        self.x = self.dx + self.width//2
        self.y = self.dy + self.height//2
        self.image = py.transform.scale(py.transform.rotate(py.image.load('enemy.png').convert_alpha(), 90), (self.width, self.height))
        self.baseSpeed = speed
        self.speed = self.baseSpeed

    def draw(self):
        screen.blit(self.image, (self.dx, self.dy))
        self.y -= self.speed
        self.dy -= self.speed
        if self.dy < 150:
            self.speed = 0
        else:
            self.speed = self.baseSpeed
    
    def refresh(self):
        num = rn.randint(HEIGHT, HEIGHT + 100)
        self.dy = num
        self.y = self.dy + self.height//2
        num2 = rn.randint(10, WIDTH-60)
        self.dx = num2
        self.x = self.dx + self.width//2
    
ENEMIES = [Enemy(200, 400), Enemy(500, 600), Enemy(20, 800, 2), Enemy(500, 1600), Enemy(100, 900),
           Enemy(120, 1000, 2, True), Enemy(40, 900, 1, True), Enemy(40, 900, 1, True), Enemy(20, 800, 2)
        ]
