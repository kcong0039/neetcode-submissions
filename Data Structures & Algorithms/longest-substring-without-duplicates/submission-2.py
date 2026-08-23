class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        i = 0
        while i + maxLen + 1 <= len(s):
            if len(list(s[i:i+maxLen+1])) == len(set(s[i:i+maxLen+1])):
                maxLen += 1
            else:
                i += 1
        return maxLen