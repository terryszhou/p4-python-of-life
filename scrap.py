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