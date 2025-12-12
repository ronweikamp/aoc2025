import re
import itertools
from collections import Counter

light_pattern = re.compile(r'[\.\#]')

def findbuttons(line):
    buttons = [s for s in line.split() if '(' in s]
    buttons = [tuple([int(i) for i in s.strip("()").split(',')]) for s in buttons]
    return buttons

def findjoltlevels(line):
    jolts = [s for s in line.split() if '{' in s][0]
    jolts = [int(i) for i in jolts.strip("{}").split(',')]
    return {i:j for i,j in enumerate(jolts)}

def remove_even_occurrences(lights):
    counts = Counter(lights)
    return [x for x in lights if counts[x] % 2 == 1]

def sum_buttons(buttons):
    return [i for b in buttons for i in b]


def readfile(filename):
    lights = []
    buttons = []
    jolts = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            lights.append([i for i,l in enumerate(light_pattern.findall(line)) if l =='#'])
            buttons.append(findbuttons(line))
            jolts.append(findjoltlevels(line))
    return lights, buttons, jolts

def day10(filename):
    lights, buttonlist, _= readfile(filename)
    min_combis = []
    for i, buttons in enumerate(buttonlist):
        target = set(lights[i])
        for r in range(1, len(buttons) + 1):
            found = False
            for combination in itertools.combinations(buttons, r):
                sb = sum_buttons(combination)
                t = remove_even_occurrences(sb)
                if target == set(t):
                    min_combis.append(combination)
                    found = True
                    break
            if found:
                break
    return sum([len(c) for c in min_combis])

def is_feasible_button(button, jolts_left):
    return all(i in jolts_left for i in button)

def feasible_buttons(buttonlist, jolts_left):
    return [b for b in buttonlist if is_feasible_button(b, jolts_left)] 

def update_jolts(button, jolts):
    for i in button:
        jolts[i] -= 1
    return {i:j for i,j in jolts.items() if j > 0}

# too expensive
def press_rec(buttonlist, solutions, solution, jolts_left):
    
    if len(jolts_left) == 0:
        solutions.append(solution)
        # print(f"hoi {len(solutions)}")
        return
    else:
        # print(f"fbuttons {len(feasible_buttons(buttonlist, jolts_left))}")
        k = next(iter(jolts_left))
        for b in feasible_buttons([b for b in buttonlist if k in b], jolts_left):
            new_jolts = update_jolts(b, {i:j for i,j in jolts_left.items()})
            # print(f'{jolts_left} and {new_jolts} button {b}')
            new_sol = solution + [b]
            # print(f'new sol {new_sol}')
            press_rec(buttonlist, solutions, solution + [b], new_jolts)

def day10pt2(filename):
    _, buttonlist, jolts = readfile(filename)

    minsols = []
    for i, buttons in enumerate(buttonlist):
        jolt_levels = jolts[i]
        solutions = []
        press_rec(buttons, solutions, [], jolt_levels)
        print("blabla")
        minsols.append(min([len(s) for s in solutions]))

    return sum(minsols)

# pip install z3-solver
from z3 import Optimize, sat, IntVector

def day10_sat(filename):
    
    _, buttonlist, jolts = readfile(filename)

    solutions = []
    for row, buttons in enumerate(buttonlist):
        jolt_levels = jolts[row]
        vars = IntVector('i', len(buttons))
        opt = Optimize()
        opt.add([v >= 0 for v in vars])
        for i,v in jolt_levels.items():
            buttons_that_satisfy_i = [j for j, b in enumerate(buttons) if i in b]
            opt.add(sum([vars[k] for k in buttons_that_satisfy_i]) == v)

        h = opt.minimize(sum(vars))
        if opt.check() == sat:
            m = opt.model()
            sol = [m[v].as_long() for v in vars]
            solutions.append(sum(sol))
            # print("min sum =", sum(sol))
            # print("solution =", sol)
        else:
            print("No solution found.")


    return sum(solutions)


print(day10('day10/testinput'))
print(day10('day10/input'))
print(day10pt2('day10/testinput'))
print(day10_sat('day10/testinput'))
print(day10_sat('day10/input'))