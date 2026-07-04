# ================== Bibliotecas ================== 
import random

# ================== Dados do jogo ================== 
from game.logic.game_data import game_data as game

# ================== Componentes ================== 
from game.components.piece import Piece

# ================== Configurações ================== 
from settings.dicts import SPEEDS
from settings.config import CLEAR_SOUND


class EventManager:
    """
    Engloba o processamento dos eventos e do estado atual do jogo
    """

    def update(self) -> None:
        """
        Atualiza todo a lógica do *Game Loop*
        """

        if game.state == "game_screen":
            self._update_game()
        

    def _update_game(self):
        # Se não houver peça ativa, desenhe ela
        if not game.have_active_piece:
            piece_type: str = self._choose_piece()
            game.piece = Piece(game.game_grid, piece_type)

            # GAME OVER
            if not game.piece.is_position_valid():
                self._game_over()
                

            game.piece.add_piece()
            game.have_active_piece = True
        
        # Se houver uma peça ativa
        else:
            self._update_movement()


    def _update_movement(self) -> None:
        """
        Atualiza a posição da `Piece` quando ela deve descer ou realizar um **hard drop**
        """

        if game.hard_drop:
            self._update_fix_piece()
            game.frame_cont = 0
            game.hard_drop = False

        elif game.frame_cont >= game.falling_speed:
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
            self._update_fix_piece()

        # Senão, desça normal
        else:
            game.piece.move_down(1)
    

    def _update_fix_piece(self) -> None:
        """
        Faz a lógica necessária para fixar uma peça

        - Fixar
        - Limpar (se houver) **rows** limpas
        - Atualizar (se necessário) o **score**
        - Atualizar (se necessário) a velocidade
        """

        game.piece.fix_piece()

        if game.game_grid.get_complete_rows():
            # Após fixar, limpe as linhas completas a aumente o contador
            rows_cleared = game.game_grid.clear_complete_rows()

            CLEAR_SOUND.play()

            game.rows_cleared += rows_cleared
            self._update_score(rows_cleared)

            # Mude, a velocidade
            self._update_speed()

        # Avisa que não tem uma peça ativa
        game.have_active_piece = False


    def _update_speed(self) -> None:
        """
        Atualiza da velocidade de queda da `Piece`
        """

        level = game.get_level()

        if level not in SPEEDS:
            return

        else:
            game.normal_falling_speed = SPEEDS[level]
    

    def _update_score(self, rows_cleared: int) -> None:
        """
        Atualiza a pontuação conforme a quantidade de **rows** limpas (`rows_cleared`)
        """

        level: int = game.get_level()
        
        if rows_cleared == 0:
            return
        
        elif rows_cleared == 1:
            game.score += 40 * (level + 1)
        
        elif rows_cleared == 2:
            game.score += 100 * (level + 1)
        
        elif rows_cleared == 3:
            game.score += 300 * (level + 1)
        
        elif rows_cleared >= 4:
            game.score += 1200 * (level + 1)
    

    def _game_over(self) -> None:
        """
        Faz a lógica necessária após um Game Over
        - Limpar a tela
        - Reiniciar as contagens de **score**, **rows** limpas e **score**
        """

        # Limpa o grid
        game.game_grid.clear_matrix()

        # Reinicia a contagem de rows
        game.rows_cleared = 0

        # Limpa o score
        game.score = 0
        
        # Altera a velocidade para o início
        self._update_speed()
