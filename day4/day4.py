import numpy as np

def get_adjacent_values(array, x, y):
    # Define the offsets for 8 directions
    offsets = [(-1, -1), (-1, 0), (-1, 1),
               (0, -1),          (0, 1),
               (1, -1), (1, 0), (1, 1)]
    
    # Initialize a list to store adjacent values
    adjacent_values = []
    
    for dx, dy in offsets:
        nx, ny = x + dx, y + dy
        
        # Check if the new coordinates are within the array bounds
        if 0 <= nx < array.shape[0] and 0 <= ny < array.shape[1]:
            adjacent_values.append(array[nx, ny])
    
    return adjacent_values

def readgrid(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append([c == '@' for c in line.strip()])
    
    grid = np.array(lines)
    return grid 

def part1(filename):
    grid = readgrid(filename)
    count = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] and sum(get_adjacent_values(grid, i, j)) < 4:
                count +=1
    return count

def part2(filename):
    grid = readgrid(filename)
    round = 0
    count = 0
    removed = -1
    rolls = []
    while removed != 0:
        coords = []
        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                if grid[i,j] and sum(get_adjacent_values(grid, i, j)) < 4:
                    coords.append((i,j))
                    count += len(coords)
        removed = len(coords)
        rolls.append(removed)
        print(f"round {round} removed {removed}")
        for c in coords:
            grid[c] = False
        round += 1

    return sum(rolls)

# print(part1('day4/testinput'))
# print(part1('day4/input'))
print(part2('day4/testinput'))
print(part2('day4/input'))