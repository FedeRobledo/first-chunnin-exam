import pygame as pg
from .base_screen import Screen
from widgets import (
    Button, TextTitle, PlayerAvatar, Text
)
from modules.constants import (
    SCREEN_DIMENSIONS, BACKGROUND_PATH, PLAYER_INIT_POS, GREEN_COLOR, BLUE_COLOR, RED_COLOR)
from modules.auxiliar import (import_and_return_ask)


class Game(Screen):

    def __init__(self, name, screen, x, y, active, level_num, music_path):
        super().__init__(name, screen, x, y, active, level_num, music_path)

        self.surface = pg.image.load(BACKGROUND_PATH).convert_alpha()
        self.surface = pg.transform.scale(self.surface, SCREEN_DIMENSIONS)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        self.game_questions = import_and_return_ask()

        # Preguntas, despues se importarán de la funciones auxiliares que las cargan del JSON y se mostrarán aleatoriamente.

        self.actual_question = 0
        self.finish_question = len(self.game_questions)
        print(self.game_questions[0]['respuestas'][0]['texto'])

        self.text_option_1 = self.game_questions[0]['respuestas'][0]['texto']
        self.text_option_2 = self.game_questions[0]['respuestas'][1]['texto']
        # self.text_ask = self.game_questions[self.actual_question.pregunta]
        self.text_ask = self.game_questions[self.actual_question]['pregunta']
        print(self.game_questions[0]['pregunta'])


        # Timer HACERLO WIDGET
        self.timer_1_Sec = pg.USEREVENT
        pg.time.set_timer(self.timer_1_Sec, 1000)
        self.limit_time = 15

        # Puntaje
        self.score = 0

        # WIDGETS
        self.player_image = PlayerAvatar(
            x=PLAYER_INIT_POS[0],
            y=PLAYER_INIT_POS[1],
            text=None,
            screen=screen,
            on_click=self.on_click_avatar,
        )

        # Puntaje
        self.subtitle_score = TextTitle(
            x=SCREEN_DIMENSIONS[0] - 100,
            y=40,
            text=f"puntaje: {self.score}",
            screen=screen,
            font_size=30
        )

        # Pregunta
        self.ask = TextTitle(
            x=600,
            y=650,
            text=self.text_ask,
            screen=screen,
            font_size=20,
            color=GREEN_COLOR
        )

        # Botón único para elegir la opción 1
        self.button_first_option = Button(
            x=400,
            y=750,
            text=self.text_option_1,
            screen=screen,
            font_size=20,
            on_click=self.choose_option_1,
            color=BLUE_COLOR
        )

        # Botón único para elegir la opción 2
        self.button_second_option = Button(
            x=800,
            y=750,
            text=self.text_option_2,
            screen=screen,
            font_size=20,
            on_click=self.choose_option_2,
            color=RED_COLOR
        )

        self.widgets_list = [
            self.button_first_option, self.button_second_option,
            self.player_image, self.ask, self.subtitle_score
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
