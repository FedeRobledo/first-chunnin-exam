import pygame as pg
from .base_screen import Screen
from modules.constants import (SCREEN_DIMENSIONS)
from widgets import (
    TextTitle, Button
)


class MainMenu(Screen):
    def __init__(self, name, screen, x, y, active, level_num, music_path):
        super().__init__(name, screen, x, y, active, level_num, music_path)
        
        self.start_first_level = False
        
        # Actualizar la musica aca
        self.music_update()
        
        self.surface = pg.image.load('./assets/images/background.png').convert_alpha()
        self.surface = pg.transform.scale(self.surface, SCREEN_DIMENSIONS)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        
        self.menu_ppal_title = TextTitle(x=SCREEN_DIMENSIONS[0]//2, y=50, text='Examenes Chunnin', screen=screen, font_size=60)
        self.subtitle = TextTitle(x=SCREEN_DIMENSIONS[0]//2, y=SCREEN_DIMENSIONS[1]//2-100, text='MENU PRINCIPAL', screen=screen, font_size=40)
       
        self.button_start = Button(x=SCREEN_DIMENSIONS[0]//2, y=SCREEN_DIMENSIONS[1]//2, text='Nueva Partida', screen=screen, on_click=self.click_start, on_click_param='screen_enter_name')
       
        self.button_options = Button(x=SCREEN_DIMENSIONS[0]//2, y=SCREEN_DIMENSIONS[1]//2+75, text='OPCIONES', screen=screen, on_click=self.click_option, on_click_param='screen_options')
        # self.button_rankings = Button(x=SCREEN_DIMENSIONS[0]//2, y=SCREEN_DIMENSIONS[1]//2+150, text='RANKING', pantalla=pantalla, on_click=self.click_ranking, on_click_param='form_rankings')
        # self.button_exit = Button(x=SCREEN_DIMENSIONS[0]//2, y=SCREEN_DIMENSIONS[1]//2+225, texto='EXIT', pantalla=pantalla, on_click=self.click_exit)

        self.widget_list = [
            self.menu_ppal_title, self.subtitle, self.button_start, self.button_options,
            # , self.menu_ppal_title, self.button_exit, #self.button_level_select,
            # self.button_options, self.button_rankings, 
        ]
    
    def click_start(self, parametro):
        self.start_first_level = True
        self.set_active(parametro)
    
    def click_level_select(self, parametro):
        self.set_active(parametro)
    
    def click_option(self, parametro):
        self.set_active(parametro)
    
    def click_exit(self, parametro):
        self.set_active(parametro)
    
    def click_ranking(self, parametro):
        self.set_active(parametro)
    
    def draw(self):
        super().draw()
        for widget in self.widget_list:
            widget.draw()
    
    def update(self):
        self.draw()
        for widget in self.widget_list:
            widget.update()
