from .widget import Widget
import pygame as pg
from modules.constants import (KNIFE_SOUND, GREEN_COLOR, NARUTO_FONT)


class Button(Widget):

    def __init__(self, x, y, text, screen, font_size=25, on_click=None, on_click_param=None, color=GREEN_COLOR):
        super().__init__(x, y, text, screen, font_size)
        self.font = pg.font.Font(NARUTO_FONT, self.font_size)
        self.image = self.font.render(self.text, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.click_option_sfx = pg.mixer.Sound(KNIFE_SOUND)
        self.on_click = on_click
        self.on_click_param = on_click_param

    def button_pressed(self):
        mouse_pos = pg.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1:
                pg.time.delay(300)
                self.on_click(self.on_click_param)
                self.click_option_sfx.set_volume(0.4)
                self.click_option_sfx.play()

    def draw(self):
        super().draw()

    def update(self):
        self.draw()
        self.button_pressed()
