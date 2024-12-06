import pygame as pg
from .widget import Widget
from modules.constants import (NARUTO_ORANGE_COLOR, NARUTO_FONT)


class Timer(Widget):
    
    def __init__(self, x, y, screen, font_size=50, color=NARUTO_ORANGE_COLOR, limit_time=15):
        """
        Timer para la pantalla del juego que decrementa cada 1 segundo.
        """
        super().__init__(x, y, "", screen, font_size)
        self.font = pg.font.Font(NARUTO_FONT, self.font_size)
        self.color = color
        self.time_left = limit_time
        self.update_text()

    def update_text(self):
        """Actualiza el texto del temporizador.
        """
        self.text = f"Tiempo: {self.time_left}"
        self.image = self.font.render(self.text, True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
    
    def draw(self):
        """Dibuja el temporizador en la pantalla."""
        self.screen.blit(self.image, self.rect)

    def decrement_time(self):
        """Disminuye el tiempo restante y actualiza el texto."""
        if self.time_left > 0:
            self.time_left -= 1
            self.update_text()

    def update(self):
        """Dibuja el temporizador en cada iteración del bucle de juego."""
        self.draw()
