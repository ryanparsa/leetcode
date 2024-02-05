class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        p1 = 0
        p2 = len(s) - 1

        new_s = list(s)  # O (n)

        # O (log n)
        while p1 < p2:
            if new_s[p1] not in vowels:  # O (1)
                p1 += 1
                continue
            elif new_s[p2] not in vowels:  # O (1)
                p2 -= 1
                continue

            else:
                new_s[p1], new_s[p2] = new_s[p2], new_s[p1]  # O (1)
                p1 += 1
                p2 -= 1

        # O (N)
        return ''.join(new_s)


s = Solution()
print(s.reverseVowels("leetcode"))

a = []

print(id(a))
for i in range(10):
    a += str(i)
    print(id(a))

print(id(a))
