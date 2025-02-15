def insertion_sort(arr):
    for i in range(1, len(arr)):  # Traverse through 1 to len(arr)
        key = arr[i]  # Store the current element in key
        j = i - 1 # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert the key in its correct position
        
    return arr  # Return the sorted array


# Driver code to test the function
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = insertion_sort(arr)
    print("Sorted array:", sorted_arr)
