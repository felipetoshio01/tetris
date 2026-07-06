# ================== Bibliotecas ================== 
import pygame

# ================== Dados do jogo ================== 
from game.logic.game_data import game_data as game


class MusicPlayer:
    
    current_music: str | None = None

    def play(self) -> None:
        """
        Ativa a música do jogo
        """
        new_music = game.state

        if new_music == self.current_music:
            return

        pygame.mixer.music.fadeout(200)
        pygame.mixer.music.set_volume(0.2)

        if new_music == "title_screen":
            self.load_title_music()
            self.current_music = "title_screen"
            pygame.mixer.music.play(-1)
        
        elif new_music == "game_screen":
            self.load_game_music()
            self.current_music = "game_screen"
            pygame.mixer.music.play(-1)

        elif new_music == "game_over_screen":
            self.load_game_over_music()
            self.current_music = "game_over_screen"
            pygame.mixer.music.play()   


    def load_game_music(self) -> None:
        pygame.mixer.music.load("music/game_music.wav")


    def load_title_music(self) -> None:
        pygame.mixer.music.load("music/title_music.mp3")


    def load_game_over_music(self) -> None:
        pygame.mixer.music.load("music/game_over_sound.wav")
