import sys
import time

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

def find_line(p1, p2, end=False):
    if p1[0] == p2[0]:
        # vertical
        min_y = min(p1[1] , p2[1])
        max_y = max(p1[1] , p2[1])
        # print((min_y, max_y))
        if end:
            # skip start, include end
            return {(p1[0], i) for i in range(min_y+1, max_y+1)}
        else:
            # include start, skip end
            return {(p1[0], i) for i in range(min_y, max_y)}

        # return border.difference({p1, p2})
    else:
        # horizontal
        min_x = min(p1[0] , p2[0])
        max_x = max(p1[0] , p2[0])
        if end:
            return {(i, p1[1]) for i in range(min_x+1, max_x + 1)}
        else:
            return {(i, p1[1]) for i in range(min_x, max_x)}

def find_borders2(points):
    v_borders = []
    h_borders = []
    v_borders_with_end = []
    h_borders_with_end = []
    for i in range(len(points) + 1):
        # if i == len(points):
        #     border = border.union(find_line(points[-1], points[0]))
        # else:
        p1 = points[i % len(points)]
        p2 = points[(i+1) % len(points)]
        # print((p1,p2))
        new_border = find_line(p1,p2)
        # print(new_border)
        if p1[0] == p2[0]:
            v_borders.append(find_line(p1,p2))
            v_borders_with_end.append(find_line(p1,p2, end=True))
        else:
            h_borders.append(new_border)
            h_borders_with_end.append(find_line(p1,p2, end=True))
        # borders.append(new_border)

    return (v_borders, h_borders, v_borders_with_end, h_borders_with_end)

# too slow, cannot flood these large lattices
def find_inside_flood_dfs(border, current=(0,0), flood={(0,0)}, visited={(0,0)}):
    # min_x = min([p[0] for p in border])
    x_max = max([p[0] for p in border]) + 2
    # min_y = min([p[1] for p in border])
    y_max = max([p[1] for p in border]) + 2

    x,y=current
    neighbors = [(x-1,y), (x+1,y), (x, y-1), (x,y+1)]
    neighbors = [(nx,ny) for (nx,ny) in neighbors if (nx >= 0 and nx < x_max + 1) and (ny >= 0 and ny < y_max)]
    neighbors = [n for n in neighbors if n not in visited]
    # print(current)
    # print(neighbors)

    if len(flood) % 10 == 0:
        print(len(flood))
    if len(visited) % 10 == 0:
        print(len(visited))

    if len(neighbors) == 0:
        return
    else:
        for n in neighbors:
            visited.add(n)
            start = time.perf_counter()
            not_in_border = n not in border
            end = time.perf_counter()
            print(f"Elapsed: {end - start:.6f} s")
            if not_in_border:
                flood.add(n)
                # print(n)
                find_inside_flood_dfs(border, n, flood, visited)

# idea: if the vertical side of the square intersects with a horizontal line, 
# that moves inside the square.
# it must have a point outside the area. Also for horizontal sides with vertical
# lines.
def test_square(s, h_borders, v_borders, h_borders_with_end, v_borders_with_end):
    p1,p2 = s
    x_min = min(p1[0], p2[0])
    x_max = max(p1[0], p2[0])
    y_min = min(p1[1], p2[1])
    y_max = max(p1[1], p2[1])
    # print(s)
    
    vv_borders = set([p for b in v_borders for p in b if 
                      (p[1] == y_min) and
                      (p[0] > x_min) and 
                      (p[0] < x_max)
                      ])
    vv_borders_with_end = set([p for b in v_borders_with_end for p in b if 
                               (p[1] == y_max) and 
                               (p[0] > x_min) and 
                               (p[0] < x_max)
                               ])
    if len(vv_borders) > 0 or len(vv_borders_with_end) > 0:
        return False
    
    hh_borders = set([p for b in h_borders for p in b if 
                      (p[0] == x_min) and
                      (p[1]>y_min) and 
                      (p[1] < y_max)
                      ])
    hh_borders_with_end = set([p for b in h_borders_with_end for p in b if 
                               (p[0] == x_max) and
                               (p[1]>y_min) and 
                               (p[1] < y_max)
                               ])
    if len(hh_borders) > 0 or len(hh_borders_with_end) > 0:
        return False

    return True

def print_grid(points):
    max_x = max([p[0] for p in points])
    max_x = 12
    max_y = max([p[1] for p in points])
    max_y = 8

    for j in range(0, max_y + 1):
        line = []
        for i in range(0,max_x + 1):
            if (i,j) in points:
                line.append('#')
            else:
                line.append('.')
        print(''.join(line))


def day9(filename):
    return sorted_pairs(readfile(filename))[0][1]

def sqaure_to_points(square):
    p1, p2 = square
    x_min = min(p1[0], p2[0])
    x_max = max(p1[0], p2[0])
    y_min = min(p1[1], p2[1])
    y_max = max(p1[1], p2[1])
    
    square_points = set()
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            square_points.add((i, j))
    
    return square_points

def square_opposite(square):
    ((x1,y1), (x2,y2)) = square
    return ((x1,y2), (x2,y1))

def day9pt2(filename):
    # return len(sorted_pairs(readfile(filename))) # 122760
    points = readfile(filename)
    (v_borders, h_borders, v_borders_with_end, h_borders_with_end) = find_borders2(points)

    v_border_points = set([p for b in v_borders for p in b])
    # print_grid(border_points)
    # print_grid(v_border_points)
    print()
    
    start = 35000 if (len(points) > 100) else 0
    count = 0 + start
    valid_squares = []
    valid_squares2 = []
    for (s,_) in sorted_pairs(readfile(filename))[start:]:
  
        print(f'eval {s}')
   
        if test_square(s,h_borders, v_borders, h_borders_with_end, v_borders_with_end):
            valid_squares.append(s)
            print("yoyo")
            print(area(*s))
            break
        count += 1
        print(count)
        

    print(len(valid_squares))
    print(valid_squares[0])
    return area(*valid_squares[0])

print(day9('day9/testinput'))
print(day9('day9/input'))
print(day9pt2('day9/testinput'))
print(day9pt2('day9/input'))