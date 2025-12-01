import sys

def unlock(data):
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
    ans = unlock(data)

    print(ans)


if __name__ == "__main__":
    main()
