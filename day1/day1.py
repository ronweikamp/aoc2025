def parse_line(line: str) -> Int:
    if line[0] == 'L':
        return -int(line[1:])
    else:
        return int(line[1:])
    
filename = 'day1/test_input1.txt'
filename = 'day1/input'

def part1():
    with open(filename, 'r') as file:
        start = 50
        times0 = 0
        for line in file:
            start = (start + parse_line(line)) % 100
            if start == 0:
                times0 += 1
            print(f"{line.strip()}:{parse_line(line)}:{start}")

        print(times0)

part1()