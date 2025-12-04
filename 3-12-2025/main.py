import sys

def part1(data):
    sum = 0
    
    for i in data:
        sum += findMax(i)

    return sum

def part2(data):
    pass

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