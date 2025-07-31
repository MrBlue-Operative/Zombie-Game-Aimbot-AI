import pygame as py
import sys
from environment import ENEMIES
from player import Player
from config import screen, FPS, clock, WIDTH, HEIGHT, BLACK

players = [Player((WIDTH//2 - 30, 80))]
font = py.font.SysFont('Arial', 30)

# === Game Loop ===
while True:
    screen.fill((102, 85, 12))
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()

    # === Update ===
    for player in players:
        player.update()

    for i in ENEMIES:
        i.draw()

    # === Draw ===

    py.draw.line(screen, BLACK, (0, 150), (WIDTH, 150), 5)
    text = font.render(f"Score: {int(player.score)}", True, (0, 0, 0))
    screen.blit(text, (20, 20))
    py.display.flip()
    clock.tick(FPS)
