# # IMPORT MODULES - - - - - - - - - - - - - - - - - - -
import pygame, math
from sys import exit

pygame.init()
screen = pygame.display.set_mode((757,757))
screen.fill("grey")
pygame.display.set_caption("Terry's Game of Life")
clock = pygame.time.Clock()
my_font = pygame.font.Font("fonts/Pixeltype.ttf", 50)
game_active = True
pause = False

test_surface = pygame.Surface((200,200))
test_surface.fill("red")
test_rect = test_surface.get_rect(center = (0,300))

cell_width = 20
cell_height = 20
margin = 1

grid = []

for row in range(36):
    grid.append([])
    for column in range(36):
        grid[row].append(0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            column = int(event.pos[0]/(cell_width + margin))
            row = int(event.pos[1]/(cell_height + margin))
            if grid[row][column] == 0:
                grid[row][column] = 1
            else:
                grid[row][column] = 0
            print(f"Row: {row}, Column: {column}")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pause == False:
                    pause = True
                else:
                    pause = False
            if event.key == pygame.K_q:
                if pause == True:
                    for row in range(36):
                        for column in range(36):
                            grid[row][column] = 0

    for row in range(36):
        for column in range(36):
            color = (44,44,44)
            if grid[row][column] == 1:
                color = "white"
            pygame.draw.rect(screen,
                            color,
                            [(margin + cell_width) * column + margin,
                            (margin + cell_height) * row + margin,
                            cell_width,
                            cell_height]) # <-- pygame.draw.rect(surface, color, [left, top, width, height])

    screen.blit(test_surface, test_rect)
    if pause == False:
        test_rect.x += 5
    else:
        test_rect.x = test_rect.x

    pygame.display.update()
    clock.tick(30)
pygame.quit()