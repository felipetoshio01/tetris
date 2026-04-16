import pygame

colors: dict[str, tuple[int, int, int]] = {
    "bg_color": (255, 255, 255)
}

def main() -> None:
    pygame.init()

    # ================== OBJETOS DE CRIAÇÃO ================== 
    screen: pygame.surface.Surface = pygame.display.set_mode((320, 640))
    clock: pygame.Clock = pygame.Clock()
    running: bool = True
    

    # ================== GAME LOOP ================== 
    while running:
        
        # Saída do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # ================== DESENHOS ==================
        screen.fill(colors['bg_color'])

        pygame.display.flip()

        # FPS
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()