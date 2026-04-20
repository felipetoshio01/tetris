from constants import PIECES_COORDS


class Piece:
    def __init__(self, map: "TileMap",type: str = "", coords: list[list[int]] = [[0, 0]]) -> None:
        self.map = map
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


    def remove_piece(self) -> None:
        for coord in self.coords:
            row, column = coord

            # Transforma tudo em 0
            self.map.matrix[row][column] = "0"


    def fix_piece(self) -> None:
        for coord in self.coords:
            row, column = coord

            self.map.matrix[row][column] += "#"


    def hit_ground(self) -> bool:
        for coord in self.coords:
            row, column = coord

            if row == 19:
                return True
            
            elif "#" in str(self.map.matrix[row + 1][column]):
                return True

        return False


    def move_down(self) -> None:
        # Se não for válido o movimento para baixo
        if not self.is_valid_down():
            return

        # Remove a posição da peça anterior
        self.remove_piece()

        for index, coord in enumerate(self.coords):
            row, column = coord
            
            # Atualiza as coordenadas
            self.coords[index][0] += 1

            # Preenche a próxima row
            self.map.matrix[row + 1][column] = self.type


    def move_left(self) -> None:
        # Se não for válido o movimento a esquerda
        if not self.is_valid_left():
            return

        # Remove a posição da peça anterior
        self.remove_piece()

        for index, coord in enumerate(self.coords):
            row, column = coord
            
            # Atualiza as coordenadas
            self.coords[index][1] -= 1

            # Preenche a column da esquerda
            self.map.matrix[row][column - 1] = self.type


    def move_right(self) -> None:
        # Se não for válido o movimento para a direita
        if not self.is_valid_right():
            return
        
        # Remove a posição da peça anterior
        self.remove_piece()

        for index, coord in enumerate(self.coords):
            row, column = coord
            
            # Atualiza as coordenadas
            self.coords[index][1] += 1

            # Preenche a column da direita
            self.map.matrix[row][column + 1] = self.type


class TileMap: 

    def __init__(self) -> None:
        self.matrix: list[list[str]] = [["0" for _ in range(10)] for _ in range(20)]
        

    def clear_matrix(self) -> None:
        for row in range(20):
            for column in range(10):
                self.matrix[row][column] = "0"

    
    def add_piece(self, type: str) -> Piece:
        # Obtêm as coordenadas da peça escolhida
        coords: list[list[int]] = [list(coord) for coord in PIECES_COORDS[type]]

        # Desenha na matrix
        for coord in coords:
            row, column = coord
            self.matrix[row][column] = type

        return Piece(self, type, coords)
