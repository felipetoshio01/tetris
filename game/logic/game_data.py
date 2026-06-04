# ================== Bibliotecas ================== 
import pygame

# ================== Componentes ================== 
from game.components.tile_map import TileMap
from game.components.piece import Piece

# ================== Configurações ================== 
from settings.config import start_falling_speed, fast_falling_speed


class GameData:
    """
    Objeto que contém as informações sobre o jogo
    """

    def __init__(self) -> None:
        pygame.init()

        self.screen: pygame.surface.Surface = pygame.display.set_mode((450, 640))
        self.clock: pygame.Clock = pygame.Clock()
        self.running: bool = True

        # Áreas dos blocos
        self.game_grid: TileMap = TileMap()

        # Peça do jogo
        self.piece: Piece
        
        # Se há peça ativa
        self.have_active_piece = False

        # Ordem de surgimento de peças
        self.pieces_poll: list[str] = []

        # Contador de frames
        self.frame_cont: int = 0

        # Velocidade atual queda (cells/frame)
        self.falling_speed = start_falling_speed
        
        # Velocidade normal de queda
        self.normal_falling_speed = start_falling_speed

        # Velocidade acelerado de queda (soft drop)
        self.fast_falling_speed = fast_falling_speed


# Objeto que guarda as informações do jogo
game_data: GameData = GameData()
