#https://leetcode.com/problems/longest-consecutive-sequence/description/

def longest_consecutive(nums):
    hashSet = set(nums)
    max_count = 0
    candidate = None
    for item in hashSet:
        if item - 1 not in hashSet:
            candidate = item
            count = 1  # Initialize count here
            while candidate + 1 in hashSet:
                candidate += 1
                count += 1
            max_count = max(max_count, count)
    return max_count

# Example usage
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    result = longest_consecutive(nums)
    print(f"Length of the longest consecutive sequence is: {result}")