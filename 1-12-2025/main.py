import sys

def part1(data):
    count = 0
    cur = 50
    for i in data:
        if i[0] == "R":
            cur += i[1]
        else:
            cur -= i[1]
        cur %= 100
        if cur == 0:
            count += 1
    return count

def part2(data):
    count = 0
    cur = 50

    for d, step in data:
        if d == "R":
            raw = cur + step
            if raw >= 100:
                count += raw // 100
            cur = raw % 100
        else:
            raw = cur - step
            if raw <= 0:
                count += (-raw // 100) + (cur != 0)
            cur = raw % 100

    return count

def split_lines(data):
    res = []
    for line in data:
        res.append([line[0], int(line[1:])] )
    return res

def main():
    data = sys.stdin.read().splitlines()
    # data now contains all lines from input.txt
    data = split_lines(data)
    # print(data)
    ans1 = part1(data)
    ans2 = part2(data)

    print("Part1:", ans1)
    print("Part2:", ans2)


if __name__ == "__main__":
    main()
