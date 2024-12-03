import sys
import pygame as pg

from modules.constants import (SCREEN_DIMENSIONS)
from screens.screens_manager import ScreensManager


def start_game():
    pg.init()

    main_menu = pg.display.set_mode(SCREEN_DIMENSIONS, pg.SCALED)
    pg.display.set_caption('Examen Chunnin')
    run = True

    screens = ScreensManager(main_menu)
    
    while run:
        event_list = pg.event.get()
        for event in event_list:
            if event.type == pg.QUIT:
                run = False

        screens.update(event_list)
        pg.display.update()

    pg.quit()
    sys.exit()
