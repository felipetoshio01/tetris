# ================== Bibliotecas ================== 
import pygame

# ================== Dados do jogo ================== 
from game.logic.game_data import game_data as game

# ================== Configurações ================== 
from settings.dicts import COLORS
from settings.config import pieces_area_board_width, pieces_area_board_radius


class Renderer:
    """
    Engloba o processamento gráfico do jogo
    """

    def render(self) -> None:
        game.screen.fill(COLORS['bg_color'])

        self._draw_pieces_area()
        self._draw_grid_lines()
            
        pygame.display.flip()


    def _draw_pieces_area(self) -> None:
        """
        Desenha o Game Grid
        """

        # Cria a área dos bloquinhos
        pieces_area: pygame.Rect = pygame.Rect(25, 70, 250, 500)
        pygame.draw.rect(game.screen, COLORS['bg_block_area_color'], pieces_area)

        self._draw_pieces()

        # Cria a borda da área dos bloquinhos
        pieces_area_border: pygame.Rect = pygame.Rect(
            25 - pieces_area_board_width,
            70 - pieces_area_board_width,
            250 + 2 * pieces_area_board_width,
            500 + 2 * pieces_area_board_width
        )
        pygame.draw.rect(
            game.screen,
            COLORS['block_area_border_color'], 
            pieces_area_border, 
            width=pieces_area_board_width, 
            border_radius=pieces_area_board_radius
        )


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
