import pygame as pg


def get_images(image_path, size):

    image_raw = pg.image.load(image_path)
    image = pg.transform.scale(image_raw, size)

    return image
