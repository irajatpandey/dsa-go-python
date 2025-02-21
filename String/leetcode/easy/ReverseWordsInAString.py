#https://leetcode.com/problems/reverse-words-in-a-string/description/

def reverse(s, start, end):
	while start <= end:
		s[start], s[end] = s[end], s[start]
		start += 1
		end -= 1

def trimSpace(s):
    # Remove leading spaces
    start = 0
    while start < len(s) and s[start] == ' ':
        start += 1
    # Remove trailing spaces
    end = len(s) - 1
    while end >= start and s[end] == ' ':
        end -= 1
    return s[start:end+1]


def reverseWords(s):

    trimSpace(s)
    reverse(s, 0, len(s) - 1)
    # Step 3: Reverse each word individually
    for i in range(n + 1):
        if i == n or s[i] == ' ':
            reverse(s, start, i - 1)
            start = i + 1
    return ''.join(s)

print(reverseWords("the sky is blue"))
