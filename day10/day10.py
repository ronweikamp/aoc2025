import re
import itertools
from collections import Counter

light_pattern = re.compile(r'[\.\#]')

def findbuttons(line):
    buttons = [s for s in line.split() if '(' in s]
    buttons = [tuple([int(i) for i in s.strip("()").split(',')]) for s in buttons]
    return buttons

def remove_even_occurrences(lights):
    counts = Counter(lights)
    return [x for x in lights if counts[x] % 2 == 1]

def sum_buttons(buttons):
    return [i for b in buttons for i in b]


def readfile(filename):
    lights = []
    buttons = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            lights.append([i for i,l in enumerate(light_pattern.findall(line)) if l =='#'])
            buttons.append(findbuttons(line))
    return lights, buttons

def day10(filename):
    lights, buttonlist = readfile(filename)
    min_combis = []
    for i, buttons in enumerate(buttonlist):
        target = set(lights[i])
        for r in range(1, len(buttons) + 1):
            found = False
            for combination in itertools.combinations(buttons, r):
                sb = sum_buttons(combination)
                t = remove_even_occurrences(sb)
                if target == set(t):
                    print(f"yoyo {combination} {target}")
                    min_combis.append(combination)
                    found = True
                    break
            if found:
                break
    return sum([len(c) for c in min_combis])

print(day10('day10/testinput'))
print(day10('day10/input'))