def strStr(haystack: str, needle: str) -> int:
    haystack_index = 0
    needle_index = 0

    while haystack_index < len(haystack) and needle_index < len(needle):
        if haystack[haystack_index] == needle[needle_index]:
            haystack_index += 1
            needle_index += 1
        else:
            haystack_index = haystack_index - needle_index + 1
            needle_index = 0

    if needle_index == len(needle):
        return haystack_index - needle_index

    return -1

# Test cases
assert strStr(haystack="sadbutsad", needle="sad") == 0
assert strStr(haystack="leetcode", needle="leeto") == -1
