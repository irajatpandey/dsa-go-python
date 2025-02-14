def linear_search(arr, target):
    for element in arr:
        if element == target:
            print("Element found in an Array")
    print("Element not found")

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    target = 3
    result = linear_search(arr, target)
    print(f"Element found at index: {result}")