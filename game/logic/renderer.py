# ================== Bibliotecas ================== 
import pygame

# ================== Dados do jogo ================== 
from game.logic.game_data import game_data as game

# ================== Componentes ================== 
from game.components.button import Button

# ================== Configurações ================== 
from settings.dicts import COLORS
from settings.config import BORDER_WIDTH, BORDER_RADIUS, NUMBER_FONT, TITLE_FONT, TEXT_FONT, NUMBER_FONT


class Renderer:
    """
    Engloba o processamento gráfico do jogo
    """

    def render(self) -> None:
        game.screen.fill(COLORS["primary_color"])

        if game.state == "game_screen":
            game.screen.fill(COLORS["primary_color"])
            self._draw_game_screen()
        
        elif game.state == "title_screen":
            game.screen.fill(COLORS["primary_color"])
            self._draw_title_screen()
        
        elif game.state == "game_over_screen":
            game.screen.fill(COLORS["game_over_primary_color"])
            self._draw_game_over_screen()


        pygame.display.flip()


    def _draw_game_over_screen(self) -> None:

        # GAME OVER
        self._draw_game_over_title()

        # Melhor score
        self._draw_best_score_text()

        # Melhor level
        self._draw_best_level_text()
        
        # Botões
        retry_button: Button = Button(
            75,
            350,
            300,
            75,
            "Retry",
            COLORS["game_over_secondary_color"],
            COLORS["game_over_hover_color"],
            self._start_game
        )

        title_screen_button: Button = Button(
            75,
            450,
            300,
            75,
            "Tela inicial",
            COLORS["game_over_secondary_color"],
            COLORS["game_over_hover_color"],
            self._title_screen
        )

        retry_button.draw()
        title_screen_button.draw()


    def _draw_game_over_title(self) -> None:
        game_over_text = TITLE_FONT.render("GAME OVER", True, COLORS["text_color"])
        game_over_text_rect = game_over_text.get_rect()

        game_over_text_rect.center = (game.screen.width / 2, 150)
        game.screen.blit(game_over_text, game_over_text_rect)


    def _draw_best_score_text(self) -> None:
        best_score_text = TEXT_FONT.render("Melhor score", True, COLORS["text_color"])
        best_score_rect = best_score_text.get_rect() 

        score = NUMBER_FONT.render(f"{game.best_score:0>5}", True, COLORS["text_color"])
        score_rect = score.get_rect()

        best_score_rect.center = (game.screen.width / 2, 200)
        score_rect.center = (game.screen.width / 2, 225)

        game.screen.blit(best_score_text, best_score_rect)
        game.screen.blit(score, score_rect)


    def _draw_best_level_text(self) -> None:
        best_lvl_text = TEXT_FONT.render("Nível", True, COLORS["text_color"])
        lvl_text_rect = best_lvl_text.get_rect() 

        lvl = NUMBER_FONT.render(f"{game.best_lvl:0>2}", True, COLORS["text_color"])
        lvl_rect = lvl.get_rect()

        lvl_text_rect.center = (game.screen.width / 2, 275)
        lvl_rect.center = (game.screen.width / 2, 300)

        game.screen.blit(best_lvl_text, lvl_text_rect)
        game.screen.blit(lvl, lvl_rect)
 

    def _title_screen(self) -> None:
        game.state = "title_screen"


    def _draw_title_screen(self):
        title = TITLE_FONT.render("TETRIS", True, COLORS["text_color"])
        title_rect = title.get_rect()

        title_rect.center = (game.screen.width / 2, 150)
        game.screen.blit(title, title_rect)

        start_button: Button = Button(
            75,
            300,
            300,
            100,
            "Start",
            COLORS["secondary_color"],
            COLORS["hover_color"],
            self._start_game
        )

        start_button.draw()


    def _start_game(self) -> None:
        game.frame_cont = 0
        game.state = "game_screen"


    def _draw_game_screen(self):
        self._draw_pieces_area()
        self._draw_grid_lines()
        self._draw_score_area(game.get_score())
        self._draw_lvl_area()


    def _draw_pieces_area(self) -> None:
        """
        Desenha o Game Grid
        """

        # Cria a área dos bloquinhos
        pieces_area: pygame.Rect = pygame.Rect(25, 70, 250, 500)
        pygame.draw.rect(game.screen, COLORS['secondary_color'], pieces_area)

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
        
        # Texto
        label = TEXT_FONT.render("Score", True, COLORS["text_color"])
        label_rect = label.get_rect()

        # Fonte do score
        score = NUMBER_FONT.render(f"{score_num:0>5}", True, COLORS["text_color"])
        score_rect = score.get_rect()
        
        # Retângulo onde o score ficará
        score_area: pygame.Rect = pygame.Rect(300, 70, 125, 70)
        score_rect.center = score_area.center
        label_rect.center = score_area.center

        label_rect.top = score_area.top
        score_rect.top = label_rect.bottom + 5

        pygame.draw.rect(game.screen, COLORS["secondary_color"], score_area)
        self._draw_outline(score_area, BORDER_WIDTH, BORDER_RADIUS)

        game.screen.blit(score, score_rect)
        game.screen.blit(label, label_rect)


    def _draw_lvl_area(self) -> None:
        """
        Desenha a área do **score**
        """
        
        # Texto
        label = TEXT_FONT.render("Level", True, COLORS["text_color"])
        label_rect = label.get_rect()

        # Fonte do score
        lvl = NUMBER_FONT.render(f"{game.get_level():0>2}", True, COLORS["text_color"])
        lvl_rect = lvl.get_rect()
        
        # Retângulo onde o score ficará
        lvl_area: pygame.Rect = pygame.Rect(300, 500, 125, 70)
        lvl_rect.center = lvl_area.center
        label_rect.center = lvl_area.center

        label_rect.top = lvl_area.top
        lvl_rect.top = label_rect.bottom + 5

        pygame.draw.rect(game.screen, COLORS["secondary_color"], lvl_area)
        self._draw_outline(lvl_area, BORDER_WIDTH, BORDER_RADIUS)

        game.screen.blit(lvl, lvl_rect)
        game.screen.blit(label, label_rect)


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
