import pygame as pg
from .base_screen import Screen
from widgets import (
    Button, TextTitle, PlayerAvatar
)
from modules.constants import SCREEN_DIMENSIONS, BACKGROUND_PATH, PLAYER_INIT_POS


class Game(Screen):

    def __init__(self, name, screen, x, y, active, level_num, music_path):
        super().__init__(name, screen, x, y, active, level_num, music_path)

        self.surface = pg.image.load(BACKGROUND_PATH).convert_alpha()
        self.surface = pg.transform.scale(self.surface, SCREEN_DIMENSIONS)

        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        # Preguntas, despues se importarán de la funciones auxiliares que las cargan del JSON y se mostrarán aleatoriamente.
        self.text_option_1 = "Opcion 1"
        self.text_option_2 = "Opcion 2"
        self.text_ask = "¿Acaso soy una pregunta?"

        # Timer
        self.timer_1_Sec = pg.USEREVENT
        pg.time.set_timer(self.timer_1_Sec, 1000)
        self.limit_time = 15

        self.player_image = PlayerAvatar(
            x=PLAYER_INIT_POS[0],
            y=PLAYER_INIT_POS[1],
            text=None,
            screen=screen,
            on_click=self.on_click_avatar,
        )

        # Botón único para elegir la opción 1
        self.button_first_option = Button(
            x=300,
            y=700,
            text=self.text_option_1,
            screen=screen,
            on_click=self.choose_option_1,
        )

        # Botón único para elegir la opción 2
        self.button_second_option = Button(
            x=900,
            y=700,
            text=self.text_option_2,
            screen=screen,
            on_click=self.choose_option_2,
        )

        self.widgets_list = [
            self.button_first_option, self.button_second_option,
            self.player_image
        ]

    def choose_option_1(self,  parametro=None):
        print("Se elegió la opción 1")

    def choose_option_2(self,  parametro=None):
        print("Se elegió la opción 2")

    def on_click_avatar(self, parametro=None):
        print("Presione el avatar")

    def draw(self):
        super().draw()
        for widget in self.widgets_list:
            widget.draw()

    def update(self):
        super().draw()
        for widget in self.widgets_list:
            widget.update()
