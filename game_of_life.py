# # IMPORT MODULES - - - - - - - - - - - - - - - - - - -
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((757,757))
pygame.display.set_caption("Terry's Game of Life")
clock = pygame.time.Clock()
test_font = pygame.font.Font("fonts/Pixeltype.ttf", 50)
game_active = True

cell_width = 20
cell_height = 20
margin = 1

grid = []
for row in range(36):
    grid.append([])
    for column in range(36):
        grid[row].append(0)

cell_surf = pygame.Surface((cell_width, cell_height))
cell_surf.fill("white")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_active == True:
        screen.fill("grey")
        for row in range(36):
            for column in range(36):
                pygame.draw.rect(screen, "black", [
                    (margin + cell_width) * column + margin,
                    (margin + cell_height) * row + margin,
                    cell_width,
                    cell_height
                ])




    pygame.display.update()
    clock.tick(30)
