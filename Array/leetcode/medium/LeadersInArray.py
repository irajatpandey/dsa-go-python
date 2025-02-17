def find_leaders(arr):
    result = []
    currentLeader = arr[len(arr) - 1]
    for i in range(len(arr) - 1, -1, -1):
        if len(result) == 0:
            result.append(currentLeader)
        else:
            if arr[i] >= currentLeader:
                currentLeader = arr[i]
                result.append(currentLeader)
    result.reverse()
    return result
    

# Example usage
if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    leaders = find_leaders(arr)
    print(f"Leaders in the array are: {leaders}")