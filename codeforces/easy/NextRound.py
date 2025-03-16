if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    for item in arr:
        if (item >= arr[k-1] and item > 0):
            count += 1
    print(count)