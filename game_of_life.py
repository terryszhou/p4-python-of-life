# # IMPORT MODULES - - - - - - - - - - - - - - - - - - -
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Terry's Game of Life")
clock = pygame.time.Clock()
test_font = pygame.font.Font("fonts/Pixeltype.ttf", 50)
game_active = True

cell_width = 20
cell_height = 20
margin = 5

grid = []
for column in range(10):
    grid.append(0)

cell_surf = pygame.Surface((cell_width, cell_height))
cell_surf.fill("white")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for column in range(10):
        pygame.draw.rect(screen, "white", [(margin + cell_width) * column + margin, margin + 0, cell_width, cell_height])




    pygame.display.update()
    clock.tick(30)
