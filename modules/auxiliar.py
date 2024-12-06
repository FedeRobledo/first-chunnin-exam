import pygame as pg

import json
import random

from modules.constants import (
   RANKING_FILE_PATH, ASKS_PATH
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


# Bubble sort

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


def import_and_return_asks() -> list:
    """
    Carga las preguntas desde un archivo JSON, las ordena aleatoriamente
    y las devuelve como una lista para ser usadas en el juego.
    """

    # Cargar el archivo JSON
    with open(ASKS_PATH, "r", encoding="utf-8") as file:
        preguntas = json.load(file)
    
    # Mezclar aleatoriamente las preguntas
    random.shuffle(preguntas)

    # Mezclar respuestas de cada pregunta
    for pregunta in preguntas:
        if "respuestas" in pregunta:
            random.shuffle(pregunta["respuestas"])

    return preguntas