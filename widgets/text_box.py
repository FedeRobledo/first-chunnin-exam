import pygame as pg
from .widget import Widget
from modules.constants import GREEN_COLOR, KNIFE_SOUND, NARUTO_FONT

class TextBox(Widget):
    
    def __init__(self, x, y, text, screen, font_size=40, on_click=None, on_click_param=None):
        super().__init__(x, y, text, screen, font_size)
        self.font = pg.font.SysFont(None, self.font_size)
        self.image = self.font.render(self.text, True, GREEN_COLOR)
        
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.click_option_sfx = pg.mixer.Sound(KNIFE_SOUND)
        self.click_option_sfx.set_volume(0.3)
        
        self.on_click = on_click
        self.on_click_param = on_click_param
        
        self.write_on = True
        self.writing = ''
        self.image_writing = self.font.render(self.writing, True, GREEN_COLOR)
        self.rect_writing = self.image_writing.get_rect()
        self.rect_writing.center = (x, y)
    
    def write_on_box(self, event_list: list):
        for event in event_list:
            if event.type == pg.KEYDOWN and self.write_on:
                if event.key == pg.K_BACKSPACE:
                    self.writing = self.writing[:-1]
                else:
                    self.writing += event.unicode
                self.click_option_sfx.play()
    
    def draw(self):
        super().draw()
        self.image.blit(self.screen, (self.rect_writing.x, self.rect_writing.y))
    
    def update(self, event_list: list):
        self.draw()
        self.write_on_box(event_list)