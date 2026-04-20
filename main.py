import pygame
import random
 
from engine import TileMap, Piece
from constants import COLORS


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

        # Timers
        self.MOVE_DOWN = pygame.USEREVENT + 1
        pygame.time.set_timer(self.MOVE_DOWN, 800)


    def _handle_events(self) -> None:
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
                    if event.key == pygame.K_LEFT:
                        self.piece.move_left()

                    # Direita
                    if event.key == pygame.K_RIGHT:
                        self.piece.move_right()
                
                # Desce a peça
                if event.type == self.MOVE_DOWN:
                    self._handle_move_down()


    def _handle_move_down(self) -> None:
        """
        Faz o movimento da `Piece` descer dentro do `TileMap`.
        Se a `Piece` atingiu o chão ou outra peça, fixe ela
        """

        # Se a peça atingiu uma coisa
        if self.piece.hit_ground():
            self.piece.fix_piece()
            self.have_active_piece = False     

        # Senão, desça normal
        else:
            self.piece.move_down()


    def _shuffle_new_pieces(self) -> None:
        """
        Reembaralha a `Game.pieces_poll`
        """

        pieces: list[str] = ["I", "O", "L", "J", "S", "Z"]
        self.pieces_poll = random.sample(pieces, 6)


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
            self.piece = self.game_grid.add_piece(piece_type)
            self.have_active_piece = True


    def _draw(self) -> None:
        """
        Atualiza de desenha todos os elementos da tela
        """

        # Limpa a tela
        self.screen.fill(COLORS['bg_color'])

        # Cria a área dos bloquinhos
        blocks_area: pygame.Rect = pygame.Rect(25, 70, 250, 500)
        pygame.draw.rect(self.screen, COLORS['bg_block_area_color'], blocks_area)

        # Desenhando os quadrados
        for y, row in enumerate(self.game_grid.matrix):
            for x, tile_type in enumerate(row):
                tile = pygame.Rect(x * 25 + 25, y * 25 + 70, 25, 25)

                # Cores dos quadradinhos
                if tile_type != "0":
                    pygame.draw.rect(self.screen, COLORS[tile_type], tile)

                # Desenha a borda
                pygame.draw.rect(self.screen, COLORS['block_area_line'], tile, width=1)

        pygame.display.flip()


    def run(self) -> None:
        """
        Instancia o *Game Loop*
        """

        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(60)
        
        pygame.quit()


if __name__ == '__main__':
    game: Game = Game()
    game.run()
