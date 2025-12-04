from typing import List

def find_rating(line: str) -> int:
    ratings = []
    for i in range(0, len(line)):
        for j in range(i+1, len(line)):
            ratings.append(int(line[i] + line[j]))
    return max(ratings)

def find_rating_rec(rating, rest):
    base = 12
    if len(rating) == base:
        return [int(rating)]
    if len(rating) + len(rest) < base:
        return []
    else:
        slots_needed = base - len(rating)
        space = rest[:len(rest) - slots_needed + 1]
        m = max(space)
        max_indices = [index for index, value in enumerate(space) if value == m]

        return [r for i in max_indices for r in find_rating_rec(rating + rest[i], rest[i+1:])]

def part1(filename):
    ratings = []
    with open(filename, 'r') as file:
        for line in file:
            rating = find_rating(line)
            ratings.append(rating)
    return sum(ratings)

def part2(filename):
    ratings = []
    with open(filename, 'r') as file:
        for line in file:
            rating = max(find_rating_rec('', line.strip()))
            print(rating)
            ratings.append(rating)
    return sum(ratings)



# print(part1('day3/testinput'))
# print(part1('day3/input'))
print(part2('day3/testinput'))
print(part2('day3/input'))