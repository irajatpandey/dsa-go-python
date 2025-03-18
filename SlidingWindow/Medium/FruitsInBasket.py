""" 
Time Complexity: O(N²)
Space Complexity: O(N)
N elements in the worst case.
"""
def totalElementsBruteForce(arr):
    n = len(arr)
    max_len = 0
    
    for i in range(n):
        distinct = set()  # Set to track distinct elements
        for j in range(i, n):
            distinct.add(arr[j])
            if len(distinct) > 2:
                break  # More than 2 distinct elements, stop checking further
            max_len = max(max_len, j - i + 1)  # Update max length
    
    return max_len



def totalElements(self,arr):
    left, right, ans = 0, 0, 0
    freq = {}  # Dictionary to store frequency of elements
    
    while right < len(arr):
        freq[arr[right]] = freq.get(arr[right], 0) + 1  # Add right element
        
        # If there are more than 2 distinct elements, shrink window from left
        while len(freq) > 2:
            freq[arr[left]] -= 1
            if freq[arr[left]] == 0:
                del freq[arr[left]]  # Remove element if frequency becomes zero
            left += 1
        
        ans = max(ans, right - left + 1)  # Update max length
        right += 1
    
    return ans

