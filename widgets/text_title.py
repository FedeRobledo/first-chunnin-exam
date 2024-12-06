import pygame as pg
from .widget import Widget
from modules.constants import (NARUTO_ORANGE_COLOR, NARUTO_FONT, GREEN_COLOR)

class TextTitle(Widget):
    
    def __init__(self, x, y, text, screen, font_size=50, color=NARUTO_ORANGE_COLOR, draw_box=False, box_color=(255, 255, 255), box_padding=10, border_radius=10):
        """
        widget de textos.
        """
        super().__init__(x, y, text, screen, font_size)
        self.font = pg.font.Font(NARUTO_FONT, self.font_size)
        self.image = self.font.render(self.text, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # Configuración del recuadro
        self.draw_box = draw_box
        self.box_color = box_color
        self.box_padding = box_padding
        self.border_radius = border_radius

    def draw(self):
        """Dibujo el texto, opcionalmente con un recuadro redondeado apra poder ordenarlo mejor."""
        if self.draw_box:
            # Dibujar el recuadro inglate me deja redibujar el cuadrado y hacer el padding
            box_rect = self.rect.inflate(self.box_padding * 2, self.box_padding * 2)
            pg.draw.rect(self.screen, self.box_color, box_rect, border_radius=self.border_radius)
        # Dibujar el texto
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Actualiza el widget."""
        self.draw()
