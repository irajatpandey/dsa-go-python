#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def length_of_longest_substring(self, s):
        """
        Function to find the length of the longest substring 
        without repeating characters.
        """
        left_ptr, right_ptr = 0, 0  # Sliding window pointers
        max_length = 0  # Stores the maximum length of a unique substring
        char_set = set()  # Set to store unique characters in the current window

        if not s:
            return 0  # Handle empty string case

        while right_ptr < len(s):
            # If duplicate character found, shrink the window from the left
            while s[right_ptr] in char_set:
                char_set.remove(s[left_ptr])
                left_ptr += 1

            # Add the new character to the set
            char_set.add(s[right_ptr])

            # Update the maximum length of unique substring found so far
            max_length = max(max_length, right_ptr - left_ptr + 1)

            # Expand the window by moving the right pointer
            right_ptr += 1

        return max_length


# Driver function
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = ["abcabcbb", "bbbbb", "pwwkew", "", "abcdef", "aabbcc"]
    
    for test in test_cases:
        print(f"Input: '{test}' | Longest Substring Length: {solution.length_of_longest_substring(test)}")
