
if __name__ == "__main__":
    n = int(input().strip())
    count = 0
    for _ in range(n):
        str = input()
        if str == "++X":
            count += 1
        if str == "X++":
            count += 1
        if str == "--X" or str == "X--":
            count -= 1
    print(count)