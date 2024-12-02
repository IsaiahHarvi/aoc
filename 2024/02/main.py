def part_one(l: [list]):
    safe = 0
    for i in l:
        if i in [(s_i := sorted(i)), s_i[::-1]]:
            safe += 1 if len([j for j in range(len(i)-1) if not abs(i[j] - i[j+1]) in range(1, 4)]) == 0 else 0
    return safe

def part_two(l):




if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l = [list(map(int, line.split())) for line in f if line.strip()]
    print(part_one(l))

