# # IMPORT MODULES - - - - - - - - - - - - - - - - - - -
import pygame
from sys import exit

# # BASIC VARIABLES - - - - - - - - - - - - - - - - -
pygame.init()
screen = pygame.display.set_mode((757,757))
screen.fill("grey")
pygame.display.set_caption("Terry's Game of Life")
clock = pygame.time.Clock()
my_font = pygame.font.Font("fonts/Pixeltype.ttf", 50)
# game_active = True
pause = False

# # TESTING - - - - - - - - - - - - - - - - -
test_surface = pygame.Surface((200,200))
test_surface.fill("red")
test_rect = test_surface.get_rect(center = (0,300))

# # CELL VARIABLES - - - - - - - - - - - - - - - - -
cell_width = 20
cell_height = 20
margin = 1
grid = []
for row in range(36):
    grid.append([])
    for column in range(36):
        grid[row].append(0)

# # MAIN GAME LOOP - - - - - - - - - - - - - - - - -
while True:
    # # EVENT CONDITIONALS - - - - - - - - - - - - - - - - -
    for event in pygame.event.get(): # <-- gets events, loops through them
        if event.type == pygame.QUIT: # <-- closes out window if event type is QUIT
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN: # <-- mark squares
            column = int(event.pos[0]/(cell_width + margin))
            row = int(event.pos[1]/(cell_height + margin))
            if grid[row][column] == 0:
                grid[row][column] = 1
            else:
                grid[row][column] = 0
            print(f"Row: {row}, Column: {column}")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # <-- pause/unpause game
                if pause == False:
                    pause = True
                else:
                    pause = False
            if event.key == pygame.K_q:
                if pause == True:
                    for row in range(36): # <-- clear board if game is paused
                        for column in range(36):
                            grid[row][column] = 0

    # # DRAW CELLS - - - - - - - - - - - - - - - - -
    for row in range(35):
        for column in range(35):
            color = (44,44,44)
            cell = grid[row][column]
            neighbors = (grid[row][column + 1], grid[row][column - 1], grid[row - 1][column],
                        grid[row + 1][column], grid[row - 1][column -1], grid[row - 1][column + 1],
                        grid[row + 1][column - 1], grid[row + 1][column + 1])
            neighbors_count = sum(neighbors)
            if pause == False:
                if cell == 1:
                    color = "white"
                    if neighbors_count < 2  or neighbors_count > 3:
                        grid[row][column] = 0
                else:
                    if neighbors_count == 3:
                        grid[row][column] = 1
            else:
                if cell == 1:
                    color = "white"

            pygame.draw.rect(screen,
                            color,
                            [(margin + cell_width) * column + margin,
                            (margin + cell_height) * row + margin,
                            cell_width,
                            cell_height]) # <-- pygame.draw.rect(surface, color, [left, top, width, height])

    # # TESTING - - - - - - - - - - - - - - - - -
    # screen.blit(test_surface, test_rect)
    # if pause == False:
    #     test_rect.x += 5
    # else:
    #     test_rect.x = test_rect.x

    # # UPDATE CLOCK AND DISPLAY - - - - - - - - - - - - - - - - - - -
    pygame.display.update()
    clock.tick(30)

# # EMERGENCY EXIT - - - - - - - - - - - - - - - - -
pygame.quit()