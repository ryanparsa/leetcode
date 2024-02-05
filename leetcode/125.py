"""
https://leetcode.com/problems/valid-palindrome/
"""


def isPalindrome(s: str) -> bool:
    p1 = 0
    p2 = len(s) - 1
    while p1 < p2:
        if not s[p2].isalnum():
            p2 -= 1
        elif not s[p1].isalnum():
            p1 += 1

        elif str.lower(s[p2]) != str.lower(s[p1]):
            return False

        else:
            p2 -= 1
            p1 += 1

    return True


assert isPalindrome("A man, a plan, a canal: Panama") == True
assert isPalindrome("0P") == False
