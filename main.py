import pygame as pg

SCREEN_DIMENSIONS = (1200, 800)
WHITE_COLOR = (255, 255, 255)
GREEN_COLOR = (0, 255, 0)
NARUTO_COLOR = (255, 102, 0)

STAND_INIT_POS = (0, 0)
CENTER_SCREEN_POS = (600, 400)

COORDENADAS_RECTANGLE_PLAYER = (0, 550, 1200, 300)

pg.init()

screen = pg.display.set_mode(SCREEN_DIMENSIONS)

timer_1_Sec = pg.USEREVENT
pg.time.set_timer(timer_1_Sec, 1000)
limit_time = 15

background = pg.image.load("./assets/images/background.png")
stands = pg.transform.scale(background, SCREEN_DIMENSIONS)


stands = pg.image.load("./assets/images/stands-transformed.png")
stands = pg.transform.scale(stands, (1200, 550))

font = pg.font.Font("./assets/fonts/ninja-naruto.regular.ttf", 40)

pg.display.set_caption("Examen Chunnin")

text = font.render("Prueba de Texto", True, NARUTO_COLOR)
text_dimensions = text.get_size()


def get_screen_center(screen_dimensions, text_dimensions):
    center = screen_dimensions[0] // 2
    text_center = text_dimensions[0] // 2

    return center - text_center


# Bucle
game_running = True

while game_running:

    event_list = pg.event.get()

    for event in event_list:
        if event.type == pg.QUIT:
            game_running = False
        if event.type == pg.USEREVENT:
            if event.type == timer_1_Sec:
                # Detener timer cuando sea 0
                print("LIMIT TIME", limit_time)
                if limit_time != 0:
                    limit_time -= 1
        if event.type == pg.MOUSEBUTTONDOWN:
            print(event.pos)
        if event.type == pg.MOUSEBUTTONUP:
            pass
        if event.type == pg.MOUSEWHEEL:
            pass

    screen.fill(WHITE_COLOR)
    # pg.draw.circle(screen, GREEN_COLOR, (100, 100), 60)
    screen.blit(stands, STAND_INIT_POS)

    # Esto lo voy a usar para el menú
    # x_text_position = get_screen_center(SCREEN_DIMENSIONS, text_dimensions)
    # screen.blit(text, (x_text_position, 50))

    # Esto lo voy a usar para el tiempo limite para responder las preguntas.
    time_limit_text = font.render(str(limit_time), True, NARUTO_COLOR)
    x_limit_text_position = get_screen_center(SCREEN_DIMENSIONS, time_limit_text.get_size())
    screen.blit(time_limit_text, (x_limit_text_position, 50))

    pg.draw.rect(screen, NARUTO_COLOR, COORDENADAS_RECTANGLE_PLAYER)
    pg.display.flip()

pg.quit()