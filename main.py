import pygame
import sys
import random
from pathlib import Path

from engine.map.tilemap import TileMap
from engine.services.input import EventMapper
from engine.services.display import DisplayService
from engine.services.layer import Layer


cwd = Path.cwd()
tilemap_path = cwd / "engine" / "assets" / "tilemaps" / "test.png"
tilemap = TileMap(tilemap_path, 16)

dimensions = 768,624
FPS = 120

display = DisplayService(
    dimensions=dimensions,
    caption="eeeeee",
    vsync=False
)

TILE_SIZE = 48

def fill_layer_with_tiles(layer, tile_size=TILE_SIZE):
    """Fill a layer with a random tile pattern."""
    tiles_x = (layer.dimensions[0] // tile_size) + 2 
    tiles_y = (layer.dimensions[1] // tile_size) + 2
    
    for y in range(tiles_y):
        for x in range(tiles_x):
            tile = random.choice(tilemap.tiles).get_surface()
            tile = pygame.transform.scale(tile, (tile_size, tile_size))
            layer.surface.blit(tile, (x * tile_size, y * tile_size))

tile_layer = Layer(
    dimensions=dimensions,
    render_priority=0
)

tile_layer2 = Layer(
    dimensions=dimensions,
    render_priority=1,
    opacity_percent=50
)

fill_layer_with_tiles(tile_layer)
fill_layer_with_tiles(tile_layer2)

display.add_layer(tile_layer)
display.add_layer(tile_layer2)
event = EventMapper()
mouse = pygame.mouse

def main():
    while display.running:
        tile_layer.loopscroll(1, 1)
        tile_layer2.loopscroll(-1, -1)

        display.tick()
        display.clock.tick(FPS)
        pygame.display.set_caption(f"{display.caption} - {display.clock.get_fps():.0f}fps (limit {FPS})")
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()