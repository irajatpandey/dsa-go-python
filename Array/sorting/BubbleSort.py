def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - 1):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    for values in arr:
        print(values, end=" ")

# Example usage
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print("Sorted array is:", arr)