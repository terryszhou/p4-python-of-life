'''
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
'''
'''
# for row in range(1, 35):
#     for column in range(1, 35):
#         color = (44,44,44)
#         cell = grid[row][column]
#         neighbors = (grid[row - 1][column - 1], grid[row - 1][column], grid[row - 1][column + 1],
#                     grid[row][column - 1], grid[row][column + 1], grid[row + 1][column - 1],
#                     grid[row + 1][column], grid[row + 1][column + 1])
#         neighbors_count = sum(neighbors)
#         if pause == False: # <-- runs simulation if game is unpaused
#             if grid[row][column] == 1: # <-- rules for living cells
#                 color = "white"
#                 if neighbors_count < 2  or neighbors_count > 3:
#                     grid[row][column] = 0
#             else: # <-- rules for dead cells
#                 if neighbors_count == 3:
#                     grid[row][column] = 1
#         else: # <-- makes sure that living cells stay white even when paused
#             if grid[row][column] == 1:
#                 color = "white"
#         pygame.draw.rect(screen,
#                         color,
#                         [(margin + cell_width) * column + margin,
#                         (margin + cell_height) * row + margin,
#                         cell_width,
#                         cell_height]) # <-- pygame.draw.rect(surface, color, [left, top, width, height])
'''

'''
# # TESTING - - - - - - - - - - - - - - - - -
test_surface = pygame.Surface((200,200))
test_surface.fill("red")
test_rect = test_surface.get_rect(center = (0,300))

# screen.blit(test_surface, test_rect)
# if pause == False:
#     test_rect.x += 5
# else:
#     test_rect.x = test_rect.x
'''

'''
neighbors = []
if row - 1 >= 0 and column + 1 <= 36:
    neighbors.append(grid[row - 1][column + 1])
if row + 1 <= 36 and column + 1 <= 36:
    neighbors.append(grid[row + 1][column + 1])
if row + 1 <= 36 and column - 1 >= 0:
    neighbors.append(grid[row + 1][column - 1])
if row - 1 >= 0 and column - 1 >= 0:
    neighbors.append(grid[row - 1][column - 1])
if column + 1 <= 36:
    neighbors.append(grid[row][column + 1])
if row + 1 <= 26:
    neighbors.append(grid[row + 1][column])
if column - 1 >= 0:
    neighbors.append(grid[row][column - 1])
if row - 1 >= 0:
    neighbors.append(grid[row - 1][column])
'''

'''
for row in range(36):
    for column in range(36):
        color = (44,44,44)
        if grid[row][column] == 1:
            neighbor_count = 0
            color = "white"
            if grid[row][column + 1] == 1: # <-- neighbor east
                neighbor_count += 1
            if grid[row][column - 1] == 1: # <-- neighbor west
                neighbor_count += 1
            if grid[row - 1][column] == 1: # <-- neighbor north
                neighbor_count += 1
            if grid[row + 1][column] == 1: # <-- neighbor south
                neighbor_count += 1
            if grid[row - 1][column -1 ] == 1: # <-- neighbor northwest
                neighbor_count += 1
            if grid[row - 1][column + 1] == 1: # <-- neighbor northeast
                neighbor_count += 1
            if grid[row + 1][column - 1] == 1: # <-- neighbor southwest
                neighbor_count += 1
            if grid[row + 1][column + 1] == 1: # <-- neighbor southeast
                neighbor_count += 1
            if pause == False: # <-- kills cells if game is unpaused
                if neighbor_count <= 1 or neighbor_count >= 4:
                    grid[row][column] = 0
                else: grid[row][column] = 1
        pygame.draw.rect(screen,
                        color,
                        [(margin + cell_width) * column + margin,
                        (margin + cell_height) * row + margin,
                        cell_width,
                        cell_height]) # <-- pygame.draw.rect(surface, color, [left, top, width, height])
'''

'''
for row in range(36):
    for column in range(36):
        color = (44,44,44)
        if grid[row][column] == 1 or 0:
            neighbor_count = 0
            if grid[row][column + 1] == 1: # <-- neighbor east
                neighbor_count += 1
            if grid[row][column - 1] == 1: # <-- neighbor west
                neighbor_count += 1
            if grid[row - 1][column] == 1: # <-- neighbor north
                neighbor_count += 1
            if grid[row + 1][column] == 1: # <-- neighbor south
                neighbor_count += 1
            if grid[row - 1][column -1 ] == 1: # <-- neighbor northwest
                neighbor_count += 1
            if grid[row - 1][column + 1] == 1: # <-- neighbor northeast
                neighbor_count += 1
            if grid[row + 1][column - 1] == 1: # <-- neighbor southwest
                neighbor_count += 1
            if grid[row + 1][column + 1] == 1: # <-- neighbor southeast
                neighbor_count += 1
            if pause == False: # <-- kills cells if game is unpaused
                if grid[row][column] == 1:
                    color = "white"
                    if neighbor_count <= 1 or neighbor_count >= 4:
                        grid[row][column] = 0
                    else: grid[row][column] = 1
                elif grid[row][column] == 0:
                    if neighbor_count == 3:
                        grid[row][column] = 1
                        print(grid[row][column])
        pygame.draw.rect(screen,
                        color,
                        [(margin + cell_width) * column + margin,
                        (margin + cell_height) * row + margin,
                        cell_width,
                        cell_height]) # <-- pygame.draw.rect(surface, color, [left, top, width, height])
'''