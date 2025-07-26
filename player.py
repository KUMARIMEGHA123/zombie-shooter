import pygame
import config
from bullet import Bullet

class Player:
    def __init__(self):
        self.rect = pygame.Rect(400, 300, 50, 50)
        self.color = (0, 255, 0)
        self.speed = 5
        self.health = 100

    def update(self, keys, mouse_pos):
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

    def shoot(self, target):
        return Bullet(self.rect.center, target)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)