import pygame.mixer as mixer


class Sound:
    def __init__(self):
        mixer.init()

    def play_sound(self, ruta_snd: str):
        sound = mixer.Sound(ruta_snd)
        sound.set_volume(0.8)
        sound.play()
    
    def play_music(self, ruta_musica: str):
        mixer.music.load(ruta_musica)
        mixer.music.set_volume(0.3)
        mixer.music.play(-1, 0, 3000)
    
    def stop_music(self):
        mixer.music.fadeout(500)
        # mixer.music.stop()
