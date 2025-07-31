import pygame as py

py.init()
py.font.init()
WIDTH, HEIGHT = 800, 600
FPS = 60

screen = py.display.set_mode((WIDTH, HEIGHT))
clock = py.time.Clock()
py.display.set_caption("Zombie Survival")

# === Colors ===
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (205, 0, 0)
BLACK = (0, 0, 0)