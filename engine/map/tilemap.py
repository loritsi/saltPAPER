import pygame
from pathlib import Path

class TileType():
    def __init__(self, id, size):
        self.surface = pygame.surface.Surface((16,16))

    def get_surface(self) -> pygame.surface.Surface:
        return self.surface

class TileMap():
    def __init__(self, path, size):
        self.path = path
        self.base = pygame.image.load(path)
        self.size = size
        self.tiles = []
        self.load_tilesheet()

    def load_tilesheet(self, path=None):
        if path == None:
            path = self.path
        width,height = self.base.get_size()
        if not width == height:
            raise ValueError("tilesheets should be exactly square")
        if not width % self.size == 0:
            raise ValueError("tilesheet size is not a multiple of tile size")
        tilewidth = width // self.size
        tilestotal = tilewidth * tilewidth

        for i in range(tilestotal):
            tile = TileType(i, self.size)
            offsetx = (i % tilewidth) * self.size
            offsety = (i // tilewidth) * self.size
            tile.surface.blit(self.base, (0, 0), (offsetx, offsety, self.size, self.size))
            self.tiles.append(tile)
    
    def __len__(self):
        return len(self.tiles)

if __name__ == "__main__":
    cwd = Path.cwd()
    test_image = cwd / "engine" / "assets" / "images" / "test.png"
    tilemap = TileMap(test_image, 16)
    print(len(tilemap))