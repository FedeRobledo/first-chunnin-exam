import sys
import pygame as pg

from .constants import (SCREEN_DIMENSIONS)

print(SCREEN_DIMENSIONS)


def run_game():
    pg.init()

    main_menu = pg.display.set_mode(SCREEN_DIMENSIONS)
    pg.display.set_caption('Examen Chunnin')
    run = True
    while run:
        event_list = pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                run = False
        # Tengo que comenzar a dibujar las pantallas, debo ver formularios.
    pg.quit()
    sys.exit()
