# ================== Bibliotecas ================== 
import pygame
import sys

# ================== Componentes ================== 
from game.logic.renderer import Renderer
from game.logic.inputs import InputManager
from game.logic.updates import EventManager

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

        pygame.display.set_caption("Tetris")


    def run(self) -> None:
        """
        Começa o Game Loop
        """
        while game.running:
            self.input_manager.handle_inputs()
            self.event_manager.update()
            self.renderer.render()

            game.frame_cont += 1
            game.score += 1

            game.clock.tick(60)

        pygame.quit()
        sys.exit()
