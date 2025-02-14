def print_subarrays(arr):
    
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            for k in range(i, j + 1):
                print(arr[k], end=" ")
            print()

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print_subarrays(arr)