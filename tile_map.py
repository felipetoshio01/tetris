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
                