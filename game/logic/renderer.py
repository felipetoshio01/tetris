# ================== Bibliotecas ================== 
import pygame

# ================== Dados do jogo ================== 
from game.logic.game_data import game_data as game
from game.logic.music_player import MusicPlayer

# ================== Componentes ================== 
from game.components.button import Button

# ================== Configurações ================== 
from settings.dicts import COLORS
from settings.config import BORDER_WIDTH, BORDER_RADIUS, NUMBER_FONT, TITLE_FONT


class Renderer:
    """
    Engloba o processamento gráfico do jogo
    """

    def render(self) -> None:
        game.screen.fill(COLORS['bg_color'])

        if game.state == "game_screen":
            self._draw_game_screen()
        
        elif game.state == "title_screen":
            self._draw_title_screen()

        pygame.display.flip()


    def _draw_title_screen(self):
        title = TITLE_FONT.render(text="TETRIS", antialias=True, color=COLORS["text_color"])
        title_rect = title.get_rect()

        title_rect.center = (game.screen.width / 2, 150)
        game.screen.blit(title, title_rect)

        start_button: Button = Button(
            x=75,
            y=300,
            width=300,
            height=100,
            text="Start",
            function=self._start_game
        )

        start_button.draw()


    def _start_game(self) -> None:
        game.frame_cont = 0
        game.state = "game_screen"


    def _draw_game_screen(self):
        self._draw_pieces_area()
        self._draw_grid_lines()
        self._draw_score_area(game.get_score())


    def _draw_pieces_area(self) -> None:
        """
        Desenha o Game Grid
        """

        # Cria a área dos bloquinhos
        pieces_area: pygame.Rect = pygame.Rect(left=25, top=70, width=250, height=500)
        pygame.draw.rect(surface=game.screen, color=COLORS['bg_block_area_color'], rect=pieces_area)

        self._draw_pieces()
        self._draw_outline(pieces_area, BORDER_WIDTH, BORDER_RADIUS)


    def _draw_pieces(self) -> None:
        """
        Desenha cada tile do Game Grid
        """

        # Desenhando os quadrados
        for y, row in enumerate(game.game_grid.matrix):
            for x, tile_type in enumerate(row):
                tile = pygame.Rect(left=x * 25 + 25, top=y * 25 + 70, width=25, height=25)

                # Cores dos quadradinhos
                if tile_type != "0":
                    pygame.draw.rect(surface=game.screen, color=COLORS[tile_type], rect=tile)


    def _draw_grid_lines(self) -> None:
        """
        Desenha as linhas do Game Grid
        """
        for y in range(19):
            pygame.draw.line(
                surface=game.screen,
                color=COLORS['block_area_line'],
                start_pos=(25, y * 25 + 95),
                end_pos=(275, y * 25 + 95)
            )

        for x in range(9):
            pygame.draw.line(
                surface=game.screen,
                color=COLORS['block_area_line'],
                start_pos=(x * 25 + 50, 70),
                end_pos=(x * 25 + 50, 570)
            )


    def _draw_score_area(self, score_num: str = "0") -> None:
        """
        Desenha a área do **score**
        """
        
        # Fonte do score
        score = NUMBER_FONT.render(text=score_num, antialias=True, color=COLORS["text_color"])
        score_rect = score.get_rect()
        
        # Retângulo onde o score ficará
        score_area: pygame.Rect = pygame.Rect(left=300, top=70, width=125, height=70)
        score_rect.center = score_area.center

        pygame.draw.rect(surface=game.screen, color=COLORS["bg_block_area_color"], rect=score_area)
        self._draw_outline(score_area, BORDER_WIDTH, BORDER_RADIUS)

        game.screen.blit(score, score_rect)


    def _draw_outline(self, rect: pygame.Rect, width: int, radius: int = 0) -> None:
        """
        Desenha uma borda ao redor do retângulo especificado (`rect`), com a largura e arredondamento especificado
        """

        border: pygame.Rect = pygame.Rect(
            left=rect.x - width,
            top=rect.y - width,
            width=rect.width + 2 * width,
            height=rect.height + 2 * width
        )

        pygame.draw.rect(
            surface=game.screen,
            color=COLORS['block_area_border_color'],
            rect=border,
            width=width,
            border_radius=radius
        )
