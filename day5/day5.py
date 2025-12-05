def parserange(line):
    start, end = line.split('-')
    return range(int(start), int(end) + 1)

def readfile(filename):
    lines = []
    rangestate = True
    ranges = []
    ingredients = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if len(line) == 0:
                rangestate = False
                continue
            if rangestate:
                ranges.append(parserange(line))
            else:
                ingredients.append(int(line))
    
    return ranges, ingredients

def part1(filename):
    ranges, ingredients = readfile(filename)
    freshi = []
    for i in ingredients:
        if any(i in r for r in ranges):
            freshi.append(i)
    return len(freshi)

print(part1('day5/testinput'))
print(part1('day5/input'))