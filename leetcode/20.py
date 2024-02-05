"""
https://leetcode.com/problems/valid-parentheses/
"""

pattern = {
    "(": ")",
    "[": "]",
    "{": "}",
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        for c in s:
            if c in pattern.keys():
                stack.append(pattern[c])
            elif not stack or stack.pop() != c:
                return False

        if stack:
            return False
        return True


s = Solution()

# print(s.isValid("()"))
# print(s.isValid("()[]{}"))
# print(s.isValid("(]"))
print(s.isValid("]"))
