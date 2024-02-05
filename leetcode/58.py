def lengthOfLastWord(s: str) -> int:
    p1 = len(s) - 1
    p2 = p1

    while p2 >= 0 and s[p2] == ' ':
        p2 -= 1
        p1 = p2

    while p1 >= 0 and s[p1] != ' ':
        p1 -= 1

    return p2 - p1


assert lengthOfLastWord("a") == 1
assert lengthOfLastWord("a ") == 1
assert lengthOfLastWord("Hello World") == 5
assert lengthOfLastWord("   fly me   to   the moon  ") == 4
