def count_palindromes(s):
    n = len(s)
    palindromes_count = 0

    # Helper function to expand around the center
    def expand_around_center(left, right):
        nonlocal palindromes_count
        while left >= 0 and right < n and s[left] == s[right]:
            palindromes_count += 1
            left -= 1
            right += 1

    # Iterate through each character as a potential center
    for i in range(n):
        # Consider odd-length palindromes
        expand_around_center(i, i)

        # Consider even-length palindromes
        expand_around_center(i, i + 1)

    return palindromes_count


# Test cases
print(count_palindromes("abc"))  # Output: 3
print(count_palindromes("aaa"))  # Output: 6
