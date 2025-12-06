import re
from functools import reduce

numberpattern = re.compile(r'\d+')
symbolpattern = re.compile(r'[\*\+]')

def readfile(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            numbers = (numberpattern.findall(line))
            if len(numbers) == 0:
                return lines, symbolpattern.findall(line)
            else:
                numbers = [int(s) for s in numbers]
                lines.append(numbers)

def part1(filename):
    lines, symbols = readfile(filename)
    totals = 0
    for icol in range(len(lines[0])):
        numbers = []
        for irow in range(len(lines)):
            numbers.append(lines[irow][icol])
        if symbols[icol] == '*':
            totals += reduce(lambda x, y: x * y, numbers)
        else:
            totals += sum(numbers)
    return totals

def rotate_file_left(filename):
    lines = []
    sizes = set()
    with open(filename, 'r') as file:
        for line in file:
            sizes.add(len(line))
            lines.append(line)

    symbols = symbolpattern.findall(lines[-1])[::-1]
    lines = lines[:-1]
    r_lines = []

    linelength = len(lines[0])
    for icol in range(linelength):
        rline = ''

        for irow in range(len(lines)):
            rline += lines[irow][linelength - icol - 1]

        r_lines.append(rline)
    
    # drop newlines \n
    r_lines = r_lines[1:]

    groups = []
    group = []
    for i, line in enumerate(r_lines):
        sline = line.strip()
        if len(sline) == 0:
            groups.append([int(n) for n in group])
            group = []
        else:
            group.append(sline)
        
        # trick to do last group
        if i == len(r_lines) - 1:
            groups.append([int(n) for n in group])
        

    return groups, symbols

def part2(filename):
    numbers, operations = rotate_file_left(filename)

    totals = 0
    for i, group in enumerate(numbers):
        if operations[i] == '*':
            totals += reduce(lambda x, y: x * y, group)
        else:
            totals += sum(group)

    return totals

print(part1('day6/testinput'))
print(part1('day6/input'))

print(part2('day6/testinput'))
print(part2('day6/input'))