import sys

def part1(matrix, operators):
    total = 0
    for i in range(len(matrix[0])):
        if operators[i] == '*':
            ans = 1
            for j in range(len(matrix)):
                ans *= matrix[j][i]
        else:
            ans = 0
            for j in range(len(matrix)):
                ans += matrix[j][i]
        # print(ans)
        total += ans
    return total

def part2(blocks, operators):
    total = 0
    for i in range(len(blocks)):
        block = blocks[i]
        op = operators[i]

        if op == '*':
            ans = 1
            for n in block:
                ans *= n
        else:
            ans = 0
            for n in block:
                ans += n

        total += ans

    return total
        

def process1(data):
    operator_line = data[-1]
    operators = operator_line.split()

    matrix = [list(map(int, line.split())) for line in data[:-1]]

    return matrix, operators

def process2(data):
    W = max(len(line) for line in data)

    # Pad all lines
    data = [line.ljust(W) for line in data]

    blocks = []
    current_block = []

    for col in range(W):
        digits = []
        for row in range(len(data)):
            ch = data[row][col]
            if ch.isdigit():
                digits.append(ch)

        if digits:
            # we have a vertical number
            num = int("".join(digits))
            current_block.append(num)
        else:
            # no digits in this column → end block if any
            if current_block:
                blocks.append(current_block)
                current_block = []

    # Add final block if it exists
    if current_block:
        blocks.append(current_block)

    return blocks
    
def main():
    data = sys.stdin.read().strip().splitlines()
    # data now contains all data from input.txt
    # print(data)
    matrix, operators = process1(data)
    ans1 = part1(matrix, operators)
    
    # for i in data:
    #     print(i, "\n")
    blocks = process2(data[:-1])
    # print(blocks)
    ans2 = part2(blocks, operators)

    print("Part1:", ans1)
    print("Part2:", ans2)


if __name__ == "__main__":
    main()