import pygame

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

display = pygame.display.set_mode((Width, Height))

On_Game_True = True
while On_Game_True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            On_Game_True = False
            quit()

    display.fill(cyan)

    pygame.display.flip()


