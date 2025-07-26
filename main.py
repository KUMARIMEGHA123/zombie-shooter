import pygame
from player import Player
from zombie import Zombie
from bullet import Bullet
import random
import config

pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
pygame.display.set_caption("Zombie Shooter")
clock = pygame.time.Clock()

player = Player()
zombies = []
bullets = []
spawn_timer = 0
score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            bullet = player.shoot(pygame.mouse.get_pos())
            if bullet:
                bullets.append(bullet)

    player.update(pygame.key.get_pressed(), pygame.mouse.get_pos())

    spawn_timer += 1
    if spawn_timer > 60:
        zombies.append(Zombie())
        spawn_timer = 0

    for zombie in zombies[:]:
        zombie.update(player.rect.center)
        if zombie.rect.colliderect(player.rect):
            player.health -= 1
            zombies.remove(zombie)
        for bullet in bullets[:]:
            if zombie.rect.colliderect(bullet.rect):
                bullets.remove(bullet)
                zombies.remove(zombie)
                score += 1
                break

    for bullet in bullets:
        bullet.update()

    # Draw everything
    player.draw(screen)
    for zombie in zombies:
        zombie.draw(screen)
    for bullet in bullets:
        bullet.draw(screen)

    # Health and Score
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, player.health * 2, 20))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 40))

    pygame.display.flip()
    clock.tick(config.FPS)

pygame.quit()