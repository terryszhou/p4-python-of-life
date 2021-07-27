# # IMPORT MODULES - - - - - - - - - - - - - - - - - - -
import pygame
import numpy as np
from random import choice
from sys import exit

# # BASIC VARIABLES - - - - - - - - - - - - - - - - -
pygame.init()
pygame.display.set_caption("Terry's Game of Life")
clock = pygame.time.Clock()
my_font = pygame.font.Font("fonts/Pixeltype.ttf", 40)
title_font = pygame.font.Font("fonts/Pixeltype.ttf", 75)
pause = True
screen_width = 757
screen_height = 757
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill("black")

# # MAIN GAME CLASS - - - - - - - - - - - - - - - - -
class Game_Of_Life:
    def __init__(self):
        self.cell_width = 20
        self.cell_height = 20
        self.rows = 36
        self.cols = 36
        self.margin = 1
        self.living = choice(["red", "orange", "green", "gold", "cornflowerblue", "purple", "deeppink", "black"])
        self.dead = (44,44,44)
        self.game_surf = pygame.Surface((screen_width,screen_height))
        self.game_surf.fill((0,0,0))
        self.grid = np.random.randint(0,2, size = (self.rows, self.cols)) 

    def render_bg(self):
        screen.blit(self.game_surf, (0,0))

    def draw_grid(self):
        cell_status = ""
        for row in range(1, self.rows - 1):
            for col in range(1, self.cols - 1):
                if self.grid[row][col] == 1:
                    cell_status = self.living
                else:
                    cell_status = self.dead
                pygame.draw.rect(screen,
                                    cell_status,
                                    [(self.margin + self.cell_width) * col + self.margin,
                                    (self.margin + self.cell_height) * row + self.margin,
                                    self.cell_width,
                                    self.cell_height],5,4)

    def update_grid(self):
        if pause == False:
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
                except IndexError:
                    continue
        if current_state == 1:
            if neighbors_count < 2 or neighbors_count > 3:
                current_state = 0
        else:
            if neighbors_count == 3:
                current_state = 1
        return current_state

    def run(self):
        self.render_bg()
        self.draw_grid()
        self.update_grid()

# # SOUNDS & MUSIC - - - - - - - - - - - - - - - - -
class Audio:
    def __init__(self):
        self.run_sim = pygame.mixer.Sound("audio/run_sim.wav")
        self.pause_sim = pygame.mixer.Sound("audio/pause_sim.wav")
        self.click = pygame.mixer.Sound("audio/click.wav")
        self.unclick = pygame.mixer.Sound("audio/unclick.wav")
        self.destroy = pygame.mixer.Sound("audio/destroy.wav")

        self.run_sim.set_volume(0.06)
        self.pause_sim.set_volume(0.1)
        self.click.set_volume(0.1)
        self.unclick.set_volume(0.1)
        self.destroy.set_volume(0.1)

        self.bg_music = pygame.mixer.music
        self.bg_music.load("audio/dont-forget-me.mp3")
        self.bg_music.set_volume(0.1)
        self.bg_music.play(-1)

# # PAUSE SCREEN - - - - - - - - - - - - - - - - -
class Pause_Screen:
    def __init__(self):
        # self.pause == True
        self.pause_surf = pygame.Surface((screen_width,screen_height), pygame.SRCALPHA)
        self.pause_surf.fill((0,0,0,180))

        self.title = title_font.render("TERRY'S GAME OF LIFE", False, "white")
        self.title_rect = self.title.get_rect(center = (380,100))

        self.rule_1 = my_font.render("1. Any live cell with 2 or 3 live neighbors survives.", True, "white")
        self.rule_2_pt_1 = my_font.render("2. Any dead cell with exact 3 live", False, "white")
        self.rule_2_pt_2 = my_font.render("neighbors comes to life.", False, "white")
        self.rule_3 = my_font.render("3. All other cells die.", False, "white")

        self.rule_1_rect = self.rule_1.get_rect(center = (380,200))
        self.rule_2_pt_1_rect = self.rule_2_pt_1.get_rect(center = (380,300))
        self.rule_2_pt_2_rect = self.rule_2_pt_2.get_rect(center = (380,330))
        self.rule_3_rect = self.rule_3.get_rect(center = (380,430))

        self.instruction_1 = my_font.render("<CLICK> to bring cells to life", True, "white")
        self.instruction_2 = my_font.render("<SPACEBAR> to pause/unpause", True, "white")
        self.instruction_3 = my_font.render("<Q>, when paused, to clear board", True, "white")
        self.instruction_4 = my_font.render("<M> to pause/unpause music", True, "white")

        self.instruction_1_rect = self.instruction_1.get_rect(center = (380,600))
        self.instruction_2_rect = self.instruction_2.get_rect(center = (380,630))
        self.instruction_3_rect = self.instruction_3.get_rect(center = (380,660))
        self.instruction_4_rect = self.instruction_4.get_rect(center = (380,690))

    def draw_pause(self):
        if pause == True:
            screen.blit(self.pause_surf, (0,0))
            screen.blit(self.title, self.title_rect)
            screen.blit(self.rule_1, self.rule_1_rect)
            screen.blit(self.rule_2_pt_1, self.rule_2_pt_1_rect)
            screen.blit(self.rule_2_pt_2, self.rule_2_pt_2_rect)
            screen.blit(self.rule_3, self.rule_3_rect)
            screen.blit(self.instruction_1, self.instruction_1_rect)
            screen.blit(self.instruction_2, self.instruction_2_rect)
            screen.blit(self.instruction_3, self.instruction_3_rect)
            screen.blit(self.instruction_4, self.instruction_4_rect)

    def run(self):
        self.draw_pause()

# # INSTANTIATE CLASS VARIABLES - - - - - - - - - - - - - - - - -
game_of_life = Game_Of_Life()
audio = Audio()
pause_screen = Pause_Screen()

# # MAIN GAME LOOP - - - - - - - - - - - - - - - - -
while True:
    # # EVENT CONDITIONALS - - - - - - - - - - - - - - - - -
    for event in pygame.event.get(): # <-- gets events, loops through them
        if event.type == pygame.QUIT: # <-- closes out window if event type is QUIT
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN: # <-- mark cells as living or dead
            row = int(event.pos[1]/(game_of_life.cell_height + game_of_life.margin))
            col = int(event.pos[0]/(game_of_life.cell_width + game_of_life.margin))
            if game_of_life.grid[row][col] == 0:
                audio.click.play()
                game_of_life.grid[row][col] = 1
            else:
                audio.unclick.play()
                game_of_life.grid[row][col] = 0
            # print(f"Row: {row}, Column: {col}")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m: # <-- pause/unpause music
                if audio.bg_music.get_busy() == 1:
                    audio.bg_music.pause()
                else:
                    audio.bg_music.unpause()
            if event.key == pygame.K_SPACE: # <-- pause/unpause game
                if pause == False:
                    audio.pause_sim.play()
                    pause = True
                else:
                    audio.run_sim.play()
                    pause = False
            if event.key == pygame.K_q: # <-- clear board if game is paused
                if pause == True:
                    audio.destroy.play()
                    for row in range(36):
                        for column in range(36):
                            game_of_life.grid[row][column] = 0

    # # RUN GAME - - - - - - - - - - - - - - - - - - -
    game_of_life.run()
    pause_screen.run()

    # # UPDATE CLOCK AND DISPLAY - - - - - - - - - - - - - - - - - - -
    pygame.display.update()
    clock.tick(10)

# # EMERGENCY EXIT - - - - - - - - - - - - - - - - -
pygame.quit()