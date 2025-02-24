#https://leetcode.com/problems/longest-common-prefix/description/
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # Sort the list lexicographically
        strs.sort()
        
        # The first string is the smallest, and the last is the largest
        smallest_string = strs[0]
        largest_string = strs[-1]
        
        # Initialize the common prefix
        common_prefix = ""
        
        # Determine the minimum length to avoid index out of range
        min_length = min(len(smallest_string), len(largest_string))
        
        # Iterate through each character up to the minimum length
        for i in range(min_length):
            if smallest_string[i] == largest_string[i]:
                common_prefix += smallest_string[i]
            else:
                break
        
        return common_prefix

# Driver function
def main():
    solution = Solution()
    
    # Test Case 1
    strs1 = ["flower", "flow", "flight"]
    print(f"Input: {strs1}\nOutput: \"{solution.longestCommonPrefix(strs1)}\"\n")
    
    # Test Case 2
    strs2 = ["dog", "racecar", "car"]
    print(f"Input: {strs2}\nOutput: \"{solution.longestCommonPrefix(strs2)}\"\n")
    
    # Test Case 3
    strs3 = ["interspecies", "interstellar", "interstate"]
    print(f"Input: {strs3}\nOutput: \"{solution.longestCommonPrefix(strs3)}\"\n")
    
    # Test Case 4
    strs4 = ["throne", "throne"]
    print(f"Input: {strs4}\nOutput: \"{solution.longestCommonPrefix(strs4)}\"\n")
    
    # Test Case 5
    strs5 = []
    print(f"Input: {strs5}\nOutput: \"{solution.longestCommonPrefix(strs5)}\"\n")
    
    # Test Case 6
    strs6 = ["", "b"]
    print(f"Input: {strs6}\nOutput: \"{solution.longestCommonPrefix(strs6)}\"\n")

if __name__ == "__main__":
    main()