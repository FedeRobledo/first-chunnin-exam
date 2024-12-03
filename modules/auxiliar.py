import pygame as pg
from modules.constants import (
   RANKING_FILE_PATH
)


def get_images(image_path, size):
    image_raw = pg.image.load(image_path)
    image = pg.transform.scale(image_raw, size)
    return image


def get_ranking():
    ranking = []
    with open(RANKING_FILE_PATH, 'r') as rank:
        rows = rank.read()
        for row in rows.split('\n'):
            ranking.append(row.split(','))
    sort_matrix(ranking)
    return ranking


def sort_matrix(matrix: list[list]):
    for i in range(len(matrix) - 1):
        for j in range(i+1, len(matrix)):
            if int(matrix[i][1]) < int(matrix[j][1]):
                matrix[i], matrix[j] =\
                    matrix[j], matrix[i]


def save_score(player_score):
    with open(RANKING_FILE_PATH, '+a') as rkn:
        rkn.write(player_score.to_csv_format())
        print(f'Se guardo el puntaje del jugador: {player_score}')