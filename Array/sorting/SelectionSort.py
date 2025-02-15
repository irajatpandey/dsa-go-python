def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i  # Assume the current index has the smallest element

        # Find the minimum element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update min_index if a smaller element is found
        
        # Swap the minimum element with the first element of the unsorted part
        arr[min_index], arr[i] = arr[i], arr[min_index]

    return arr  # Return the sorted array


# Driver code to test the function
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = selection_sort(arr)
    print("Sorted array:", sorted_arr)
