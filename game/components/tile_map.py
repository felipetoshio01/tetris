# ================== Configurações ================== 
from settings.config import CLEAR_SOUND

class TileMap: 
    """
    Matrix 20x10 que conterá as informações para a região das peças
    """

    def __init__(self) -> None:
        self.matrix: list[list[str]] = [["0" for _ in range(10)] for _ in range(20)]
        self.complete_rows: list[int] = []


    def clear_matrix(self) -> None:
        """
        Transforma cada elemento do `TileMap.matrix` em **"0"**
        """
        
        for row in range(20):
            for column in range(10):
                self.matrix[row][column] = "0"
    

    def _is_row_complete(self, row: list[str]) -> bool:
        """
        Determina se uma `row` da `TileMap.matrix` está completa ou não
        """
        
        return "0" not in row
    

    def get_complete_rows(self) -> bool:
        """
        Adiciona o index de **rows** completas ao `TileMap.complete_rows`. Caso ele tenha obtido um **row** completa, retorna **True**, senão **False**
        """

        have_complete_rows: bool = False

        for index, row in enumerate(self.matrix):
            if self._is_row_complete(row):
                self.complete_rows.append(index)
                have_complete_rows = True

        return have_complete_rows


    def _delete_complete_rows(self) -> None:
        """
        Deleta cada **row** no `TileMap.complete_rows`
        """

        for row in self.complete_rows:
            for column in range(10):
                self.matrix[row][column] = "0"


    def _move_down_rows(self) -> None:
        """
        Move cada **row** acima de uma **row** completa para baixo no `TileMap.matrix`
        """

        new_matrix: list[list[str]] = [self.matrix[index] for index in range(20) if index not in self.complete_rows]

        needed_rows: int = 20 - len(new_matrix)

        new_rows: list[list[str]] = [["0" for _ in range(10)] for _ in range(needed_rows)]

        self.matrix = new_rows + new_matrix


    def clear_complete_rows(self) -> int:
        """
        Faz a lógica completa de limpar **rows** completas. No final, limpa a `TileMap.complete_rows`
        """
        # Número de rows sendo limpas
        number_of_rows: int = 0 

        if self.get_complete_rows():
            CLEAR_SOUND.play()

            # Pega quantas rows foram obtidas
            number_of_rows = len(self.complete_rows)
            
            self._delete_complete_rows()
            self._move_down_rows()
            self.complete_rows.clear()

        return number_of_rows
    