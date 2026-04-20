from constants import PIECES_COORDS


class Piece:
    def __init__(self, map: "TileMap",type: str = "", coords: list[list[int]] = [[0, 0]]) -> None:
        self.map = map
        self.type = type
        self.coords = coords

    def _is_valid_down(self) -> bool:
        """
        Retorna **True** se o movimento para baixo da `Piece` for possível. Caso contrário, retorna **False**
        """

        for coord in self.coords:
            row = coord[0]

            if row >= 19:
                return False

        return True
    

    def _is_valid_left(self) -> bool:
        """
        Retorna **True** se o movimento para a esquerda da `Piece` for possível. Caso contrário, retorna **False**
        """

        for coord in self.coords:
            row, column = coord

            if column == 0:
                return False
            
            elif "#" in self.map.matrix[row][column - 1]:
                return False

        return True
    

    def _is_valid_right(self) -> bool:
        """
        Retorna **True** se o movimento para a direita da `Piece` for possível. Caso contrário, retorna **False**
        """

        for coord in self.coords:
            row, column = coord

            if column == 9:
                return False
            
            elif "#" in self.map.matrix[row][column + 1]:
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
        Transforma um `Piece` móvel numa estática, adicionando um **#** às suas coordenadas
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


    def move_down(self) -> None:
        """
        Move cada coordenada da `Piece` para uma **row** abaixo, se o movimento for possível
        """

        # Se não for válido o movimento para baixo
        if not self._is_valid_down():
            return

        # Remove a posição da peça anterior
        self._remove_piece()

        for index, coord in enumerate(self.coords):
            row, column = coord
            
            # Atualiza as coordenadas
            self.coords[index][0] += 1

            # Preenche a próxima row
            self.map.matrix[row + 1][column] = self.type


    def move_left(self) -> None:
        """
        Move cada coordenada da `Piece` para uma **column** à esquerda, se o movimento for possível
        """

        # Se não for válido o movimento a esquerda
        if not self._is_valid_left():
            return

        # Remove a posição da peça anterior
        self._remove_piece()

        for index, coord in enumerate(self.coords):
            row, column = coord
            
            # Atualiza as coordenadas
            self.coords[index][1] -= 1

            # Preenche a column da esquerda
            self.map.matrix[row][column - 1] = self.type


    def move_right(self) -> None:
        """
        Move cada coordenada da `Piece` para uma **column** à direita, se o movimento for possível
        """

        # Se não for válido o movimento para a direita
        if not self._is_valid_right():
            return
        
        # Remove a posição da peça anterior
        self._remove_piece()

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
        """
        Transforma cada elemento do `TileMap.matrix` em **"0"**
        """
        for row in range(20):
            for column in range(10):
                self.matrix[row][column] = "0"

    
    def add_piece(self, type: str) -> Piece:
        """
        Retorna uma nova `Piece` com o tipo especificado e adiciona ela no `TileMap.matrix`. Os tipos devem ser **"I", "O", "S", "Z", "L" ou "J"**
        """

        # Obtêm as coordenadas da peça escolhida
        coords: list[list[int]] = [list(coord) for coord in PIECES_COORDS[type]]

        # Desenha na matrix
        for coord in coords:
            row, column = coord
            self.matrix[row][column] = type

        return Piece(self, type, coords)
