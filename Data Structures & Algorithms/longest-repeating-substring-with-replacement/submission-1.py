class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = defaultdict(int)
        i = 0
        maxLen = 0
        maxFreq = 0
        while i + maxLen < len(s):
            charCount[s[i+maxLen]] += 1
            maxFreq = max(maxFreq, charCount[s[i+maxLen]])
            if maxLen-maxFreq < k:
                maxLen += 1
            else:
                charCount[s[i]] -= 1
                i += 1
        return maxLen

