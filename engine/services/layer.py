import pygame
import numpy as np

class Layer:
    def __init__(
            self,
            dimensions,
            render_priority=0,
            tick_priority=0,
            opacity_percent=100,
            surface=None,
            func=None,
    ):
        self.dimensions = dimensions
        self.surface = surface if surface else pygame.Surface(dimensions, pygame.HWSURFACE | pygame.SRCALPHA)
        self.visible = True
        self.ticking = True
        self.opacity_percent = opacity_percent
        self.offset = (0,0)
        self.func = func
        self.render_priority = render_priority
        self.tick_priority = tick_priority

    def tick(self):
        if self.func:
            self.func(self)
    
    def render(self):
        if self.opacity_percent >= 100:
            return self.surface
        
        surf = self.surface.copy()
        surf.set_alpha(int(self.opacity_percent * 2.55))
        return surf
    
    def loopscroll(self, dx, dy):
        surf = self.surface
        scroll_area_x = (abs(dx), surf.get_height())
        scroll_area_y = (surf.get_width(), abs(dy))
        if not dx == 0:
            tempx = pygame.Surface(scroll_area_x, pygame.SRCALPHA)
        if not dy == 0:
            tempy = pygame.Surface(scroll_area_y, pygame.SRCALPHA)

        top = 0
        left = 0
        right = surf.get_width()
        bottom = surf.get_height()

        if dx > 0: # image is moving right, copy rightmost chunk to left
            tempx.blit(surf, (0,0), ((right-dx, top), (dx, bottom)))
            surf.scroll(dx, 0)
            surf.blit(tempx, (left,top))
        elif dx < 0: # image is moving left, copy leftmost chunk to right
            tempx.blit(surf, (0,0), ((0, top), (-dx, bottom)))
            surf.scroll(dx, 0)
            surf.blit(tempx, (right+dx,top))
        
        if dy > 0: # image is moving down, copy bottom chunk to top
            tempy.blit(surf, (0,0), ((left, bottom-dy), (right, dy)))
            surf.scroll(0, dy)
            surf.blit(tempy, (left, top))
        elif dy < 0: # image is moving up, copy top chunk to bottom
            tempy.blit(surf, (0,0), ((left, 0), (right, -dy)))
            surf.scroll(0, dy)
            surf.blit(tempy, (left, bottom+dy))
        
        self.surface = surf
