import pygame
import random
 
from piece import Piece
from tile_map import TileMap
from timer import Timer
from settings.dicts import COLORS


class Game:
    def __init__(self) -> None:
        pygame.init()

        # Objetos de criação
        self.screen: pygame.surface.Surface = pygame.display.set_mode((450, 640))
        self.clock: pygame.Clock = pygame.Clock()
        self.running: bool = True

        # Variáveis
        self.game_grid: TileMap = TileMap()
        self.have_active_piece: bool = False
        self.piece: Piece
        self.pieces_poll: list[str] = []
        self.fall_speed: int = 800

        # Timers
        self.move_down_timer: Timer = Timer(self.fall_speed, self._handle_move_down, repeat=True)


    def _handle_touch_events(self) -> None:
        """
        Cuida dos eventos do *Game Loop*
        """
        for event in pygame.event.get():

            # Saída do jogo
            if event.type == pygame.QUIT:
                self.running = False

            # Se houver uma peça ativa, execute o movimento delas
            if self.have_active_piece:
                if event.type == pygame.KEYDOWN:              
                    # Esquerda
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        self.piece.move_left(1)

                    # Direita
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        self.piece.move_right(1)

                    # Rotaciona para a esquerda
                    if event.key == pygame.K_z:
                        self.piece.rotate("left")   
                    
                    # Rotaciona para a direita
                    if event.key == pygame.K_x:
                        self.piece.rotate("right")


    def _handle_hold_events(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            self.move_down_timer.duration = 100
            
        else:
            self.move_down_timer.duration = self.fall_speed



    def _handle_move_down(self) -> None:
        """
        Faz o movimento da `Piece` descer dentro do `TileMap`.
        Se a `Piece` atingiu o chão ou outra peça, fixe ela (`Piece.fix_piece()`)
        """
        
        # Se a peça atingiu uma coisa
        if self.piece.hit_ground():
            self.piece.fix_piece()

            # Após fixar, limpe as linhas completas
            self.game_grid.clear_complete_rows()

            # Avisa que não tem uma peça ativa
            self.have_active_piece = False     

        # Senão, desça normal
        else:
            self.piece.move_down(1)


    def _shuffle_new_pieces(self) -> None:
        """
        Reembaralha a `Game.pieces_poll`
        """

        pieces: list[str] = ["I", "T", "O", "L", "J", "S", "Z"]
        self.pieces_poll = random.sample(pieces, 7)


    def _choose_piece(self) -> str:
        """
        Seleciona uma peça dentro do `Game.pieces_poll`. 
        Se a lista estiver vazia, será criado uma nova e escolhido um novo elemento dessa nova lista
        """

        # Se não houver mais peças, crie uma nova lista
        if not self.pieces_poll:
            self._shuffle_new_pieces()

        selected_piece: str = self.pieces_poll.pop()

        return selected_piece


    def _update(self) -> None:
        """
        Atualiza todo a lógica do *Game Loop*
        """

        # Se não houver peça ativa, desenhe ela
        if not self.have_active_piece:
            piece_type: str = self._choose_piece()
            self.piece = Piece(self.game_grid, piece_type)

            # GAME OVER
            if not self.piece.is_position_valid():
                self.game_grid.clear_matrix()

            self.piece.add_piece()
            self.have_active_piece = True


    def _draw(self) -> None:
        """
        Atualiza e desenha todos os elementos da tela
        """

        # Limpa a tela
        self.screen.fill(COLORS['bg_color'])

        # Desenha a área dos bloquinhos
        self._draw_grid_board()        
        self._draw_grid_lines()

        pygame.display.flip()


    def _draw_pieces(self) -> None:
        """
        Desenha cada tile do Game Grid
        """

        # Desenhando os quadrados
        for y, row in enumerate(self.game_grid.matrix):
            for x, tile_type in enumerate(row):
                tile = pygame.Rect(x * 25 + 25, y * 25 + 70, 25, 25)

                # Cores dos quadradinhos
                if tile_type != "0":
                    pygame.draw.rect(self.screen, COLORS[tile_type], tile)


    def _draw_grid_board(self) -> None:
        """
        Desenha o local onde as peças se mexem
        """

        border_width: int = 5

        # Cria a área dos bloquinhos
        blocks_area: pygame.Rect = pygame.Rect(25, 70, 250, 500)
        pygame.draw.rect(self.screen, COLORS['bg_block_area_color'], blocks_area)

        self._draw_pieces()
        
        blocks_area_border: pygame.Rect = pygame.Rect(
            25 - border_width,
            70 - border_width,
            250 + 2 * border_width,
            500 + 2 * border_width
        )

        pygame.draw.rect(
            self.screen,
            COLORS['block_area_border_color'], 
            blocks_area_border, 
            width=border_width, 
            border_radius=15
        )


    def _draw_grid_lines(self) -> None:
        """
        Desenha as linhas do Game Grid
        """
        for y in range(19):
            pygame.draw.line(self.screen, COLORS['block_area_line'], (25, y * 25 + 95), (275, y * 25 + 95))

        for x in range(9):
            pygame.draw.line(self.screen, COLORS['block_area_line'], (x * 25 + 50, 70), (x * 25 + 50, 570)) 


    def run(self) -> None:
        """
        Instancia o *Game Loop*
        """

        while self.running:
            self._handle_touch_events()
            self._handle_hold_events()
            self.move_down_timer.update()
            self._update()
            self._draw()
            self.clock.tick(60)
        
        pygame.quit()


if __name__ == '__main__':
    game: Game = Game()
    game.run()
