# # IMPORT MODULES - - - - - - - - - - - - - - - - - - -
import pygame
import numpy as np
from random import choice
from sys import exit

# # BASIC VARIABLES - - - - - - - - - - - - - - - - -
pygame.init()
pygame.display.set_caption("Terry's Game of Life")
clock = pygame.time.Clock()
my_font = pygame.font.Font("fonts/Pixeltype.ttf", 35)
title_font = pygame.font.Font("fonts/Pixeltype.ttf", 75)
pause = True
screen_width = 757
screen_height = 757
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill("black")

# class BG_Music:
#     def __init__(self):
#         self.bg_music = pygame.mixer.Sound("audio/dont-forget-me.mp3")
#         self.bg_music.set_volume(0.05)
#         self.paused = False

#     def play_music(self):
#         if self.paused == False:
#             self.bg_music.play()
#         else:



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

game_of_life = Game_Of_Life()

run_sim_sound = pygame.mixer.Sound("audio/run_sim.wav")
pause_sim_sound = pygame.mixer.Sound("audio/pause_sim.wav")
click_sound = pygame.mixer.Sound("audio/click.wav")
unclick_sound = pygame.mixer.Sound("audio/unclick.wav")
destroy_sound = pygame.mixer.Sound("audio/destroy.wav")

run_sim_sound.set_volume(0.03)
pause_sim_sound.set_volume(0.05)
click_sound.set_volume(0.05)
unclick_sound.set_volume(0.05)
destroy_sound.set_volume(0.05)

pause_surf = pygame.Surface((screen_width,screen_height), pygame.SRCALPHA)
pause_surf.fill((0,0,0,180))

title_message = title_font.render("TERRY'S GAME OF LIFE", False, "white")
title_message_rect = title_message.get_rect(center = (380,100))

rule_1_message = my_font.render("1. Any live cell with 2 or 3 live neighbors survives.", True, "white")
rule_2_pt_1_message = my_font.render("2. Any dead cell with exact 3 live", False, "white")
rule_2_pt_2_message = my_font.render("neighbors comes to life.", False, "white")
rule_3_message = my_font.render("3. All other cells die.", False, "white")

rule_1_rect = rule_1_message.get_rect(center = (380,200))
rule_2_pt_1_rect = rule_2_pt_1_message.get_rect(center = (380,300))
rule_2_pt_2_rect = rule_2_pt_2_message.get_rect(center = (380,330))
rule_3_rect = rule_3_message.get_rect(center = (380,430))

instruction_1 = my_font.render("<CLICK> to bring cells to life", True, "white")
instruction_2 = my_font.render("<SPACEBAR> to pause/unpause", True, "white")
instruction_3 = my_font.render("<Q>, when paused, to clear board", True, "white")
instruction_4 = my_font.render("<M> to pause/unpause music", True, "white")

instruction_1_rect = instruction_1.get_rect(center = (380,600))
instruction_2_rect = instruction_2.get_rect(center = (380,630))
instruction_3_rect = instruction_3.get_rect(center = (380,660))
instruction_4_rect = instruction_4.get_rect(center = (380,690))

bg_music = pygame.mixer.music
bg_music.load("audio/dont-forget-me.mp3")
bg_music.set_volume(0.05)
bg_music.play(-1)

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
                click_sound.play()
                game_of_life.grid[row][col] = 1
            else:
                unclick_sound.play()
                game_of_life.grid[row][col] = 0
            print(f"Row: {row}, Column: {col}")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                if bg_music.get_busy() == 1:
                    bg_music.pause()
                else:
                    bg_music.unpause()
            if event.key == pygame.K_SPACE: # <-- pause/unpause game
                if pause == False:
                    pause_sim_sound.play()
                    pause = True
                else:
                    run_sim_sound.play()
                    pause = False
            if event.key == pygame.K_q: # <-- clear board if game is paused
                if pause == True:
                    destroy_sound.play()
                    for row in range(36):
                        for column in range(36):
                            game_of_life.grid[row][column] = 0

    game_of_life.run()

    if pause == True:
        screen.blit(pause_surf, (0,0))
        screen.blit(title_message, title_message_rect)
        screen.blit(rule_1_message, rule_1_rect)
        screen.blit(rule_2_pt_1_message, rule_2_pt_1_rect)
        screen.blit(rule_2_pt_2_message, rule_2_pt_2_rect)
        screen.blit(rule_3_message, rule_3_rect)
        screen.blit(instruction_1, instruction_1_rect)
        screen.blit(instruction_2, instruction_2_rect)
        screen.blit(instruction_3, instruction_3_rect)
        screen.blit(instruction_4, instruction_4_rect)

    # # UPDATE CLOCK AND DISPLAY - - - - - - - - - - - - - - - - - - -
    pygame.display.update()
    clock.tick(10)

# # EMERGENCY EXIT - - - - - - - - - - - - - - - - -
pygame.quit()