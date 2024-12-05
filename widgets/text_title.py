import pygame as pg
from .widget import Widget
from modules.constants import (NARUTO_ORANGE_COLOR, NARUTO_FONT, GREEN_COLOR)


class TextTitle(Widget):
    
    def __init__(self, x, y, text, screen, font_size=50, color=NARUTO_ORANGE_COLOR):
        super().__init__(x, y, text, screen, font_size)
        self.font = pg.font.Font(NARUTO_FONT, self.font_size)
        self.image = self.font.render(self.text, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
    def draw(self):
        super().draw()
    
    def update(self):
        self.draw()