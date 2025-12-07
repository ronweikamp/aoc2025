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
    print(ttlines)
    return splits

# prettyprint(readfile('day7/testinput'))

print(day7('day7/testinput'))
# print(day7('day7/input'))

# prettyprint(lines)