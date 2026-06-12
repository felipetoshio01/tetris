# ================== Bibliotecas ================== 
import pygame
import sys

pygame.init()

# ================== Componentes ================== 
from game.logic.renderer import Renderer
from game.logic.inputs import InputManager
from game.logic.updates import EventManager
from game.logic.music_player import MusicPlayer

# ================== Dados do jogo ================== 
from game.logic.game_data import game_data as game


class Tetris:
    """
    Objetos que executará o Game Loop do jogo
    """

    def __init__(self) -> None:
        self.input_manager: InputManager = InputManager()
        self.event_manager: EventManager = EventManager()
        self.renderer: Renderer = Renderer()
        self.music_player: MusicPlayer = MusicPlayer()

        pygame.display.set_caption("Tetris")


    def run(self) -> None:
        """
        Começa o Game Loop
        """

        self.music_player.play()
        
        while game.running:
            self.input_manager.handle_inputs()
            self.event_manager.update()
            self.renderer.render()

            game.frame_cont += 1

            game.clock.tick(60)

        pygame.quit()
        sys.exit()
