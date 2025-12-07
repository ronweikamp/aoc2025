def readfile(filename):
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line.strip())
    
    return lines

def prettyprint(lines):
    for l in lines:
        print(l)

def find_char_indices(s, char):
    return [i for i, c in enumerate(s) if c == char]

def replace_char_at_index(original_string, index, new_char):
    
    new_string = original_string[:index] + new_char + original_string[index + 1:]
    return new_string

def next(lines, irow):
    # copy
    new_lines = [l for l in lines]

    splits = 0
    if irow == 0:
        row = new_lines[0].replace('S', '|')
        new_lines[irow] = row
    else:
        ibeams = find_char_indices(new_lines[irow-1], '|')
        # print(ibeams)
        row = new_lines[irow]
        for i in ibeams:
            if row[i] == '.':
                row = replace_char_at_index(row, i, '|')
            elif row[i] == '^':
                splits += 1
                if i > 0 and row[i-1] == '.':
                    row = replace_char_at_index(row, i-1, '|')
                if i < len(row) - 1 and row[i+1] == '.':
                    row = replace_char_at_index(row, i+1, '|')
    
        new_lines[irow] = row
    
    tlines = sum(['|' == c for c in new_lines[irow]])
    return new_lines, splits, tlines

def next_rec(lines, irow):
    # copy
    new_lines = [l for l in lines]

    if irow == len(lines) - 1:
        # print('hoi')
        return [1]
    elif irow == 0:
        row = new_lines[0].replace('S', '|')
        new_lines[irow] = row
        return next_rec(new_lines, 1)
    else:
        i = find_char_indices(new_lines[irow-1], '|')[0]
        # print(ibeams)
        row = new_lines[irow]

        if row[i] == '.':
            row = replace_char_at_index(row, i, '|')
            new_lines[irow] = row
            return next_rec(new_lines, irow+1)
        elif '^' in row:
            if (i > 0 and row[i-1] == '.') and (i < len(row) - 1 and row[i+1] == '.'):
                row1 = replace_char_at_index(row, i-1, '|')
                row2 = replace_char_at_index(row, i+1, '|')
                world1 = [l for l in new_lines]
                world2 = [l for l in new_lines]
                world1[irow] = row1
                world2[irow] = row2
                return next_rec(world1, irow + 1) + next_rec(world2, irow+1)
            elif i > 0 and row[i-1] == '.':
                row = replace_char_at_index(row, i-1, '|')
                new_lines[irow] = row
                return next_rec(new_lines, irow + 1)
            elif i < len(row) - 1 and row[i+1] == '.':
                row = replace_char_at_index(row, i+1, '|')
                new_lines[irow] = row
                return next_rec(new_lines, irow + 1)


def day7(filename):
    n0, s0, tlines = next(readfile(filename), 0)
    # prettyprint(n0)
    # n1, s1 = next(n0, 1)
    splits = 0
    ssplits = []
    ttlines = []
    for i in range(0, len(n0)):
        n0, s, tlines = next(n0, i)
        ssplits.append(s)
        ttlines.append(tlines)
        # prettyprint(n0)
        splits += s
    # print(ttlines)
    return splits

def day7pt2(filename):
    outcome = next_rec(readfile(filename), 0)

    # for w in outcome:
    #     # prettyprint(w)
    #     print("")
    return len(outcome)

# prettyprint(readfile('day7/testinput'))

# print(day7('day7/testinput'))
print(day7pt2('day7/testinput'))
# print(day7pt2('day7/input'))
# print(day7('day7/input'))

# prettyprint(lines)