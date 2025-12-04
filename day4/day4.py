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

def part1(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append([c == '@' for c in line.strip()])
    
    grid = np.array(lines)
    count = 0
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i,j] and sum(get_adjacent_values(grid, i, j)) < 4:
                count +=1
    return count

print(part1('day4/testinput'))
print(part1('day4/input'))