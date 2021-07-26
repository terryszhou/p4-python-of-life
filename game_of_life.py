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

pause = False

class Game_Of_Life:
    def __init__(self, screen, width=800, height=800, cell_width=20, cell_height = 20, margin=1, living="white", dead =(44,44,44)):
        self.screen = screen
        self.width = width
        self.height = height
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.margin = margin
        self.living = living
        self.dead = dead

        self.rows = 36
        self.cols = 36
        self.grid = []

    def run(self):
        self.draw_grid()

    def draw_grid(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col]:
                    pygame.draw.rect(self.screen,
                                    self.living,
                                    [(self.margin + self.cell_width) * col + self.margin,
                                    (self.margin + self.cell_height) * row + self.margin,
                                    self.cell_width,
                                    self.cell_height])
                else:
                    pygame.draw.rect(self.screen,
                                    self.dead,
                                    [(self.margin + self.cell_width) * col + self.margin,
                                    (self.margin + self.cell_height) * row + self.margin,
                                    self.cell_width,
                                    self.cell_height])


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
        if event.type == pygame.MOUSEBUTTONDOWN: # <-- mark cells as living
            column = int(event.pos[0]/(cell_width + margin))
            row = int(event.pos[1]/(cell_height + margin))
            if grid[row][column] == 0:
                grid[row][column] = 1
            else:
                grid[row][column] = 0
            # print(f"Row: {row}, Column: {column}")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # <-- pause/unpause game
                if pause == False:
                    pause = True
                else:
                    pause = False
            if event.key == pygame.K_q: # <-- clear board if game is paused
                if pause == True:
                    for row in range(36):
                        for column in range(36):
                            grid[row][column] = 0

    # # DRAW CELLS - - - - - - - - - - - - - - - - -
    new_grid = grid.copy()
    for row in range(1, 35):
        for column in range(1, 35):
            color = (44,44,44)
            cell = grid[row][column]
            neighbors = (grid[row - 1][column - 1], grid[row - 1][column], grid[row - 1][column + 1],
                        grid[row][column - 1], grid[row][column + 1], grid[row + 1][column - 1],
                        grid[row + 1][column], grid[row + 1][column + 1])
            neighbors_count = sum(neighbors)
            if pause == False: # <-- runs simulation if game is unpaused
                if grid[row][column] == 1: # <-- rules for living cells
                    color = "white"
                    if neighbors_count < 2  or neighbors_count > 3:
                        new_grid[row][column] = 0
                else: # <-- rules for dead cells
                    if neighbors_count == 3:
                        new_grid[row][column] = 1
            else: # <-- makes sure that living cells stay white even when paused
                if grid[row][column] == 1:
                    color = "white"
            pygame.draw.rect(screen,
                            color,
                            [(margin + cell_width) * column + margin,
                            (margin + cell_height) * row + margin,
                            cell_width,
                            cell_height]) # <-- pygame.draw.rect(surface, color, [left, top, width, height])

    # # UPDATE CLOCK AND DISPLAY - - - - - - - - - - - - - - - - - - -
    pygame.display.update()
    clock.tick(10)

# # EMERGENCY EXIT - - - - - - - - - - - - - - - - -
pygame.quit()