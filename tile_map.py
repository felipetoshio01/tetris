class TileMap: 
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
        
        for item in row:
            if item == "0":
                return False
        
        return True
    

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


    def delete_complete_rows(self) -> None:
        """
        Deleta cada **row** no `TileMap.complete_rows`
        """

        for row in self.complete_rows:
            for column in range(10):
                self.matrix[row][column] = "0"


    def move_down_rows(self) -> None:
        """
        Move cada **row** acima de uma **row** completa para baixo no `TileMap.matrix`. No final, limpa a lista `TileMap.complete_rows`
        """

        for cleared_row in self.complete_rows:

            for index, row in enumerate(reversed(self.matrix)):
                row_index = 19 - index

                if row_index >= cleared_row:
                    continue

                self.matrix[row_index + 1] = row.copy()

        self.complete_rows.clear()