import pygame
import os 


WIDTH = 400
HEIGHT = 400
FPS = 30
x = 100
y = 100


pygame.init()
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
os.environ['Sp_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

size = [500, 500]
Screen = pygame.display.set_mode(size)
pygame.display.set_caption("Test drawings")
Screen.fill((0,0,255))
pygame.display.flip()
runGame = True # флаг выхода из цикла игры


while runGame:
    # Отслеживание события: "закрыть окно"
    for event in pygame.event.get():
        if event.type == pygame.QUIT: runGame = False


# Выход из игры: 
pygame.quit()