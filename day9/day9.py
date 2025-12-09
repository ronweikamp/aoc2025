def readfile(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(tuple([int(s) for s in line.strip().split(',')]))
    
    return lines

def area(p1,p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs((p1[1] - p2[1])) + 1)

def sorted_pairs(points):
    pairs = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1 = points[i]
            p2 = points[j]
            pairs.append(((p1, p2), area(p1,p2)))
    
    sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
    
    return sorted_pairs

def day9(filename):
    return sorted_pairs(readfile(filename))[0][1]

print(day9('day9/testinput'))
print(day9('day9/input'))