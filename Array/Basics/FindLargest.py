
def largest(arr):
    max = arr[0]
    for item in arr:
        if item > max:
            max = item
    return max



arr = [12, 34, 3, 456, 2312, 344]
print("Largest in given array is", largest(arr))