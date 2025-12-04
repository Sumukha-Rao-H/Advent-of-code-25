import sys

def part1(data):
    sum = 0

    for i in data:
        sum += findMax(i)

    return sum

def part2(data):
    sum = 0
    # print(data)
    for i in data:
        # print(findTwelveMax(i))
        sum += findTwelveMax(i)

    return sum

def findMax(s):
    max1, max2 = 0,0
    index = 0
    for i in range(len(s)-1):
        if int(s[i]) > max1:
            max1 = int(s[i])
            index = i

    for i in s[index+1:]:
        max2 = max(max2, int(i))
    
    return max1*10 + max2

def findTwelveMax(s):
    k = 12
    n = len(s)
    result = []
    start = 0

    while len(result) < k:
        need = k - len(result)
        end = n - need

        max_d = -1
        max_i = -1

        for i in range(start, end + 1):
            d = int(s[i])
            if d > max_d:
                max_d = d
                max_i = i

        result.append(max_d)
        start = max_i + 1

    value = 0
    for d in result:
        value = value * 10 + d

    return value

def main():
    data = sys.stdin.read().split()
    # data now contains all lines from input.txt
    # print(data)

    ans1 = part1(data)
    ans2 = part2(data)

    print("Part1:", ans1)
    print("Part2:", ans2)


if __name__ == "__main__":
    main()