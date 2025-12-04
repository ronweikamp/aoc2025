def parse_line(line: str) -> Int:
    if line[0] == 'L':
        return -int(line[1:])
    else:
        return int(line[1:])
    
filename = 'day1/test_input1.txt'
filename = 'day1/input'

def part1(filename):
    with open(filename, 'r') as file:
        start = 50
        times0 = 0
        for line in file:
            start = (start + parse_line(line)) % 100
            if start == 0:
                times0 += 1
            print(f"{line.strip()}:{parse_line(line)}:{start}")

        print(times0)

def part2(filename):
    with open(filename, 'r') as file:
        start = 50
        times0 = 0
        for line in file:
            step = parse_line(line)
            non_mod = start + step
            new_start = (start + step) % 100
            if (non_mod <= 0) and start != 0:
                times0 += 1 + int(abs(non_mod) / 100)
            elif (non_mod >= 100) and start != 0:
                times0 += int(abs(non_mod) / 100)
            elif start == 0:
                times0 += int(abs(non_mod) / 100)

            print(f"{line.strip()}:{parse_line(line)}:{non_mod}:{start}")
            start = new_start

        print(times0)

part1('day1/input')
part2('day1/input')