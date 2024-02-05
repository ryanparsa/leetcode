from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        p1 = 0

        while p1 < len(flowerbed):
            if p1 + 1 < len(flowerbed):
                if p1 >= 0:
                    if sum([flowerbed[p1 - 1] + flowerbed[p1] + flowerbed[p1 + 1]]) == 0:
                        n -= 1
                        p1 = p1 + 1
            p1 += 1

        return n <= 0


s = Solution()

# print(s.canPlaceFlowers([1, 0, 0, 0, 0, 0, 1], 2))
print(s.canPlaceFlowers([0, 0, 1, 0, 1], 1))
