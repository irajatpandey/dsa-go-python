

def check(arr):
    count = 0  # Count of "out of order" points

    for i in range(len(arr)):
        # If current element is greater than next element (circular check), increment count
        if arr[i] > arr[(i + 1) % len(arr)]:
            count += 1
        if count > 1:
            return false

    # Array can be rotated to become sorted if there's at most one such point
    return count <= 1


# Driver function for testing
if __name__ == "__main__":
    arr = [3, 4, 5, 1, 2]
    print("Is rotated sorted array:", check(arr))  # Expected Output: True
