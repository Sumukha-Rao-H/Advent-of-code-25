import sys

def part1(ingredients, ids):
    ptr1, ptr2 = 0,0
    res = 0

    while ptr2 < len(ids) and ptr1 < len(ingredients):

        start, end = ingredients[ptr1]
        id = ids[ptr2]

        if id < start:
            ptr2 += 1
        elif id > end:
            ptr1 += 1
        else:
            res += 1
            ptr2 += 1
    
    return res

def part2(ingredients):
    res = 0
    for start, end in ingredients:
        res += end+1-start
    return res

def merge_intervals(ingredients):
    ingredients = sorted(ingredients)
    merged = [ingredients[0]]

    for start, end in ingredients[1:]:
        prevStart, prevEnd = merged[-1]

        if start <= prevEnd:
            merged[-1][1] = max(prevEnd, end)
        else:
            merged.append([start,end])

    return merged


def split(data):
    ingredients, ids = [] , []
    i = 0
    while data[i] != '':
        ingredients.append([int(data[i].split('-')[0]),int(data[i].split('-')[1])])
        i += 1
    for id in data[i+1:]:
        ids.append(int(id))

    return ingredients, ids

def main():
    data = sys.stdin.read().strip().splitlines()
    # data now contains all lines from input.txt
    ingredients, ids = split(data)
    ingredients = merge_intervals(ingredients)
    ids = sorted(ids)
    # print(ingredients)
    # print(ids)
    # print(data)

    ans1 = part1(ingredients, ids)
    ans2 = part2(ingredients)

    print("Part1:", ans1)
    print("Part2:", ans2)


if __name__ == "__main__":
    main()