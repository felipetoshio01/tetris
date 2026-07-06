# ================== Bibliotecas ================== 
import pygame
from collections.abc import Callable

# ================== Dados do jogo ================== 
from game.logic.game_data import game_data as game

# ================== Configurações ================== 
from settings.config import TEXT_FONT, BORDER_RADIUS
from settings.dicts import COLORS


class Button:
    def __init__(self,
                 x: int,
                 y: int,
                 width: int,
                 height: int, 
                 text: str,
                 default_color: pygame.Color,
                 hover_color: pygame.Color,
                 function: Callable) -> None:

        # Retângulo do botão
        self.button_rect: pygame.Rect = pygame.Rect(x, y, width, height)
        self.default_color = default_color
        self.hover_color = hover_color

        # Texto do botão
        self.button_text = TEXT_FONT.render(text, True, COLORS["text_color"])

        # Centralizar texto do botão
        self.text_rect = self.button_text.get_rect()
        self.text_rect.center = self.button_rect.center

        # Função do botão
        self.function = function
    

    def draw(self) -> None:
        """
        Desenha o botão
        """
        
        mouse_pos: tuple[int, int] = pygame.mouse.get_pos()
        button_color = self.default_color

        # Se o mouse entrou
        if self.button_rect.collidepoint(mouse_pos):
            button_color = self.hover_color

            # Se o mouse entro e clicou
            if pygame.mouse.get_pressed()[0] == 1:
                button_color = COLORS["click_color"]
                self.function()
        
        # Desenha o botão
        pygame.draw.rect(
            game.screen,
            button_color,
            self.button_rect,
            border_radius=BORDER_RADIUS
        )
        
        # Coloca o texto
        game.screen.blit(self.button_text, self.text_rect)
