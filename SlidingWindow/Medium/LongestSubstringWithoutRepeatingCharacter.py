#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, max_length = 0, 0, 0
        char_count = {}
        while right < len(s):
            char_count[s[right]] = char_count.get(s[right], 0) + 1 
            while char_count[s[right]] > 1:
                char_count[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
            right += 1
        return max_length


# Driver function
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = ["abcabcbb", "bbbbb", "pwwkew", "", "abcdef", "aabbcc"]
    
    for test in test_cases:
        print(f"Input: '{test}' | Longest Substring Length: {solution.length_of_longest_substring(test)}")
