import pygame
import random

class Enemy:
    def __init__(self):
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 750)
        self.rect.y = -50

        self.speed = random.randint(2, 5)

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)