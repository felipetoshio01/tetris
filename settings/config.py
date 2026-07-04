import pygame


# ================== Variáveis de jogo ================== 
FAST_FALLING_SPEED: int = 4  # 1 cell a cada 4 frames


# ================== Variáveis de desenho ================== 
BORDER_WIDTH: int = 5 
BORDER_RADIUS: int = 15


# ================== Fontes ================== 
NUMBER_FONT: pygame.Font = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 15)
TITLE_FONT: pygame.Font = pygame.font.Font("fonts/Tiny5-Regular.ttf", 60)
TEXT_FONT: pygame.Font = pygame.font.Font("fonts/Jersey10-Regular.ttf", 35)


# ================== SFX ================== 
CLEAR_SOUND: pygame.mixer.Sound = pygame.mixer.Sound("music/clear_sound.wav")
CLEAR_SOUND.set_volume(0.2)
