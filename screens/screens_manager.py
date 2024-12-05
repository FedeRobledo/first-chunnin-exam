from modules.constants import (GAME_SOUND)

from .main_menu import MainMenu
from .enter_name import EnterNameScreen
from .options import Options
from .game_screen import Game


from game.player import Player


class ScreensManager:

    def __init__(self, screen):
        self.main_screen = screen
        self.current_level = 0
        self.game_started = False
        self.jugador_actual = Player()

        self.screens = [
            MainMenu(name='main_menu', screen=self.main_screen, x=0,
                     y=0, active=True, level_num=1, music_path=GAME_SOUND),
            EnterNameScreen(name='screen_enter_name', screen=self.main_screen,
                            x=0, y=0, active=True, level_num=1, music_path=GAME_SOUND, score=0),
            Options(name='screen_options', screen=self.main_screen, x=0,
                    y=0, active=True, level_num=1, music_path=GAME_SOUND),
            Game(name='game_screen', screen=self.main_screen, x=0,
                    y=0, active=True, level_num=1, music_path=GAME_SOUND),
        ]

    def keys_update(self, event_list: list) -> None:
        '''
        Checks if ESC key is pressed to acces the Pause form
        Arguments: event list (list)
        Returns: None
        '''

        # for event in event_list:
        #     if (event.type == pg.KEYDOWN):
        #         if (event.key == pg.K_ESCAPE):
        #             self.screens[3].set_active("pause")

    def screens_update(self, event_list: list):

        if self.screens[0].active:
            self.screens[0].update()
            self.screens[0].draw()

        elif self.screens[1].active:
            self.screens[1].update(event_list)
            self.screens[1].draw()

        elif self.screens[2].active:
            self.screens[2].update()
            self.screens[2].draw()

        elif self.screens[3].active:
            self.screens[3].update()
            self.screens[3].draw()

            # if self.screens[3].level_restart:
            #     # Inicializar nuevamente el nivel actual del formulario gestionador de niveles
            #     pass

        # elif self.screens[4].active:
        #     self.screens[4].update(event_list)
        #     self.screens[4].draw()

    def update(self, event_list: list):
        self.keys_update(event_list)
        self.screens_update(event_list)
