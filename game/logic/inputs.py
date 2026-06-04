# ================== Bibliotecas ================== 
import pygame

# ================== Dados do jogo ================== 
from game.logic.game_data import game_data as game


class InputManager: 
    """
    Engloba o processamento de inputs do usuário
    """

    def handle_inputs(self) -> None:
        self._handle_touch_events()
        self._handle_hold_events()


    def _handle_touch_events(self) -> None:
        """
        Cuida dos eventos do *Game Loop*
        """
        for event in pygame.event.get():

            # Saída do jogo
            if event.type == pygame.QUIT:
                game.running = False

            # Se houver uma peça ativa, execute o movimento delas
            if game.have_active_piece:
                if event.type == pygame.KEYDOWN:              
                    # Esquerda
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        game.piece.move_left(1)

                    # Direita
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        game.piece.move_right(1)

                    # Rotaciona para a esquerda
                    if event.key == pygame.K_z:
                        game.piece.rotate("left")   
                    
                    # Rotaciona para a direita
                    if event.key == pygame.K_x:
                        game.piece.rotate("right")


    def _handle_hold_events(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            game.falling_speed = game.fast_falling_speed
            
        else:
            game.falling_speed = game.normal_falling_speed
    