# ================== Bibliotecas ================== 
import random

# ================== Dados do jogo ================== 
from game.logic.game_data import game_data as game

# ================== Componentes ================== 
from game.components.piece import Piece


class EventManager:
    """
    Engloba o processamento dos eventos e do estado atual do jogo
    """

    def update(self) -> None:
        """
        Atualiza todo a lógica do *Game Loop*
        """

        # Se não houver peça ativa, desenhe ela
        if not game.have_active_piece:
            piece_type: str = self._choose_piece()
            game.piece = Piece(game.game_grid, piece_type)

            # GAME OVER
            if not game.piece.is_position_valid():
                game.game_grid.clear_matrix()

            game.piece.add_piece()
            game.have_active_piece = True
        
        # Se houver uma peça ativa
        else:
            if game.frame_cont >= game.falling_speed:
                game.frame_cont = 0
                self._handle_move_down()


    def _shuffle_new_pieces(self) -> None:
        """
        Reembaralha a `Game.pieces_poll`
        """

        pieces: list[str] = ["I", "T", "O", "L", "J", "S", "Z"]
        game.pieces_poll = random.sample(pieces, 7)


    def _choose_piece(self) -> str:
        """
        Seleciona uma peça dentro do `Game.pieces_poll`. 
        Se a lista estiver vazia, será criado uma nova e escolhido um novo elemento dessa nova lista
        """

        # Se não houver mais peças, crie uma nova lista
        if not game.pieces_poll:
            self._shuffle_new_pieces()

        selected_piece: str = game.pieces_poll.pop()

        return selected_piece


    def _handle_move_down(self) -> None:
        """
        Faz o movimento da `Piece` descer dentro do `TileMap`.
        Se a `Piece` atingiu o chão ou outra peça, fixe ela (`Piece.fix_piece()`)
        """
        
        # Se a peça atingiu uma coisa
        if game.piece.hit_ground():
            game.piece.fix_piece()

            # Após fixar, limpe as linhas completas
            game.game_grid.clear_complete_rows()

            # Avisa que não tem uma peça ativa
            game.have_active_piece = False     

        # Senão, desça normal
        else:
            game.piece.move_down(1)
