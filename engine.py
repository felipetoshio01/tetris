from constants import PIECES_COORDS

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
        for coord in PIECES_COORDS[type]:
            row, column = coord
            self.matrix[row][column] = type

        return Piece(type, PIECES_COORDS[type])