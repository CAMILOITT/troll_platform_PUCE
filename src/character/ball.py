import pygame

from ..const.game import SCREEN


class Ball:
    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self.color = color

    def drawing(self):
        pygame.draw.circle(
            pygame.display.get_surface(),
            pygame.Color(self.color),
            pygame.Vector2(SCREEN.get_width() / 2, SCREEN.get_height() / 2),
            int(self.radius),
        )
