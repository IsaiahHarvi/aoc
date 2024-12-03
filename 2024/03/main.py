import re

def part_one(s: str):
    sum = 0

    for i in re.finditer(r"mul\((\d+),(\d+)\)", s):
        arg1, arg2 = map(int, i.groups())
        sum += arg1 * arg2

    return sum

def part_two(s: str):
    sum = 0
    enabled = True
    pattern = re.compile(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)")

    for i in pattern.finditer(s):
        print(i.groups())
        if i.group(0) == "do()":
            enabled = True
        elif i.group(0) == "don't()":
            enabled = False
        elif enabled:
            arg1, arg2 = map(int, i.groups())
            sum += arg1 * arg2

    return sum 


if __name__ == "__main__":
    with open("input.txt") as f:
        s = f.read()

    print(part_one(s))
    print(part_two(s))
