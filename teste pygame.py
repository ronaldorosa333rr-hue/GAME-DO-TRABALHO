import pygame

pygame.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("TESTE")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 200, 0))
    pygame.display.update()

pygame.quit()