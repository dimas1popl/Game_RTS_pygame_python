import pygame
import sys
import os

pygame.init()

fpsClock = pygame.time.Clock()

Width = 1600
Height = 900

display = pygame.display.set_mode((Width, Height))

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
pink = (255, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

# Позиция игрока
player_x = Width // 2
player_y = Height // 2

# Направление игрока (по умолчанию смотрит вниз)
player_direction = "down"

try:
    bg_image = pygame.image.load('images/background.png').convert_alpha()
except pygame.error as e:
    print(f"Не удалось загрузить изображение: {e}")
    pygame.quit()
    exit()

bg_rect = bg_image.get_rect()
image_width = bg_rect.width

try:
    # Загружаем анимации для всех направлений
    player_animations = {
        "down": [],
        "up": [],
        "left": [],
        "right": []
    }

    # Список файлов для каждой анимации
    animation_files = {
        "down": ['images/player_walk_down1.png', 'images/player_walk_down2.png', 'images/player_walk_down3.png'],
        "up": ['images/player_walk_up1.png', 'images/player_walk_up2.png', 'images/player_walk_up3.png'],
        "left": ['images/player_walk_left1.png', 'images/player_walk_left2.png', 'images/player_walk_left3.png'],
        "right": ['images/player_walk_right1.png', 'images/player_walk_right2.png', 'images/player_walk_right3.png']
    }

    # Загружаем все анимации
    for direction, files in animation_files.items():
        for img_file in files:
            if os.path.exists(img_file):
                image = pygame.image.load(img_file).convert()
                image.set_colorkey((255, 255, 255))
                image = image.convert_alpha()
                player_animations[direction].append(image)
            else:
                print(f"Файл не найден: {img_file}")
                # Создаем заглушку, если файл не найден
                dummy_surface = pygame.Surface((50, 100), pygame.SRCALPHA)
                if direction == "down":
                    pygame.draw.rect(dummy_surface, blue, (10, 10, 30, 80))
                elif direction == "up":
                    pygame.draw.rect(dummy_surface, green, (10, 10, 30, 80))
                elif direction == "left":
                    pygame.draw.rect(dummy_surface, red, (10, 10, 30, 80))
                elif direction == "right":
                    pygame.draw.rect(dummy_surface, yellow, (10, 10, 30, 80))
                player_animations[direction].append(dummy_surface)

except pygame.error as e:
    print(f"Error loading image: {e}")
    # Если не удалось загрузить изображения, создаем простые фигуры для отладки
    player_animations = {
        "down": [pygame.Surface((50, 100))],
        "up": [pygame.Surface((50, 100))],
        "left": [pygame.Surface((50, 100))],
        "right": [pygame.Surface((50, 100))]
    }
    for direction in player_animations:
        player_animations[direction][0].fill(blue if direction == "down" else
                                             green if direction == "up" else
                                             red if direction == "left" else
                                             yellow)

# Получаем прямоугольник изображения
image_rect = player_animations["down"][0].get_rect()
image_rect.center = (player_x, player_y)

# Скорость движения
player_speed = 1.56

# Переменные для анимации
current_frame = 0
animation_speed = 0.1
animation_counter = 0
is_moving = False

# Главный игровой цикл
On_Game_True = True
while On_Game_True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            On_Game_True = False
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                On_Game_True = False
                quit()

    keys = pygame.key.get_pressed()
    is_moving = False
    last_direction = player_direction

    # Обработка движения с изменением направления
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        if player_y > 0:
            player_y -= player_speed
            is_moving = True
            player_direction = "up"

    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        if player_y < Height - image_rect.height:
            player_y += player_speed
            is_moving = True
            player_direction = "down"

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        if player_x > 0:
            player_x -= player_speed
            is_moving = True
            player_direction = "left"

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        if player_x < Width - image_rect.width:
            player_x += player_speed
            is_moving = True
            player_direction = "right"

    # Обновление анимации
    if is_moving:
        # Если направление изменилось, сбрасываем анимацию
        if last_direction != player_direction:
            current_frame = 0
            animation_counter = 0

        animation_counter += animation_speed
        if animation_counter >= 1:
            current_frame = (current_frame + 1) % len(player_animations[player_direction])
            animation_counter = 0
    else:
        current_frame = 0  # Возвращаем к первому кадру, когда не движемся

    # Обновление позиции прямоугольника
    image_rect.center = (player_x, player_y)

    # Ограничение FPS
    fpsClock.tick(60)

    # Отрисовка
    display.fill(cyan)

    # Рисуем фон
    for x in range(0, Width, image_width):
        display.blit(bg_image, (x, 0))
        display.blit(bg_image, (x, 286))
        display.blit(bg_image, (x, 572))
        display.blit(bg_image, (x, 858))

    # Рисуем текущий кадр анимации персонажа в правильном направлении
    current_image = player_animations[player_direction][current_frame]
    display.blit(current_image, image_rect)

    pygame.display.flip()