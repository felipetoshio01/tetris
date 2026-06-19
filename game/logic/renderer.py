# ================== Bibliotecas ================== 
import pygame

# ================== Dados do jogo ================== 
from game.logic.game_data import game_data as game

# ================== Configurações ================== 
from settings.dicts import COLORS
from settings.config import BORDER_WIDTH, BORDER_RADIUS, SCORE_FONT


class Renderer:
    """
    Engloba o processamento gráfico do jogo
    """

    def render(self) -> None:
        game.screen.fill(COLORS['bg_color'])

        self._draw_pieces_area()
        self._draw_grid_lines()
        self._draw_score_area(game.get_score())
            
        pygame.display.flip()


    def _draw_pieces_area(self) -> None:
        """
        Desenha o Game Grid
        """

        # Cria a área dos bloquinhos
        pieces_area: pygame.Rect = pygame.Rect(25, 70, 250, 500)
        pygame.draw.rect(game.screen, COLORS['bg_block_area_color'], pieces_area)

        self._draw_pieces()
        self._draw_outline(pieces_area, BORDER_WIDTH, BORDER_RADIUS)


    def _draw_pieces(self) -> None:
        """
        Desenha cada tile do Game Grid
        """

        # Desenhando os quadrados
        for y, row in enumerate(game.game_grid.matrix):
            for x, tile_type in enumerate(row):
                tile = pygame.Rect(x * 25 + 25, y * 25 + 70, 25, 25)

                # Cores dos quadradinhos
                if tile_type != "0":
                    pygame.draw.rect(game.screen, COLORS[tile_type], tile)


    def _draw_grid_lines(self) -> None:
        """
        Desenha as linhas do Game Grid
        """
        for y in range(19):
            pygame.draw.line(game.screen, COLORS['block_area_line'], (25, y * 25 + 95), (275, y * 25 + 95))

        for x in range(9):
            pygame.draw.line(game.screen, COLORS['block_area_line'], (x * 25 + 50, 70), (x * 25 + 50, 570))


    def _draw_score_area(self, score_num: str = "0") -> None:
        """
        Desenha a área do **score**
        """
        
        # Fonte do score
        score = SCORE_FONT.render(score_num, True, (255, 255, 255))
        score_rect = score.get_rect()
        
        # Retângulo onde o score ficará
        score_area: pygame.Rect = pygame.Rect(300, 70, 125, 70)
        score_rect.center = score_area.center

        pygame.draw.rect(game.screen, COLORS["bg_block_area_color"], score_area)
        self._draw_outline(score_area, BORDER_WIDTH, BORDER_RADIUS)

        game.screen.blit(score, score_rect)


    def _draw_outline(self, rect: pygame.Rect, width: int, radius: int = 0) -> None:
        """
        Desenha uma borda ao redor do retângulo especificado (`rect`), com a largura e arredondamento especificado
        """

        border: pygame.Rect = pygame.Rect(
            rect.x - width,
            rect.y - width,
            rect.width + 2 * width,
            rect.height + 2 * width
        )

        pygame.draw.rect(
            game.screen,
            COLORS['block_area_border_color'],
            border,
            width=width,
            border_radius=radius
        )
