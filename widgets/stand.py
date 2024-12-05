from .widget import Widget
import pygame as pg
from modules.constants import (KNIFE_SOUND, STANDS_PATH)


class Stand(Widget):

    def __init__(self, x, y, text, screen, on_click=None):
        super().__init__(x, y, text, screen)
        
        # Imagen del jugador
        self.image = pg.image.load(STANDS_PATH)
        self.image = pg.transform.scale(self.image, (120, 240))

        # Rectangulo para ver si desp lo hago clickeable, sino quitar.
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.click_option_sfx = pg.mixer.Sound(KNIFE_SOUND)
        self.on_click = on_click

    def avatar_pressed(self):
        mouse_pos = pg.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1:
                pg.time.delay(300)
                self.click_option_sfx.set_volume(0.4)
                self.click_option_sfx.play()

    def draw(self):
        super().draw()

    def update(self):
        self.draw()
        self.avatar_pressed()
