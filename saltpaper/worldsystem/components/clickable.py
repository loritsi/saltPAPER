from typing import TYPE_CHECKING

import pygame.mouse as mouse
from saltpaper.services.event import Criteria
from saltpaper.functions.vectortools import VectorTools

if TYPE_CHECKING:
    from saltpaper import Event, Layer

class Clickable:
    """format bounds as x, y, width, height"""
    def __init__(
            self,
            event:'Event',
            layer:'Layer',
            bounds:list[int,int,int,int]
    ):
        self.event = event
        self.layer = layer
        self.bounds = bounds

        main_criteria = Criteria.make_combined_criteria(event.criteria, self.is_mouse_inside)
        event.criteria = main_criteria

    def is_mouse_inside(self, f):
        rel_pos = self.layer.relative_coords(mouse.get_pos())
        return VectorTools.is_point_inside(rel_pos, *self.bounds)
