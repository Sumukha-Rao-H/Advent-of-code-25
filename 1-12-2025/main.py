import sys

def unlock(data):
    # data is a list of strings
    return None

def main():
    data = sys.stdin.read().splitlines()
    # data now contains all lines from input.txt

    ans = unlock(data)

    print(ans)


if __name__ == "__main__":
    main()
