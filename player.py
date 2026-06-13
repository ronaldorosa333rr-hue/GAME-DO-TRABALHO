import pygame

class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))

        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

        self.speed = 6

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)