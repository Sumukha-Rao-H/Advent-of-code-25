import sys

def part1(data):
    res = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "@" and  access(i,j,data):
                res += 1
    return res

def part2(data):
    rows = len(data)
    cols = len(data[0])
    total_removed = 0

    while True:
        to_remove = []

        for i in range(rows):
            for j in range(cols):
                if data[i][j] == '@' and access(i, j, data):
                    to_remove.append((i, j))

        if not to_remove:
            return total_removed

        for i, j in to_remove:
            data[i][j] = '.'

        total_removed += len(to_remove)

def access(i, j, data):
    rows = len(data)
    cols = len(data[0])
    count = 0

    # Directions: (row_offset, col_offset)
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    for di, dj in dirs:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols:
            if data[ni][nj] == '@':
                count += 1

    return count < 4

def matrix(data):
    res = []
    for i in data:
        res.append(list(i))
        # print(res[-1],"\n")
    return res

def main():
    data = sys.stdin.read().strip().splitlines()
    # data now contains all lines from input.txt
    data = matrix(data)
    # print(data)


    ans1 = part1(data)
    ans2 = part2(data)

    print("Part1:", ans1)
    print("Part2:", ans2)


if __name__ == "__main__":
    main()