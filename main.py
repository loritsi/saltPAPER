import pygame
import sys
import random
from pathlib import Path

from engine.map.tilemap import TileMap
from engine.services.input import EventMapper


cwd = Path.cwd()
tilemap_path = cwd / "engine" / "assets" / "tilemaps" / "test.png"
tilemap = TileMap(tilemap_path, 16)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("eeeeee")

clock = pygame.time.Clock()
screen.fill((255,255,255))
def main():
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        tile = random.choice(tilemap.tiles).get_surface()
        tile = pygame.transform.scale(tile, (48,48))
        screen.blit(tile, (random.randint(0,SCREEN_WIDTH-16),random.randint(0,SCREEN_WIDTH-16)))

        pygame.display.flip()
        
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()