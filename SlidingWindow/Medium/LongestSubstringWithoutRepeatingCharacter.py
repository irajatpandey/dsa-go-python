#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, max_length = 0, 0, 0
        freq = [0] * 128  # Frequency array for ASCII characters
        
        while right < len(s):
            freq[ord(s[right])] += 1  # Increment frequency of current character
            
            # If character appears more than once, shrink the window from the left
            while freq[ord(s[right])] > 1:
                freq[ord(s[left])] -= 1
                left += 1  # Move left pointer forward
            
            max_length = max(max_length, right - left + 1)  # Update max length
            right += 1  # Expand window by moving right pointer
        
        return max_length


# Driver function
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = ["abcabcbb", "bbbbb", "pwwkew", "", "abcdef", "aabbcc"]
    
    for test in test_cases:
        print(f"Input: '{test}' | Longest Substring Length: {solution.length_of_longest_substring(test)}")
