import pygame
import sys
import random

pygame.init()

Width = 1600
Height = 900

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
pink = (255,0,255)
yellow = (255,255,0)
cyan = (0,255,255)
magenta = (255,0,255)

try:
    image_surface = pygame.image.load("player.png").convert_alpha() #Использовать конверт () для непрозрачных изображений
except pygame.error as e:
    print(f"Error loading image: {e}")
    sys.exit()

# Получить прямоугольник изображения для позиционирования
# Это удобный способ управления координатами изображения и столкновениями
image_rect = image_surface.get_rect()
image_rect.topleft = (0, 0)  # Позиция в верхнем левом углу



display = pygame.display.set_mode((Width, Height))

On_Game_True = True
while On_Game_True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            On_Game_True = False
            quit()

    display.fill(cyan)



    display.blit(image_surface, image_rect)

    pygame.display.flip()


