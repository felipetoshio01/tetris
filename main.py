import pygame
import random

colors: dict[str, tuple[int, int, int]] = {
    "bg_color": (27, 27, 27),
    "bg_block_area_color": (40, 40, 40),
    "block_area_line": (200, 200, 200),

    "I": (81, 225, 252),
    "O": (254, 248, 76),
    "T": (148, 54, 146),
    "J": (71, 121, 212),
    "L": (246, 146, 48),
    "S": (233, 61, 30),
    "Z": (121, 174, 61)

}

pieces_coords: dict[str, list[list[int]]] = {
    "I": [[0, 3], [0, 4], [0, 5], [0, 6]],
    "O": [[0, 4], [0, 5], [1, 4], [1, 5]],
    "T": [[0, 4], [1, 3], [1, 4], [1, 5]],
    "J": [[0, 3], [1, 3], [1, 4], [1, 5]],
    "L": [[0, 5], [1, 3], [1, 4], [1, 5]],
    "S": [[0, 4], [0, 5], [1, 3], [1, 4]],
    "Z": [[0, 3], [0, 4], [1, 4], [1, 5]]
}

class Piece:
    def __init__(self, type: str = "", coords: list[list[int]] = [[0, 0]]) -> None:
        self.type = type
        self.coords = coords

    def is_valid_down(self) -> bool:
        for coord in self.coords:
            row = coord[0]

            if row >= 19:
                return False

        return True
    

    def is_valid_left(self) -> bool:
        for coord in self.coords:
            column = coord[1]

            if column == 0:
                return False

        return True
    

    def is_valid_right(self) -> bool:
        for coord in self.coords:
            column = coord[1]

            if column == 9:
                return False

        return True


    def remove_piece(self, map: "TileMap") -> None:
        for coord in self.coords:
            row, column = coord

            # Transforma tudo em 0
            map.matrix[row][column] = 0


    def move_down(self, map: "TileMap") -> None:
        # Se não for válido o movimento para baixo
        if not self.is_valid_down():
            return

        # Remove a posição da peça anterior
        self.remove_piece(map)

        for index, coord in enumerate(self.coords):
            row, column = coord
            
            # Atualiza as coordenadas
            self.coords[index][0] += 1

            # Preenche a próxima row
            map.matrix[row + 1][column] = self.type


    def move_left(self, map: "TileMap") -> None:
        # Se não for válido o movimento a esquerda
        if not self.is_valid_left():
            return

        # Remove a posição da peça anterior
        self.remove_piece(map)

        for index, coord in enumerate(self.coords):
            row, column = coord
            
            # Atualiza as coordenadas
            self.coords[index][1] -= 1

            # Preenche a column da esquerda
            map.matrix[row][column - 1] = self.type


    def move_right(self, map: "TileMap") -> None:
        # Se não for válido o movimento para a direita
        if not self.is_valid_right():
            return
        
        # Remove a posição da peça anterior
        self.remove_piece(map)

        for index, coord in enumerate(self.coords):
            row, column = coord
            
            # Atualiza as coordenadas
            self.coords[index][1] += 1

            # Preenche a column da direita
            map.matrix[row][column + 1] = self.type


class TileMap: 
    matrix: list[list] = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    def clear_matrix(self) -> None:
        for row in range(20):
            for column in range(10):
                self.matrix[row][column] = 0


    def add_piece(self, type: str) -> Piece:

        # Obtêm as coordenadas da peça escolhida
        for coord in pieces_coords[type]:
            row, column = coord
            self.matrix[row][column] = type

        return Piece(type ,pieces_coords[type])


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
        screen.fill(colors['bg_color'])
        pygame.draw.rect(screen, colors['bg_block_area_color'], blocks_area)

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
                    pygame.draw.rect(screen, colors[piece.type], tile)

                # Desenha a borda
                pygame.draw.rect(screen, colors['block_area_line'], tile, width=1)

        pygame.display.flip()


        # FPS
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()