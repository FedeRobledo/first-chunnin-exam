import pygame as pg
from modules.auxiliar import get_images
from modules.constants import PLAYER_PATH, PLAYER_SIZE


class Player:
    _instanced = None
    
    def __init__(self, name: str = 'Jugador', pos_x: int = 0, pos_y: int = 0):
        
        if Player._instanced is None:
            Player._instanced = self
        
        self.name = name
        self.score = 0
        self.total_score = 0
        self.image = get_images(PLAYER_PATH, PLAYER_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    @staticmethod
    def get_player():
        if Player._instanced is None:
            Player()
        return Player._instanced
    
    @staticmethod
    def is_instantiated():
        return Player._instanced is not None
    
    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name
    
    def get_actual_score(self):
        return self.score
    
    def get_total_score(self):
        return self.total_score
    
    def set_score(self, score: int):
        self.score = score
    
    def add_score(self, score: int):
        self.score += score
    
    def update_total_score(self):
        self.total_score += self.score
    
    # Revisar bien el tema de la /n para cuando lo tenga que leer en la pantalla Ranking
    def to_csv_format(self):
        return f'\n{self.name},{self.total_score}'
    
    def events(self, event_list: list):
        pass

        # Agregar mis propios eventos en función de lo que necesite. 
         
        # for event in event_list:
        #     if event.type == pg.KEYDOWN:
        #         if event_list[pg.K_LEFT]:
        #             self.rect.x -= 2
        #         if event_list[pg.K_RIGHT]:
        #             self.rect.x += 2
        #         if event_list[pg.K_UP]:
        #             self.rect.y -= 2
        #         if event_list[pg.K_DOWN]:
        #             self.rect.y += 2
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self, event_list):
        self.events(event_list)
