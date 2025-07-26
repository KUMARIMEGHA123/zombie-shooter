import pygame
import config

class Bullet:
    def __init__(self, pos, target):
        self.rect = pygame.Rect(pos[0], pos[1], 5, 5)
        self.color = (255, 255, 0)
        self.speed = 10
        dx, dy = target[0] - pos[0], target[1] - pos[1]
        dist = max((dx ** 2 + dy ** 2) ** 0.5, 1)
        self.velocity = (self.speed * dx / dist, self.speed * dy / dist)

    def update(self):
        self.rect.x += int(self.velocity[0])
        self.rect.y += int(self.velocity[1])

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)