import pygame
import random
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Shooter")
        self.clock = pygame.time.Clock()

        self.player = Player()
        self.enemies = []
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 25)

    def run(self):
        running = True

        while running:
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.update(keys)
            self.player.draw(self.screen)

            if random.randint(1, 60) == 1:
                self.enemies.append(Enemy())

            for enemy in self.enemies[:]:
                enemy.update()
                enemy.draw(self.screen)

                if enemy.rect.colliderect(self.player.rect):
                    running = False  # derrota

                if enemy.rect.y > 600:
                    self.enemies.remove(enemy)
                    self.score += 1

            if self.score >= 20:
                running = False  # vitória

            text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(text, (10, 10))

            pygame.display.update()

        pygame.quit()