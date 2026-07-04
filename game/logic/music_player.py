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
            self.play_title_music()
            self.current_music = "title_screen"
        
        elif new_music == "game_screen":
            self.play_game_music()
            self.current_music = "game_screen"


    def play_game_music(self) -> None:
        pygame.mixer.music.load("music/game_music.wav")

        # Loop infinito
        pygame.mixer.music.play(-1)


    def play_title_music(self) -> None:
        pygame.mixer.music.load("music/title_music.mp3")

        # Loop infinito
        pygame.mixer.music.play(-1, fade_ms=2000)
