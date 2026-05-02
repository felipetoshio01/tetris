from constants import (
    PIECES_COORDS,
    PIECES_ROTATIONS,
    WALL_KICK_DATA,
    I_WALL_KICK_DATA
)
from tile_map import TileMap


class Piece:
    def __init__(self, map: TileMap, type: str) -> None:
        self.map = map
        self.type = type

        self.coords = [list(coord) for coord in PIECES_COORDS[type]]
        self.piece_rotations = PIECES_ROTATIONS[type]
        self.wall_kick_data = WALL_KICK_DATA if type != "I" else I_WALL_KICK_DATA

        self.rotation = 0
        self.row_offset = 0
        self.column_offset = 0


    def add_piece(self) -> None:
        """
        Adiciona uma nova `Piece` com o tipo especificado no `TileMap.matrix`. Os tipos devem ser **"I", "O", "S", "Z", "L"** ou **"J"**
        """

        # Desenha na matrix
        for coord in PIECES_COORDS[self.type]:
            row, column = coord
            self.map.matrix[row][column] = self.type


    def _can_move_vertical(self, moves: int) -> bool:
        """
        Determina se um movimento vertical de determinada quantidade de casas (`moves`) é válido ou não. Caso seja válido, retorna **True**, senão **False**.
        Movimentos positivos são para baixo, enquanto negativos para cima
        """

        for coord in self.coords:
            row, column = coord

            if (row + moves < 0 and moves < 0) or (row + moves > 19 and moves > 0):
                return False

            if "#" in self.map.matrix[row + moves][column]:
                return False
        
        return True


    def _can_move_horizontal(self, moves: int) -> bool:
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
        if not self._can_move_vertical(quantity):
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
        if not self._can_move_vertical(-quantity):
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
        if not self._can_move_horizontal(-quantity):
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
        if not self._can_move_horizontal(quantity):
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

        new_rotation: int = self.rotation + 1 if direction == "right" else self.rotation - 1
        
        # Obtêm a orientação
        orientation: int = new_rotation % 4

        # Obtêm as coordenadas novas, para testes
        rotation_coords: list[list[int]] = []

        for index, base_coord in enumerate(self.piece_rotations[orientation]):
            coord = [base_coord[0] + self.row_offset, base_coord[1] + self.column_offset]
            rotation_coords.append(coord)
        
        rotation_result: list[int] = self._get_rotation_kick(orientation, rotation_coords)

        # Se houve sucesso (não for lista vazia)
        if rotation_result:
            row_kick, column_kick = rotation_result

            # Adiciona o kick
            self.row_offset += row_kick
            self.column_offset += column_kick

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
            
            # Atualiza a rotação
            self.rotation = new_rotation


    def _get_rotation_kick(self, old_orientation: int, piece_coords: list[list[int]]) -> list[int]:
        """
        Retorna uma lista **[y, x]** com os valores de deslocamento extra (*Wall kick*) necessário após a rotação. Se nenhum deslocamento for bem sucedido, retorna **[ ]**
        """

        new_orientation: int = (old_orientation + 1) % 4

        wall_kick_values = self.wall_kick_data[f"{old_orientation}>{new_orientation}"]

        for value in wall_kick_values:
            row_add, column_add = value
            
            # Coordenadas de teste
            test_coords = [[coord[0] + row_add, coord[1] + column_add] for coord in piece_coords]  
         
            if self._is_coords_valid(test_coords):
                return list(value)

        return []
            
    
    def _is_coords_valid(self, coords: list[list[int]]) -> bool:
        """
        Retorna **True** se um conjunto de coordenadas é válido. Senão, retorna **False**
        """

        for coord in coords:
            row, column = coord

            # Se está fora dos limites
            if (column < 0 or column > 9) or (row < 0 or row > 19):
                return False
            
            # Se coincide com uma peça fixa
            elif "#" in self.map.matrix[row][column]:
                return False
        
        return True
