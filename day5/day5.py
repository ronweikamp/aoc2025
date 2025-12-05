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

def merge_ranges(ranges):
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    
    merged = [sorted_ranges[0]]
    
    for current in sorted_ranges[1:]:
        previous = merged[-1]
        
        if current[0] <= previous[-1]:
            merged[-1] = range(previous[0], max(previous[-1], current[-1]) + 1)
        else:
            merged.append(current)
    
    return merged

def part2(filename):
    ranges, _ = readfile(filename)
    merged_ranges = merge_ranges(ranges)
    return sum([len(r) for r in merged_ranges])

print(part1('day5/testinput'))
print(part1('day5/input'))
print(part2('day5/testinput'))
print(part2('day5/input'))