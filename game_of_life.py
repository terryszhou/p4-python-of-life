# # IMPORT MODULES - - - - - - - - - - - - - - - - - - -
import pygame as py
import numpy as np
from sys import exit

# # BASIC VARIABLES - - - - - - - - - - - - - - - - -
py.init()
py.display.set_caption("Terry's Game of Life")
screen_width = 736
screen_height = 736
screen = py.display.set_mode((screen_width,screen_height))
screen.fill("black")
clock = py.time.Clock()
my_font = py.font.Font("fonts/Pixeltype.ttf", 40)
title_font = py.font.Font("fonts/Pixeltype.ttf", 75)
pause = True
generation = 0

# # DEFAULT RULESET STATUSES - - - - - - - - - - - - - - - - -
gol_rules = True # <-- Game of Life
lwd_rules = False # <-- Life Without Death
mz_rules = False # <-- Maze
hl_rules = False # <-- High Life

# # MAIN GAME CLASS - - - - - - - - - - - - - - - - -
class Game_Of_Life:
    def __init__(self):
        self.cell_width = 15
        self.cell_height = 15
        self.rows = 46
        self.cols = 46
        self.margin = 1
        self.living = "cornflowerblue"
        self.dead = (44,44,44)
        self.game_surf = py.Surface((screen_width,screen_height))
        self.game_surf.fill((0,0,0))
        self.grid = np.random.randint(0,2, size = (self.rows, self.cols))
        self.midpoint = int(self.rows/2)

    def render_bg(self):
        screen.blit(self.game_surf, (0,0))

    def draw_grid(self): # <-- draws grid of cells on screen variable
        cell_status = ""
        for row in range(1, self.rows - 1):
            for col in range(1, self.cols - 1):
                if self.grid[row][col] == 1:
                    cell_status = self.living
                    if gol_rules == True: # <-- changes cell color based on ruleset
                        self.living = "cornflowerblue"
                    elif lwd_rules == True:
                        self.living = "red"
                    elif mz_rules == True:
                        self.living = "purple"
                    elif hl_rules == True:
                        self.living = "gold"
                else:
                    cell_status = self.dead
                py.draw.rect(screen, # <-- surface for drawing
                            cell_status, # <-- color for drawing
                            [(self.margin + self.cell_width) * col + self.margin, # <-- rect left
                            (self.margin + self.cell_height) * row + self.margin, # <-- rect top
                            self.cell_width, # <-- rect width
                            self.cell_height],5,4) # <-- rect height, line width, border radius

    def update_grid(self): # <-- makes a grid copy, calculates the shape of the next grid, merges the two
        if pause == False:
            new_grid = self.grid.copy()
            for row in range(self.rows):
                for col in range(self.cols):
                    new_grid[row][col] = self.update_cell(row, col)
            self.grid = new_grid

    def update_cell(self, row, col): # <-- updates an individual cell in the grid copy, returns 1 or 0 (living or dead)
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
        if gol_rules == True: # <-- Game of Life rules
            if current_state == 1:
                if neighbors_count < 2 or neighbors_count > 3:
                    current_state = 0
            else:
                if neighbors_count == 3:
                    current_state = 1
            return current_state
        elif lwd_rules == True: # <-- Life Without Death rules
            if current_state == 0:
                if neighbors_count == 3:
                    current_state = 1
            return current_state
        elif mz_rules == True: # <-- Maze rules
            if current_state == 1:
                if neighbors_count < 1 or neighbors_count > 5:
                    current_state = 0
            else: 
                if neighbors_count == 3:
                    current_state = 1
            return current_state
        elif hl_rules == True: # <-- High Life rules
            if current_state == 1:
                if neighbors_count < 2 or neighbors_count > 3:
                    current_state = 0
            else:
                if neighbors_count in (3,6):
                    current_state = 1
            return current_state

    def spawn_glider(self):
        self.grid[5][7] = 1
        self.grid[6][7] = 1
        self.grid[7][7] = 1
        self.grid[7][6] = 1
        self.grid[6][5] = 1

    def spawn_beacon(self):
        self.grid[self.midpoint - 3][self.midpoint - 2] = 1
        self.grid[self.midpoint - 3][self.midpoint - 3] = 1
        self.grid[self.midpoint - 2][self.midpoint - 3] = 1
        self.grid[self.midpoint - 1][self.midpoint] = 1
        self.grid[self.midpoint][self.midpoint] = 1
        self.grid[self.midpoint][self.midpoint - 1] = 1

    def spawn_hive(self):
        self.grid[self.midpoint - 3][self.midpoint - 2] = 1
        self.grid[self.midpoint - 3][self.midpoint - 1] = 1
        self.grid[self.midpoint - 2][self.midpoint - 2] = 1
        self.grid[self.midpoint - 2][self.midpoint - 1] = 1
        self.grid[self.midpoint - 1][self.midpoint - 2] = 1
        self.grid[self.midpoint - 1][self.midpoint - 1] = 1

    def spawn_replicator(self):
        self.grid[self.midpoint - 3][self.midpoint - 2] = 1
        self.grid[self.midpoint - 3][self.midpoint - 1] = 1
        self.grid[self.midpoint - 3][self.midpoint] = 1
        self.grid[self.midpoint - 2][self.midpoint - 3] = 1
        self.grid[self.midpoint - 2][self.midpoint] = 1
        self.grid[self.midpoint - 1][self.midpoint - 4] = 1
        self.grid[self.midpoint - 1][self.midpoint] = 1
        self.grid[self.midpoint][self.midpoint - 4] = 1
        self.grid[self.midpoint][self.midpoint - 1] = 1
        self.grid[self.midpoint + 1][self.midpoint - 4] = 1
        self.grid[self.midpoint + 1][self.midpoint - 3] = 1
        self.grid[self.midpoint + 1][self.midpoint - 2] = 1

    def spawn_gosper_gun(self):
        self.grid[6][4] = 1  
        self.grid[6][5] = 1        
        self.grid[7][5] = 1       
        self.grid[7][4] = 1        
        self.grid[7][14] = 1
        self.grid[6][14] = 1
        self.grid[8][14] = 1
        self.grid[5][15] = 1
        self.grid[9][15] = 1
        self.grid[4][16] = 1
        self.grid[4][17] = 1
        self.grid[10][16] = 1
        self.grid[10][17] = 1
        self.grid[9][19] = 1
        self.grid[8][20] = 1
        self.grid[7][20] = 1
        self.grid[6][20] = 1
        self.grid[5][19] = 1
        self.grid[7][18] = 1
        self.grid[7][21] = 1
        self.grid[6][24] = 1
        self.grid[5][24] = 1
        self.grid[4][24] = 1
        self.grid[4][25] = 1
        self.grid[5][25] = 1
        self.grid[6][25] = 1
        self.grid[3][26] = 1
        self.grid[7][26] = 1
        self.grid[7][28] = 1
        self.grid[8][28] = 1
        self.grid[3][28] = 1
        self.grid[2][28] = 1
        self.grid[4][38] = 1
        self.grid[4][39] = 1
        self.grid[5][39] = 1
        self.grid[5][38] = 1

    def spawn_random(self):
        self.grid = np.random.randint(0,2, size = (self.rows, self.cols))

    def run(self): # <-- runs functions above
        self.render_bg()
        self.draw_grid()
        self.update_grid()

# # SOUNDS & MUSIC CLASS - - - - - - - - - - - - - - - - -
class Audio:
    def __init__(self):
        self.run_sim = py.mixer.Sound("audio/run_sim.wav")
        self.pause_sim = py.mixer.Sound("audio/pause_sim.wav")
        self.click = py.mixer.Sound("audio/click.wav")
        self.unclick = py.mixer.Sound("audio/unclick.wav")
        self.destroy = py.mixer.Sound("audio/destroy.wav")
        self.switch_mode = py.mixer.Sound("audio/switch_mode.wav")
        self.spawn = py.mixer.Sound("audio/spawn.wav")

        self.volume_list = []
        for x in [self.run_sim, self.pause_sim, self.click, self.unclick, self.destroy, self.switch_mode, self.spawn]:
            def res(x): return x.set_volume(0.1)
            self.volume_list.append(res(x))

        self.bg_music = py.mixer.music
        self.bg_music.load("audio/dont-forget-me.mp3")
        self.bg_music.set_volume(0.1)
        self.bg_music.play(-1) # <-- autoplays background music on game load

# # PAUSE SCREEN CLASS - - - - - - - - - - - - - - - - -
class Pause_Screen:
    def __init__(self):
        self.pause_surf = py.Surface((screen_width,screen_height), py.SRCALPHA)
        self.pause_surf.fill((0,0,0,180))

        # # GAME OF LIFE DISPLAY - - - - - - - - - - - - - - -
        self.gol_title = title_font.render("TERRY'S GAME OF LIFE", False, "cornflowerblue")
        self.gol_rule_1 = my_font.render("1. Any living cell with 2 or 3 living neighbors survives.", True, "white")
        self.gol_rule_2_pt_1 = my_font.render("2. Any dead cell with exactly 3 living", False, "white")
        self.gol_rule_2_pt_2 = my_font.render("neighbors comes to life.", False, "white")
        self.gol_rule_3 = my_font.render("3. All other cells die.", False, "white")

        self.gol_title_rect = self.gol_title.get_rect(center = (screen_width/2, screen_height/7))
        self.gol_rule_1_rect = self.gol_rule_1.get_rect(center = (screen_width/2, screen_height/(7/2)))
        self.gol_rule_2_pt_1_rect = self.gol_rule_2_pt_1.get_rect(center = (screen_width/2, screen_height/(7/2.8)))
        self.gol_rule_2_pt_2_rect = self.gol_rule_2_pt_2.get_rect(center = (screen_width/2, screen_height/(7/3.2)))
        self.gol_rule_3_rect = self.gol_rule_3.get_rect(center = (screen_width/2, screen_height/(7/4)))

        # # LIFE WITHOUT DEATH DISPLAY - - - - - - - - - - - - - - -
        self.lwd_title = title_font.render("TERRY'S LIFE WITHOUT DEATH", False, "red")
        self.lwd_rule_1 = my_font.render("1. Cells do not die.", True, "white")
        
        self.lwd_title_rect = self.lwd_title.get_rect(center = (screen_width/2, screen_height/7))
        self.lwd_rule_1_rect = self.lwd_rule_1.get_rect(center = (screen_width/2, screen_height/(7/2)))

        # # MAZE DISPLAY - - - - - - - - - - - - - - -
        self.mz_title = title_font.render("TERRY'S MAZE", False, "purple")
        self.mz_rule_1 = my_font.render("1. Any living cell with 2, 3, or 4 living neighbors survives.", True, "white")

        self.mz_title_rect = self.mz_title.get_rect(center = (screen_width/2, screen_height/7))
        self.mz_rule_1_rect = self.mz_rule_1.get_rect(center = (screen_width/2, screen_height/(7/2)))

        # # HIGH LIFE DISPLAY
        self.hl_title = title_font.render("TERRY'S HIGH LIFE", False, "gold")
        self.hl_rule_2_pt_1 = my_font.render("2. Any dead cell with 3 or 6 living", False, "white")

        self.hl_title_rect = self.hl_title.get_rect(center = (screen_width/2, screen_height/7))
        self.h1_rule_2_pt_1_rect = self.hl_rule_2_pt_1.get_rect(center = (screen_width/2, screen_height/(7/2.8)))

        # # GAME INSTRUCTIONS - - - - - - - - - - - - - - -
        self.inst_1 = my_font.render("<CLICK> --- resurrect/kill cells", True, "white")
        self.inst_2 = my_font.render("<SPACEBAR> --- (un)pause simulation", True, "white")
        self.inst_3 = my_font.render("<M> --- (un)pause music", True, "white")
        self.inst_4 = my_font.render("<C> --- clear board", True, "white")
        self.inst_5 = my_font.render("<ARROW KEYS> --- change rulesets", True, "white")
        self.inst_6 = my_font.render("Try <G>, <B>, <H>, <R>, and <Q>!", True, "white")

        self.inst_1_rect = self.inst_1.get_rect(center = (screen_width/2, screen_height/(7/5)))
        self.inst_2_rect = self.inst_2.get_rect(center = (screen_width/2, screen_height/(7/5.3)))
        self.inst_3_rect = self.inst_3.get_rect(center = (screen_width/2, screen_height/(7/5.6)))
        self.inst_4_rect = self.inst_4.get_rect(center = (screen_width/2, screen_height/(7/5.9)))
        self.inst_5_rect = self.inst_5.get_rect(center = (screen_width/2, screen_height/(7/6.2)))
        self.inst_6_rect = self.inst_6.get_rect(center = (screen_width/2, screen_height/(7/6.5)))

    def draw_pause(self): # <-- draws variables above if game is paused.
        if pause == True:
            screen.blit(self.pause_surf, (0,0))
            screen.blit(self.inst_1, self.inst_1_rect)
            screen.blit(self.inst_2, self.inst_2_rect)
            screen.blit(self.inst_3, self.inst_3_rect)
            screen.blit(self.inst_4, self.inst_4_rect)
            screen.blit(self.inst_5, self.inst_5_rect)
            screen.blit(self.inst_6, self.inst_6_rect)
            if gol_rules == True:
                screen.blit(self.gol_title, self.gol_title_rect)
                screen.blit(self.gol_rule_1, self.gol_rule_1_rect)
                screen.blit(self.gol_rule_2_pt_1, self.gol_rule_2_pt_1_rect)
                screen.blit(self.gol_rule_2_pt_2, self.gol_rule_2_pt_2_rect)
                screen.blit(self.gol_rule_3, self.gol_rule_3_rect)
            elif lwd_rules == True:
                screen.blit(self.lwd_title, self.lwd_title_rect)
                screen.blit(self.lwd_rule_1, self.lwd_rule_1_rect)
                screen.blit(self.gol_rule_2_pt_1, self.gol_rule_2_pt_1_rect)
                screen.blit(self.gol_rule_2_pt_2, self.gol_rule_2_pt_2_rect)
            elif mz_rules == True:
                screen.blit(self.mz_title, self.mz_title_rect)
                screen.blit(self.mz_rule_1, self.mz_rule_1_rect)
                screen.blit(self.gol_rule_2_pt_1, self.gol_rule_2_pt_1_rect)
                screen.blit(self.gol_rule_2_pt_2, self.gol_rule_2_pt_2_rect)
                screen.blit(self.gol_rule_3, self.gol_rule_3_rect)
            elif hl_rules == True:
                screen.blit(self.hl_title, self.hl_title_rect)
                screen.blit(self.gol_rule_1, self.gol_rule_1_rect)
                screen.blit(self.hl_rule_2_pt_1, self.h1_rule_2_pt_1_rect)
                screen.blit(self.gol_rule_2_pt_2, self.gol_rule_2_pt_2_rect)
                screen.blit(self.gol_rule_3, self.gol_rule_3_rect)

    def run(self):
        self.draw_pause()

# # INSTANTIATE CLASS VARIABLES - - - - - - - - - - - - - - - - -
game_of_life = Game_Of_Life()
audio = Audio()
pause_screen = Pause_Screen()

# # GENERATION TIMER DISPLAY - - - - - - - - - - - - - - - - -
def display_generation():
    global generation
    generation_surf = my_font.render(f"{generation}", False, "white")
    generation_rect = generation_surf.get_rect(center = (screen_width/(1.05),screen_height/(1.05)))
    screen.blit(generation_surf, generation_rect)
    if pause == False:
        return int(clock.tick(10)/100)
    else:
        return 0

# # MAIN GAME LOOP - - - - - - - - - - - - - - - - -
while True:
    # # EVENT CONDITIONALS - - - - - - - - - - - - - - - - -
    for e in py.event.get(): # <-- gets game events, loops through them
        if e.type == py.QUIT: # <-- closes out window if event type is QUIT
            py.quit()
            exit()
        if e.type == py.MOUSEBUTTONDOWN: # <-- marks cells as living or dead
            if e.button == 1:
                row = int(e.pos[1]/(game_of_life.cell_height + game_of_life.margin))
                col = int(e.pos[0]/(game_of_life.cell_width + game_of_life.margin))
                if game_of_life.grid[row][col] == 0:
                    audio.click.play()
                    game_of_life.grid[row][col] = 1
                else:
                    audio.unclick.play()
                    game_of_life.grid[row][col] = 0
                print(f"Row: {row}, Column: {col}")
        if e.type == py.KEYDOWN:
            if e.key == py.K_m: # <-- pause/unpause music
                if audio.bg_music.get_busy() == 1:
                    audio.bg_music.pause()
                else:
                    audio.bg_music.unpause()
            if e.key == py.K_SPACE: # <-- pause/unpause game
                audio.pause_sim.play()
                if pause == False:
                    pause = True
                else:
                    pause = False
            if e.key == py.K_c: # <-- clear board if game is paused
                audio.destroy.play()
                generation = 0
                for row in range(game_of_life.rows):
                    for col in range(game_of_life.cols):
                        game_of_life.grid[row][col] = 0
            if e.key in (py.K_UP, py.K_LEFT, py.K_RIGHT, py.K_DOWN):
                audio.switch_mode.play()
                generation = 0
                if e.key == py.K_UP: # <-- switch to Game of Life rules
                    lwd_rules = mz_rules = hl_rules = False
                    gol_rules = True
                if e.key == py.K_LEFT: # <-- switch to Life Without Death rules
                    gol_rules = mz_rules = hl_rules = False
                    lwd_rules = True
                if e.key == py.K_RIGHT: # <-- switch to Maze rules
                    gol_rules = lwd_rules = hl_rules = False
                    mz_rules = True
                if e.key == py.K_DOWN: # <-- switch to High Life rules
                    gol_rules = lwd_rules = mz_rules = False
                    hl_rules = True
            if e.key in (py.K_g, py.K_b, py.K_h, py.K_r, py.K_q, py.K_3):
                audio.spawn.play()
                if e.key == py.K_g: game_of_life.spawn_glider() # <-- spawns glider
                if e.key == py.K_b: game_of_life.spawn_beacon() # <-- spawns blinker
                if e.key == py.K_h: game_of_life.spawn_hive() # <-- spawns hive
                if e.key == py.K_r: game_of_life.spawn_replicator() # <-- spawns hive
                if e.key == py.K_3: game_of_life.spawn_gosper_gun() # <-- spawns gosper glider gun
                if e.key == py.K_q: game_of_life.spawn_random() # <-- spawns random grid

    # # RUN SIMULATION - - - - - - - - - - - - - - - - - - -
    game_of_life.run()
    pause_screen.run()
    generation += display_generation()

    # # UPDATE CLOCK AND DISPLAY - - - - - - - - - - - - - - - - - - -
    py.display.flip()
    clock.tick(60)

# # EMERGENCY EXIT - - - - - - - - - - - - - - - - -
py.quit()