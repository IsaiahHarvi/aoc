import re

def part_one(s: str):
    sum = 0

    for i in re.finditer(r"mul\((\d+),(\d+)\)", s):
        arg1, arg2 = map(int, i.groups())
        sum += arg1 * arg2

    return sum

if __name__ == "__main__":
    with open("input.txt") as f:
        s = f.read()
    print(part_one(s))
