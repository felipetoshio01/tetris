import pygame

colors: dict[str, tuple[int, int, int]] = {
    "bg_color": (27, 27, 27),
    "bg_block_area_color": (40, 40, 40),
    "block_area_line": (200, 200, 200)
}

def main() -> None:
    pygame.init()

    # ================== OBJETOS DE CRIAÇÃO ================== 
    screen: pygame.surface.Surface = pygame.display.set_mode((450, 640))
    clock: pygame.Clock = pygame.Clock()
    running: bool = True
    

    # ================== GAME LOOP ================== 
    while running:
        
        # Saída do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # ================== SURFACES ================== 
        blocks_area: pygame.Rect = pygame.Rect(25, 70, 250, 500)


        # ================== DESENHOS ==================
        screen.fill(colors['bg_color'])
        pygame.draw.rect(screen, colors['bg_block_area_color'], blocks_area)

        for y in range(20):
            for x in range(10):
                tile = pygame.Rect(x * 25 + 25, y * 25 + 70, 25, 25)
                pygame.draw.rect(screen, colors['block_area_line'], tile, width=1)

        pygame.display.flip()

        # FPS
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()