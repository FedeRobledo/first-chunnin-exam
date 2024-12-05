import pygame as pg
from .base_screen import Screen
from widgets import (
    Button, TextTitle
)
from modules.constants import SCREEN_DIMENSIONS, BACKGROUND_PATH, GREEN_COLOR


class Options(Screen):

    def __init__(self, name, screen, x, y, active, level_num, music_path):
        super().__init__(name, screen, x, y, active, level_num, music_path)

        self.surface = pg.image.load(BACKGROUND_PATH).convert_alpha()
        self.surface = pg.transform.scale(self.surface, SCREEN_DIMENSIONS)

        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y

        self.optiones_title = TextTitle(
            x=SCREEN_DIMENSIONS[0]//2, y=50, text='Examen Chunnin', screen=screen, font_size=60)
        self.optiones_subtitle = TextTitle(
            x=SCREEN_DIMENSIONS[0]//2, y=SCREEN_DIMENSIONS[1]//2-100, text='Opciones', screen=screen, font_size=40)

        # Estado inicial de la música
        self.music_paused = False
        self.music_button_text = "MUSICA SI"

        self.button_back = Button(
            x=SCREEN_DIMENSIONS[0]//2,
            y=SCREEN_DIMENSIONS[1]//2 + 200,
            text='Volver Al Menu',
            screen=screen, on_click=self.click_back,
            on_click_param='main_menu'
        )

        # Botón único para alternar la música
        self.button_toggle_music = Button(
            x=SCREEN_DIMENSIONS[0]//2,
            y=SCREEN_DIMENSIONS[1]//2,
            text=self.music_button_text,
            screen=screen,
            on_click=self.toggle_music
        )

        self.widgets_list = [
            self.optiones_subtitle, self.optiones_title,
            self.button_toggle_music,
            self.button_back,
        ]

        self.music_update()
        self.update_music_button()

    def toggle_music(self, parametro=None):
        """Cambia el estado de la música y actualiza el texto del botón."""
        if self.music_paused:
            pg.mixer.music.unpause()
        else:
            pg.mixer.music.pause()
        self.music_paused = not self.music_paused
        self.update_music_button()  # Asegúrate de actualizar el botón tras cambiar el estado

    def update_music_button(self):
        """Actualiza el texto del botón según el estado de la música."""
        if not self.music_paused:
            self.music_button_text = 'MUSICA SI'
        else:
            self.music_button_text = 'MUSICA NO'

        # Redibujar el texto del botón
        self.button_toggle_music.text = self.music_button_text
        self.button_toggle_music.image = self.button_toggle_music.font.render(
            self.button_toggle_music.text, True, GREEN_COLOR
        )

    def click_music_on(self, parametro):
        pg.mixer.music.unpause()

    def click_music_off(self, parametro):
        pg.mixer.music.pause()

    def click_back(self, parametro):
        self.set_active(parametro)

    def draw(self):
        super().draw()
        for widget in self.widgets_list:
            widget.draw()

    def update(self):
        self.update_music_button()
        super().draw()
        for widget in self.widgets_list:
            widget.update()
