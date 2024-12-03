from modules.sound import Sound

class Screen:
    screens_dict = {}
    
    def __init__(self, name: str, screen, x: int, y: int, active: bool, level_num: int, music_path: str):
        self.screens_dict[name] = self
        self.screen = screen
        self.active = active
        self.x = x
        self.y = y
        self.level_num = level_num
        self.music_path = music_path
        self.admin_sound = Sound()
    
    # Selecciono que pantalla mostrar por nombre y actualizo la musica.
    def set_active(self, name: str):
        for aux_screen in self.screens_dict.values():
            aux_screen.active = False
        self.screens_dict[name].active = True
        self.music_update()
    
    def music_update(self):
        self.admin_sound.stop_music()
        self.admin_sound.play_music(f'{self.music_path}')
    
    def draw(self):
        self.screen.blit(self.surface, self.slave_rect)
