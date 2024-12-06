import pygame as pg
from .base_screen import Screen
from widgets import (
    Button, TextTitle, PlayerAvatar, Text, Stand, Timer
)
from modules.constants import (
    SCREEN_DIMENSIONS, BACKGROUND_PATH, PLAYER_INIT_POS, GREEN_COLOR, BLUE_COLOR, RED_COLOR)
from modules.auxiliar import (import_and_return_asks)
from game.player import Player


class Game(Screen):

    def __init__(self, name, screen, x, y, active, level_num, music_path):
        super().__init__(name, screen, x, y, active, level_num, music_path)

        self.surface = pg.image.load(BACKGROUND_PATH).convert_alpha()
        self.surface = pg.transform.scale(self.surface, SCREEN_DIMENSIONS)
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.player = Player.get_player()

        self.game_questions = import_and_return_asks()

        # Preguntas, despues se importarán de la funciones auxiliares que las cargan del JSON y se mostrarán aleatoriamente.

        print(self.player.get_ask_idx())
        self.actual_question = self.player.get_ask_idx()
        
        self.finish_question = len(self.game_questions)
        self.actual_question_data = self.game_questions[self.actual_question]
        self.update_actual_ask()

        # Puntaje
        self.score = 0

        # WIDGETS

        # Buscar una mejor imagen, esta tiene errores.
        self.stand = Stand(
            x=SCREEN_DIMENSIONS[0]//2,
            y=350,
            text=None,
            screen=screen
        )

        # Avatar
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
            font_size=30,
        )
    
        self.get_widgets()

        self.widgets_list = [
            self.button_first_option, self.button_second_option,
            self.player_image, self.ask_text_widget, self.subtitle_score, self.stand
        ]

    def choose_option_1(self, parametro):
        es_correcta = parametro['esCorrecta']

        if not es_correcta:
            print("TERMINO EL JUEGO, ES INCORRECTA")
        else:
            if self.actual_question != self.finish_question:
                self.actual_question += 1
                self.actual_question_data = self.game_questions[self.actual_question]
                self.update_actual_ask()
                # self.player.set_ask_idx(self.actual_question)
                # print(self.player.get_ask_idx())
                self.get_widgets()
                self.draw()
                # Actualizar la vista
            else:
                print("TERMINO EL JUEGO, GANASTE")

        print(f"Se elegió la opción 1 y la opcion es {"CORRRECTA" if es_correcta else "INCORRECTA"}")

    def choose_option_2(self, parametro):
        es_correcta = parametro['esCorrecta']

        if not es_correcta:
            print("TERMINO EL JUEGO, ES INCORRECTA")
        else:
            if self.actual_question != self.finish_question:
                self.actual_question += 1
                self.actual_question_data = self.game_questions[self.actual_question]
                self.update_actual_ask()
                # self.player.set_ask_idx(self.actual_question)
                # print(self.player.get_ask_idx())
                self.get_widgets()
                self.draw()
                # Actualizar la vista
            else:
                print("TERMINO EL JUEGO, GANASTE")

        print(f"Se elegió la opción 2 y la opcion es {"CORRRECTA" if es_correcta else "INCORRECTA"}")

    def on_click_avatar(self, parametro=None):
        print("Presione el avatar")

    def update_actual_ask(self):
        self.option_1 = self.actual_question_data['respuestas'][0]
        self.option_2 = self.actual_question_data['respuestas'][1]
        self.text_option_1 = self.actual_question_data['respuestas'][0]['texto']
        self.text_option_2 = self.actual_question_data['respuestas'][1]['texto']
        self.text_ask = self.actual_question_data['pregunta']

    def get_widgets(self):

        # Pregunta
        self.ask_text_widget = TextTitle(
            x=600,
            y=650,
            text=self.text_ask,
            screen=self.screen,
            font_size=20,
            draw_box=True
        )

        # Botón único para elegir la opción 1
        self.button_first_option = Button(
            x=400,
            y=750,
            text=self.text_option_1,
            screen=self.screen,
            font_size=20,
            on_click=self.choose_option_1,
            on_click_param=self.option_1,
            color=BLUE_COLOR
        )

        # Botón único para elegir la opción 2
        self.button_second_option = Button(
            x=800,
            y=750,
            text=self.text_option_2,
            screen=self.screen,
            font_size=20,
            on_click=self.choose_option_2,
            on_click_param=self.option_2,
            color=RED_COLOR
        )

    def draw(self):
        super().draw()
        for widget in self.widgets_list:
            widget.draw()

    def update(self):
        super().draw()
        for widget in self.widgets_list:
            widget.update()
