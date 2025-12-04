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

print(part1('day2/testinput'))
print(part1('day2/input'))