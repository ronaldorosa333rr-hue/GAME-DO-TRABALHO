import pygame
from game import Game

class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Shooter - Menu")
        self.font = pygame.font.SysFont("Arial", 28)

    def run(self):
        running = True

        while running:
            self.screen.fill((0, 0, 0))

            title = self.font.render("SPACE SHOOTER", True, (255, 255, 255))
            controls = self.font.render("ENTER - Iniciar | SETAS - Mover | ESC - Sair", True, (200, 200, 200))

            self.screen.blit(title, (250, 200))
            self.screen.blit(controls, (80, 300))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game = Game()
                        game.run()

                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()

        pygame.quit()