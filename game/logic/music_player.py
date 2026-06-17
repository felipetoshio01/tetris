import pygame

class MusicPlayer:
    def play(self) -> None:
        """
        Ativa a música do jogo
        """

        pygame.mixer.music.load("music/game_music.wav")
        pygame.mixer.music.set_volume(0.2)

        # Loop infinito
        pygame.mixer.music.play(-1)
