import pygame
from pathlib import Path

# from engine.services.input import EventMapper
 
cwd = Path.cwd()
test = cwd / "engine" / "assets" / "images" / "test.png"

image = pygame.image.load(test)
w,h = image.get_size()
image = pygame.transform.scale(image, (w*6,h*6))

pygame.init()
screen = pygame.display.set_mode((320*3,288*3))
clock = pygame.time.Clock()
running = True

while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    screen.blit(image, (0,0))

    clock.tick(60)

    pygame.display.flip()
pygame.quit()