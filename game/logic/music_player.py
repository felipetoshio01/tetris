import pygame

class MusicPlayer:
    def play(self) -> None:
        pygame.mixer.music.load("music/game_music.wav")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
