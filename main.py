import pygame
import random

from engine import TileMap, Piece
from constants import COLORS


def choose_piece() -> str:
    pieces: list[str] = ["I", "O", "L", "J", "S", "Z"]
    
    return random.choice(pieces)


def main() -> None:
    pygame.init()

    # ================== OBJETOS DE CRIAÇÃO ================== 
    screen: pygame.surface.Surface = pygame.display.set_mode((450, 640))
    clock: pygame.Clock = pygame.Clock()
    running: bool = True

    game_grid: TileMap = TileMap()


    # ================== VARIÁVEIS ================== 
    have_active_piece: bool = False
    piece: Piece = Piece()
    

    # ================== GAME LOOP ================== 
    while running:

        # ================== COMANDOS ==================   
        for event in pygame.event.get():

            # Saída do jogo
            if event.type == pygame.QUIT:
                running = False
            
            # Se houver uma peça ativa, execute o movimento delas
            if have_active_piece:
                if event.type == pygame.KEYDOWN:

                    # Descer
                    if event.key == pygame.K_DOWN:
                        piece.move_down(game_grid)
                
                    # Esquerda
                    if event.key == pygame.K_LEFT:
                        piece.move_left(game_grid)

                    # Direita
                    if event.key == pygame.K_RIGHT:
                        piece.move_right(game_grid)


        # ================== SURFACES ================== 
        blocks_area: pygame.Rect = pygame.Rect(25, 70, 250, 500)


        # ================== DESENHOS ==================
        screen.fill(COLORS['bg_color'])
        pygame.draw.rect(screen, COLORS['bg_block_area_color'], blocks_area)

        # Se não houver peça ativa, desenhe ela
        if not have_active_piece:
            piece_type: str = choose_piece()
            piece = game_grid.add_piece(piece_type)
            have_active_piece = True

        # Desenhando os quadrados
        for y, row in enumerate(game_grid.matrix):
            for x, tile_type in enumerate(row):
                tile = pygame.Rect(x * 25 + 25, y * 25 + 70, 25, 25)

                # Cores dos quadradinhos
                if tile_type != 0:
                    pygame.draw.rect(screen, COLORS[piece.type], tile)

                # Desenha a borda
                pygame.draw.rect(screen, COLORS['block_area_line'], tile, width=1)

        pygame.display.flip()


        # FPS
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()