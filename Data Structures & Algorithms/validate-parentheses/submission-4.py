class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2 != 0:
            return False
        for j in range(len(s)):
            if s[j] == "(" or s[j] == "{" or s[j]=="[":
                stack.append(s[j])
            elif not stack:
                return False
            elif s[j] == ")" and stack.pop() != "(":
                return False
            elif s[j] == "}" and stack.pop() != "{":
                return False
            elif s[j] == "]" and stack.pop() != "[":
                return False
        return not stack
            