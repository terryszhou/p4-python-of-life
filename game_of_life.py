# # IMPORT MODULES - - - - - - - - - - - - - - - - - - -
import pygame
import numpy as np
from random import choice
from sys import exit

# # BASIC VARIABLES - - - - - - - - - - - - - - - - -
pygame.init()
pygame.display.set_caption("Terry's Game of Life")
clock = pygame.time.Clock()
my_font = pygame.font.Font("fonts/Pixeltype.ttf", 50)

pause = False

class Game_Of_Life:
    def __init__(self):
        self.screen = pygame.display.set_mode((757,757))
        self.screen.fill("black")
        self.cell_width = 20
        self.cell_height = 20
        self.rows = 36
        self.cols = 36
        self.margin = 1
        self.living = choice(["red", "orange", "grey", "green", "yellow", "gold", "purple", "pink"])
        self.dead = (44,44,44)
        self.pause = False

        self.grid = np.random.randint(0, 2, size = (self.rows, self.cols)) 

    def run(self):
        self.draw_grid()
        self.update_grid()

    def draw_grid(self):
        cell_status = ""
        for row in range(1, self.rows - 1):
            for col in range(1, self.cols - 1):
                if self.grid[row][col] == 1:
                    cell_status = self.living
                else:
                    cell_status = self.dead
                pygame.draw.rect(self.screen,
                                    cell_status,
                                    [(self.margin + self.cell_width) * col + self.margin,
                                    (self.margin + self.cell_height) * row + self.margin,
                                    self.cell_width,
                                    self.cell_height])

    def update_grid(self):
        if self.pause == False:
            new_grid = self.grid.copy()
            for row in range(self.rows):
                for col in range(self.cols):
                    new_grid[row][col] = self.update_cell(row, col)
            self.grid = new_grid

    def update_cell(self, row, col):
        current_state = self.grid[row][col]
        neighbors_count = 0
        for i in range(-1,2):
            for j in range(-1,2):
                try:
                    if i == 0 and j == 0:
                        continue
                    elif self.grid[row + i, col + j]:
                        neighbors_count += 1
                except:
                    continue
        if current_state == 1:
            if neighbors_count < 2 or neighbors_count > 3:
                current_state = 0
        else:
            if neighbors_count == 3:
                current_state = 1
        return current_state

    # def update_cell(self, row, col):
    #     current_state = self.grid[row][col]
    #     neighbors = (self.grid[row - 1][column - 1], self.grid[row - 1][column], self.grid[row - 1][column + 1],
    #                 self.grid[row][column - 1], self.grid[row][column + 1], self.grid[row + 1][column - 1],
    #                 self.grid[row + 1][column], self.grid[row + 1][column + 1])
    #     try:
    #         neighbors_count = sum(neighbors)
    #     except:
    #         continue
    #     if current_state == 1: # <-- rules for living cells
    #         if neighbors_count < 2  or neighbors_count > 3:
    #             current_state = 0
    #     else: # <-- rules for dead cells
    #         if neighbors_count == 3:
    #             current_state = 1
    #     return current_state

game_of_life = Game_Of_Life()

# # MAIN GAME LOOP - - - - - - - - - - - - - - - - -
while True:
    # # EVENT CONDITIONALS - - - - - - - - - - - - - - - - -
    for event in pygame.event.get(): # <-- gets events, loops through them
        if event.type == pygame.QUIT: # <-- closes out window if event type is QUIT
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN: # <-- mark cells as living
            col = int(event.pos[0]/(game_of_life.cell_width + game_of_life.margin))
            row = int(event.pos[1]/(game_of_life.cell_height + game_of_life.margin))
            if game_of_life.grid[row][col] == 0:
                game_of_life.grid[row][col] = 1
            else:
                game_of_life.grid[row][col] = 0
            print(f"Row: {row}, Column: {col}")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: # <-- pause/unpause game
                if game_of_life.pause == False:
                    game_of_life.pause = True
                else:
                    game_of_life.pause = False
            if event.key == pygame.K_q: # <-- clear board if game is paused
                if game_of_life.pause == True:
                    for row in range(36):
                        for column in range(36):
                            game_of_life.grid[row][column] = 0

    # # UPDATE CLOCK AND DISPLAY - - - - - - - - - - - - - - - - - - -
    game_of_life.run()
    pygame.display.update()
    clock.tick(10)

# # EMERGENCY EXIT - - - - - - - - - - - - - - - - -
pygame.quit()