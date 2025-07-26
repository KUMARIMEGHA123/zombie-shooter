import pygame
import random
import config

class Zombie:
    def __init__(self):
        self.rect = pygame.Rect(random.choice([0, config.SCREEN_WIDTH]), random.randint(0, config.SCREEN_HEIGHT), 40, 40)
        self.color = (255, 0, 0)
        self.speed = 2

    def update(self, target_pos):
        dx, dy = target_pos[0] - self.rect.centerx, target_pos[1] - self.rect.centery
        dist = max((dx ** 2 + dy ** 2) ** 0.5, 1)
        self.rect.x += int(self.speed * dx / dist)
        self.rect.y += int(self.speed * dy / dist)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)