from constants import PIECES_COORDS, PIECES_ROTATIONS


class Piece:
    def __init__(self, map: "TileMap", type: str) -> None:
        self.map = map
        self.type = type
        self.coords = [list(coord) for coord in PIECES_COORDS[type]]
        self.piece_rotations = PIECES_ROTATIONS[type]
        self.rotation = 0
        self.row_offset = 0
        self.column_offset = 0


    def _is_valide_vertical(self, moves: int) -> bool:

        for coord in self.coords:
            row, column = coord

            if (row + moves < 0 and moves < 0) or (row + moves > 19 and moves > 0):
                return False

            if "#" in self.map.matrix[row + moves][column]:
                return False
        
        return True


    def _is_valid_horizontal(self, moves: int) -> bool:
        """
        Determina se um movimento horizontal de determinada quantidade de casas (`moves`) é válido ou não. Caso seja válido, retorna **True**, senão **False**.
        Movimentos positivos são para a direita, enquanto negativos para a esquerda
        """

        for coord in self.coords:
            row, column = coord

            if (column + moves < 0 and moves < 0) or (column + moves > 9 and moves > 0):
                return False
            
            elif "#" in self.map.matrix[row][column + moves]:
                return False

        return True


    def _remove_piece(self) -> None:
        """
        Remove a `Piece` do `TileMap.matrix`, transformando suas coordenadas em **"0"**
        """

        for coord in self.coords:
            row, column = coord

            # Transforma tudo em 0
            self.map.matrix[row][column] = "0"


    def fix_piece(self) -> None:
        """
        Transforma um `Piece` móvel numa estática, adicionando um **"#"** às suas coordenadas
        """

        for coord in self.coords:
            row, column = coord

            self.map.matrix[row][column] += "#"


    def hit_ground(self) -> bool:
        """
        Se uma `Piece` atingiu o chão do `TileMap.matrix` (**row 19**) ou se seu próximo `Piece.move_down()` atingiria uma peça estática (**#**), retorna **True**. Caso contrário, retorna **False**
        """

        for coord in self.coords:
            row, column = coord

            if row == 19:
                return True
            
            elif "#" in self.map.matrix[row + 1][column]:
                return True

        return False


    def move_down(self, quantity: int) -> None:
        """
        Move cada coordenada da `Piece` para uma **row** abaixo, se o movimento for possível
        """

        # Se não for válido o movimento para baixo
        if not self._is_valide_vertical(quantity):
            return

        # Remove a posição da peça anterior
        self._remove_piece()

        for index, coord in enumerate(self.coords):
            row, column = coord
            
            # Atualiza as coordenadas
            self.coords[index][0] += quantity

            # Preenche a próxima row
            self.map.matrix[row + quantity][column] = self.type
        
        self.row_offset += quantity


    def move_up(self, quantity: int) -> None:
        # Se não for válido o movimento para baixo
        if not self._is_valide_vertical(-quantity):
            return

        # Remove a posição da peça anterior
        self._remove_piece()

        for index, coord in enumerate(self.coords):
            row, column = coord
            
            # Atualiza as coordenadas
            self.coords[index][0] -= quantity

            # Preenche a próxima row
            self.map.matrix[row - quantity][column] = self.type
        
        self.row_offset -= quantity


    def move_left(self, quantity: int) -> None:
        """
        Move cada coordenada da `Piece` para uma **column** à esquerda, se o movimento for possível
        """

        # Se não for válido o movimento a esquerda
        if not self._is_valid_horizontal(-quantity):
            return

        # Remove a posição da peça anterior
        self._remove_piece()

        for index, coord in enumerate(self.coords):
            row, column = coord
            
            # Atualiza as coordenadas
            self.coords[index][1] -= quantity

            # Preenche a column da esquerda
            self.map.matrix[row][column - quantity] = self.type
        
        self.column_offset -= quantity


    def move_right(self, quantity: int) -> None:
        """
        Move cada coordenada da `Piece` para uma **column** à direita, se o movimento for possível
        """

        # Se não for válido o movimento para a direita
        if not self._is_valid_horizontal(quantity):
            return
        
        # Remove a posição da peça anterior
        self._remove_piece()

        for index, coord in enumerate(self.coords):
            row, column = coord
            
            # Atualiza as coordenadas
            self.coords[index][1] += quantity

            # Preenche a column da direita
            self.map.matrix[row][column + quantity] = self.type
        
        self.column_offset += quantity


    def rotate(self, direction: str) -> None:
        """
        Rotaciona a `Piece` para a `direction` desejada. O parâmetro `direction` deve ser **"right"** ou **"left"**.
        """
        if self.type == "O":
            return

        # Direita
        if direction == "right":
            self.rotation += 1

        # Esquerda
        else:
            self.rotation -= 1
        
        # Obtêm a orientação
        orientation: int = self.rotation % 4

        # Remove a peça anterior
        self._remove_piece()

        # Descoloca a peça base para sua posição
        for index, base_coord in enumerate(self.piece_rotations[orientation]):
            self.coords[index][0] = base_coord[0] + self.row_offset
            self.coords[index][1] = base_coord[1] + self.column_offset
        
        # Atualiza
        for coord in self.coords:
            row, column = coord
            self.map.matrix[row][column] = self.type

    
    def rotate_left(self) -> None:
        self.rotation -= 1
        orientation: int = self.rotation % 4
        print(orientation)


class TileMap: 
    def __init__(self) -> None:
        self.matrix: list[list[str]] = [["0" for _ in range(10)] for _ in range(20)]


    def clear_matrix(self) -> None:
        """
        Transforma cada elemento do `TileMap.matrix` em **"0"**
        """
        for row in range(20):
            for column in range(10):
                self.matrix[row][column] = "0"

    
    def add_piece(self, type: str) -> Piece:
        """
        Retorna uma nova `Piece` com o tipo especificado e adiciona ela no `TileMap.matrix`. Os tipos devem ser **"I", "O", "S", "Z", "L"** ou **"J"**
        """

        # Desenha na matrix
        for coord in PIECES_COORDS[type]:
            row, column = coord
            self.matrix[row][column] = type

        return Piece(self, type)
