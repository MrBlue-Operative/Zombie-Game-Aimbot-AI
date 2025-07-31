import pygame as py
from config import GREEN, screen, RED
import math
import numpy as np
from environment import ENEMIES


def sigmoid(x):
    return 10 / (1 + np.exp(-x))

class Player:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.original_image = py.transform.scale(py.image.load('gun.png').convert_alpha(), (80, 110))
        self.image = self.original_image
        self.speed = 5
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.angle = 0
        self.bullets = []  
        self.bullet_speed = 30  # Speed of bullets
        self.shoot_delay = 260  # Delay between shots in milliseconds
        self.last_shot = 0  

        self.score = 0
        self.track = 0

    def update(self):

        #keys = py.key.get_pressed()        
        #mouse_x, mouse_y = py.mouse.get_pos()
        mouse_x, mouse_y = self.AI()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        self.angle = -math.degrees(math.atan2(rel_y, rel_x)) - 90

        if self.score < self.track:
            self.score += 2
        elif self.score > self.track:
            self.score -= 1

     
        current_time = py.time.get_ticks()
        if 1 and current_time - self.last_shot > self.shoot_delay:
            self.shoot()
            self.last_shot = current_time
            self.track -= 7

        self.update_bullets()
        self.draw()

    def shoot(self):
       
        mouse_x, mouse_y = self.AI()
        #mouse_x, mouse_y = py.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        distance = math.hypot(rel_x, rel_y)
        if distance != 0:
            direction = (rel_x / distance, rel_y / distance) 
          
            bullet = {
                'pos': [self.x, self.y],
                'vel': [direction[0] * self.bullet_speed, direction[1] * self.bullet_speed]
            }
            self.bullets.append(bullet)
            py.draw.line(screen, (250, 0, 0), (self.x, self.y), (mouse_x, mouse_y), 4)

    def update_bullets(self):
       
        screen_width, screen_height = screen.get_size()
        bullets_to_remove = []
        r = 6
        for i, bullet in enumerate(self.bullets):
           
            bullet['pos'][0] += bullet['vel'][0]
            bullet['pos'][1] += bullet['vel'][1]
        
            if (bullet['pos'][0] < 0 or bullet['pos'][0] > screen_width or
                bullet['pos'][1] < 0 or bullet['pos'][1] > screen_height):
                bullets_to_remove.append(i)
            # Draw bullet
            py.draw.circle(screen, RED, (int(bullet['pos'][0]), int(bullet['pos'][1])), r)
            for enemy in ENEMIES:
                if abs(int(bullet['pos'][0]) - enemy.x) < 20 and abs(int(bullet['pos'][1]) - enemy.y) < 20:
                    enemy.refresh()
                    self.bullets.remove(bullet)
                    self.track += 25
                    break

        for i in reversed(bullets_to_remove):
            self.bullets.pop(i)

    def draw(self):
        self.image = py.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.image, self.rect.topleft)
        # pos = py.mouse.get_pos()
        # py.draw.line(screen, (0, 200, 0), (self.x, self.y), pos, 1)
    
    def AI(self):
        mini = None
        curr = float('inf')
        for i in ENEMIES:
            if i.y < curr:
                curr = i.y
                mini = i
        return mini.x, mini.y - abs(mini.x/10 - self.x/10)