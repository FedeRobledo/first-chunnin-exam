import pygame as pg
from .base_screen import Screen
from widgets import (Button, TextBox, TextTitle)
from modules.constants import SCREEN_DIMENSIONS, BACKGROUND_PATH
from game.player import Player
from modules.auxiliar import save_score

class EnterNameScreen(Screen):
    '''
    This class represents the enter name screen  
    '''
    def __init__(self, name: str, screen: object, x: int, y: int, active: bool, level_num: int, music_path: str, score: int) -> None:
        super().__init__(name, screen, x, y, active, level_num, music_path)

        self.surface = pg.image.load(BACKGROUND_PATH).convert_alpha()
        self.surface = pg.transform.scale(self.surface, SCREEN_DIMENSIONS)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.player = Player.get_player()

        self.music_update()
        self.confirm_name = False
                   
        self.title = TextTitle(x=SCREEN_DIMENSIONS[0]//2, y=50, text="Examenes Chunnin", screen=screen, font_size=60)
        self.subtitle = TextTitle(x=SCREEN_DIMENSIONS[0]//2, y=SCREEN_DIMENSIONS[1]//2-90, text="ingrese su nombre:", screen=screen, font_size=50)
         
        self.text_box = TextBox(x=SCREEN_DIMENSIONS[0]//2, y=SCREEN_DIMENSIONS[1]//2 + 40, text="_________________", screen=screen)
        self.button_confirm_name = Button(x=SCREEN_DIMENSIONS[0]//2, y=SCREEN_DIMENSIONS[1]//2+100, text="Confirmar", screen=screen, on_click=self.click_confirm_name)
        
        self.widget_list = [
            self.title,
            self.subtitle,
            self.button_confirm_name
        ]

        
    def click_confirm_name(self, parametro:str) -> None:
        '''
        Sets confirm name flag as True
        Arguments: parametro (str)
        Returns: None
        '''
        self.confirm_name = True
        self.player.set_name(self.writing_text.text)
        print(f'Su nombre: {self.player.get_name()} - {self.player.get_total_score()} puntos')
        # save_score(self.player)
        # self.set_active('ranking')
        self.set_active('game_screen')

        
    def draw(self) -> None:
        '''
        Merges the elements of the screen with the one from the main screen
        Arguments: None
        Returns: None
        '''
        super().draw()
        for widget in self.widget_list:    
            widget.draw()
        self.text_box.draw()
        self.writing_text = TextTitle(x=SCREEN_DIMENSIONS[0]//2, y=SCREEN_DIMENSIONS[1]//2+30, text=f"{self.text_box.writing.upper()}", screen=self.screen, font_size=30)
        self.writing_text.draw()

    def update(self, event_list) -> None:
        '''
        Executes the methods that need update 
        Arguments: event list (list)
        Returns: None
        '''
        super().draw()
        self.text_box.update(event_list)
        for widget in self.widget_list:
            widget.update()
         
