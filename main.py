import pygame
import sys
import random

pygame.init()

fpsClock = pygame.time.Clock()

Width = 1600
Height = 900

display = pygame.display.set_mode((Width, Height))

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
pink = (255,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (255,0,255)

player_x = 0
player_y = 0

try:
    bg_image = pygame.image.load('images/background.png').convert_alpha()
except pygame.error as e:
    print(f"Не удалось загрузить изображение: {e}")
    pygame.quit()
    exit()

bg_rect = bg_image.get_rect()
image_width = bg_rect.width

try:
    image_surface = pygame.image.load("images/player.png").convert_alpha()
    image_surface.set_colorkey((255, 255, 255))
except pygame.error as e:
    print(f"Error loading image: {e}")
    sys.exit()

# Получить прямоугольник изображения для позиционирования
image_rect = image_surface.get_rect()
image_rect.topleft = (player_x, player_y)  # Начальная позиция

# Добавим скорость для более плавного движения
player_speed = 1.56

On_Game_True = True
while On_Game_True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            On_Game_True = False
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_y > 0:
            player_y -= player_speed
    if keys[pygame.K_s]:
        if player_y < Height - image_rect.height:
            player_y += player_speed
    if keys[pygame.K_a]:
        if player_x > 0:
            player_x -= player_speed
    if keys[pygame.K_d]:
        if player_x < Width - image_rect.width:
            player_x += player_speed

    # ВАЖНО: обновляем позицию прямоугольника каждый кадр!
    image_rect.topleft = (player_x, player_y)

    fpsClock.tick(60)
    display.fill(cyan)
    for x in range(0, Width, image_width):
        display.blit(bg_image, (x, 0))
        display.blit(bg_image, (x, 286))#572
        display.blit(bg_image, (x, 572))#858
        display.blit(bg_image, (x, 858))
    display.blit(image_surface, image_rect)
    pygame.display.flip()