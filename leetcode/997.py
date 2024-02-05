"""
https://leetcode.com/problems/find-the-town-judge/
"""


def findJudge(n: int, trust: list[list[int]]) -> int:
    count = [0] * (n + 1)
    for p1, p2 in trust:
        count[p1] -= 1  # out degree
        count[p2] += 1  # in degree

    for i in range(1, n + 1):
        if count[i] == n - 1:
            return i
    return -1


assert findJudge(n=3, trust=[[1, 3], [2, 3]]) == 3
assert findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]) == -1
assert findJudge(n=3, trust=[[1, 2], [2, 3]]) == -1
