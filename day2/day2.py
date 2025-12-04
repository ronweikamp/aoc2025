def part1(filename):
    with open(filename, 'r') as file:
        for line in file:
            ranges_string = [range.split('-') for range in line.split(',')]
            ranges_int = [(int(r[0]), int(r[1])) for r in ranges_string]
            invalids = []
            for lower,upper in ranges_int:
                print(f"{lower}-{upper}")
                for i in range(lower, upper +1):
                    si = str(i)
                    l = len(si)
                    if l % 2 == 0:
                        hl = int(l/2)
                        if si[0:hl] == si[hl:]:
                            print(si)
                            invalids.append(int(si))

            return sum(invalids)
        
def partition_list(original_list, size):
    return [original_list[i:i + size] for i in range(0, len(original_list), size)]

def part2(filename):
    with open(filename, 'r') as file:
        for line in file:
            ranges_string = [range.split('-') for range in line.split(',')]
            ranges_int = [(int(r[0]), int(r[1])) for r in ranges_string]
            invalids = set()
            for lower,upper in ranges_int:
                print(f"{lower}-{upper}")
                for i in range(lower, upper +1):
                    si = str(i)
                    l = len(si)

                    for ng in range(2, l + 1):
                        if l % ng == 0:

                            parts = partition_list(si, int(l/ng))
                            # print(parts)

                            if all(part == parts[0] for part in parts):
                                print(si)
                                invalids.add(int(si))

            return sum(invalids)

# print(part1('day2/testinput'))
# print(part1('day2/input'))
print(part2('day2/testinput'))
print(part2('day2/input'))