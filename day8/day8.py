import numpy as np
from functools import reduce

def distance(point1, point2):
    point1 = np.array(point1)
    point2 = np.array(point2)
    
    return np.linalg.norm(point2 - point1)

def distance_matrix(points):
    points_array = np.array(points)
    
    dist_matrix = np.linalg.norm(points_array[:, np.newaxis] - points_array, axis=2)
    
    return dist_matrix

def sorted_point_pairs(points):
    dist_matrix = distance_matrix(points)
    
    pairs = []
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            pairs.append(((points[i], points[j]), dist_matrix[i, j]))
    
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    
    return sorted_pairs

def clusters(sorted_pairs, count=10):
    clusters = []
    i = 0
    for (p1,p2), _  in sorted_pairs:
        if (i == count):
            break
        # clusters that contain p1 or p2
        existing_c = [i for i,c in enumerate(clusters) if (p1 in c) or (p2 in c)]
        if len(existing_c) > 0:
            clusters[existing_c[0]].add(p1)
            clusters[existing_c[0]].add(p2)
            if len(existing_c) > 1:
                # merge
                # print("merge")
                clusters[existing_c[0]] = clusters[existing_c[0]].union(clusters.pop(existing_c[1]))
        else:
            clusters.append({p1,p2})
        i += 1

    return clusters

def readfile(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(tuple([int(s) for s in line.strip().split(',')]))
    
    return lines

def day8(filename):
    points = readfile(filename)
    sorted_cs = sorted([len(c) for c in clusters(sorted_point_pairs(points), count=1000)], reverse=True)[:3]
    print(sorted_cs)
    return reduce(lambda x, y: x * y, sorted_cs)

print(day8('day8/testinput'))
print(day8('day8/input'))