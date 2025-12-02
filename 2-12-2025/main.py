import sys

def part1(data):
    sum = 0
    for a,b in data:
        for i in range(a,b+1):
            if has_double_pattern(i):
                sum += i
    return sum

def part2(data):
    sum = 0
    for a,b in data:
        for i in range(a,b+1):
            if has_repeating_pattern(i):
                sum += i
    return sum

def has_double_pattern(n: int) -> bool:
    s = str(n)
    length = len(s)

    if length % 2 != 0:
        return False

    half = length // 2
    first = s[:half]
    second = s[half:]

    return first == second

def has_repeating_pattern(n: int) -> bool:
    s = str(n)
    length = len(s)

    for pat_len in range(1, length // 2 + 1):
        if length % pat_len == 0:
            pattern = s[:pat_len]
            if pattern * (length // pat_len) == s:
                return True

    return False

def split_input(data):
    res = []
    data1 = data.split(',')
    for i in data1:
        a,b = i.split('-')
        res.append([int(a),int(b)])
    return res

def main():
    data = sys.stdin.read()
    # data now contains all lines from input.txt
    # print(data)
    data = split_input(data)
    # print(data)

    ans1 = part1(data)
    ans2 = part2(data)

    print("Part1:", ans1)
    print("Part2:", ans2)


if __name__ == "__main__":
    main()