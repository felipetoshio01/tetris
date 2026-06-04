import pygame
from collections.abc import Callable

class Timer:
    def __init__(self, duration: float, callback: Callable, repeat: bool = False) -> None:
        self.duration = duration
        self.start_time = pygame.time.get_ticks()
        self.callback = callback
        self.repeat = repeat
        self.active = True


    def update(self) -> None:
        current_time: float = pygame.time.get_ticks()

        if not self.active:
            return

        if current_time - self.start_time >= self.duration:
            self.handle_callback()

            if not self.repeat:
                self.active = False


    def handle_callback(self) -> None:
        self.callback()
        self.start_time = pygame.time.get_ticks()
