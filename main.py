import pygame
import sys

pygame.init()

fpsClock = pygame.time.Clock()

Width = 1600
Height = 900

display = pygame.display.set_mode((Width, Height))

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
pink = (255, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)

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
    player_images = []
    player_list = ['images/player_walk_down1.png', 'images/player_walk_down2.png', 'images/player_walk_down3.png']
    for img in player_list:
        image = pygame.image.load(img).convert()  # Сначала конвертируем
        image.set_colorkey((255, 255, 255))  # Убираем белый фон
        image = image.convert_alpha()  # Затем делаем прозрачным
        player_images.append(image)
except pygame.error as e:
    print(f"Error loading image: {e}")
    sys.exit()

# Получить прямоугольник изображения для позиционирования
image_rect = player_images[0].get_rect()
image_rect.topleft = (player_x, player_y)  # Начальная позиция

# Добавим скорость для более плавного движения
player_speed = 1.56

# Переменные для анимации
current_frame = 0
animation_speed = 0.1  # Скорость анимации
animation_counter = 0
is_moving = False

On_Game_True = True
while On_Game_True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            On_Game_True = False
            quit()

    keys = pygame.key.get_pressed()
    is_moving = False

    if keys[pygame.K_w]:
        if player_y > 0:
            player_y -= player_speed
            is_moving = True
    if keys[pygame.K_s]:
        if player_y < Height - image_rect.height:
            player_y += player_speed
            is_moving = True
    if keys[pygame.K_a]:
        if player_x > 0:
            player_x -= player_speed
            is_moving = True
    if keys[pygame.K_d]:
        if player_x < Width - image_rect.width:
            player_x += player_speed
            is_moving = True

    # Обновление анимации
    if is_moving:
        animation_counter += animation_speed
        if animation_counter >= 1:
            current_frame = (current_frame + 1) % len(player_images)
            animation_counter = 0
    else:
        current_frame = 0  # Возвращаем к первому кадру, когда не движемся

    image_rect.topleft = (player_x, player_y)

    fpsClock.tick(60)
    display.fill(cyan)

    # Рисуем фон
    for x in range(0, Width, image_width):
        display.blit(bg_image, (x, 0))
        display.blit(bg_image, (x, 286))
        display.blit(bg_image, (x, 572))
        display.blit(bg_image, (x, 858))

    # Рисуем текущий кадр анимации персонажа
    display.blit(player_images[current_frame], image_rect)

    pygame.display.flip()