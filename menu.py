import pygame
from game import Game

class Menu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Shooter - Menu")
        self.font = pygame.font.SysFont("Arial", 30)
        self.clock = pygame.time.Clock()

    def run(self):
        running = True

        while running:
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            title = self.font.render("SPACE SHOOTER", True, (255, 255, 255))
            controls = self.font.render("ENTER - Iniciar | ESC - Sair", True, (200, 200, 200))

            self.screen.blit(title, (250, 200))
            self.screen.blit(controls, (180, 300))

            # 🔥 ISSO AQUI É O MAIS IMPORTANTE
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game = Game()
                        game.run()
                        return  # MUITO IMPORTANTE

                    elif event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()

        pygame.quit()