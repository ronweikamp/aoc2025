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

print(part1('day6/testinput'))
print(part1('day6/input'))