

def part_one(l1, l2):
    distances = 0
    for i, j in zip(sorted(l1), sorted(l2)):
        distances += abs(i - j)

    return distances

def part_two(l1, l2):
    score = 0
    for i in l1:
        score += i * l2.count(i)

    return score



if __name__ == "__main__":
    with open("input.txt", "r") as f:
        l1, l2 = [], []
        for i in f:
            cols = i.split()
            if len(cols):
                l1.append(int(cols[0]))
                l2.append(int(cols[1]))

    print(part_one(l1, l2))
    print(part_two(l1, l2))

