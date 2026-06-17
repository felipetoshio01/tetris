# ================== Bibliotecas ================== 
import pygame

# ================== Componentes ================== 
from game.components.tile_map import TileMap
from game.components.piece import Piece

# ================== Configurações ================== 
from settings.config import fast_falling_speed
from settings.dicts import SPEEDS


class GameData:
    """
    Objeto que contém as informações sobre o jogo
    """

    def __init__(self) -> None:
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

        # Número de linhas limpas
        self.rows_cleared: int = 0
        
        # Contador de frames
        self.frame_cont: int = 0

        # Velocidade atual queda (cells/frame)
        self.falling_speed = SPEEDS[0]
        
        # Velocidade normal de queda
        self.normal_falling_speed = SPEEDS[0]

        # Velocidade acelerado de queda (soft drop)
        self.fast_falling_speed = fast_falling_speed
        
        # Pontuação do jogo
        self.score: int = 0

        # Se a peça está em processo de hard drop
        self.hard_drop: bool = False


    def get_level(self) -> int:
        """
        Retorna o **Level** do jogo. A cada 10 **rows** limpas, um **Level** é adicionado

        """
        level: int = self.rows_cleared // 10

        return level
    
    
    def get_score(self) -> str:
        """
        Retorna o **score** do jogo em formato de string
        """

        return str(self.score)


# Objeto que guarda as informações do jogo
game_data: GameData = GameData()
