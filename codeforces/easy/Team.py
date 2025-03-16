 
if __name__ == "__main__":
    n = int(input())  # Read the value of n
    matrix = [list(map(int, input().split())) for _ in range(n)]  # Read n rows
    count = 0
    for problem in matrix:
        if problem[0] == 1 and problem[1] == 1:
           count += 1
        elif problem[1] == 1 and problem[2] == 1:
            count += 1
        elif problem[0] == 1 and problem[2] == 1:
            count += 1
    print(count) 
        


""" 
if __name__ == "__main__":
    n = int(input().strip())
    count = 0
    for _ in range(n):
        # Read the row of integers (space-separated)
        row = list(map(int, input().split()))
        # If at least two values are 1, increase count
        if sum(row) >= 2:
            count += 1
    print(count)


"""