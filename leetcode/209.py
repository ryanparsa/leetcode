def minSubArrayLen(target: int, nums: list[int]) -> int:
    left, right = 0, 0
    minLength = float('inf')  # Set to positive infinity initially
    currentSum = 0

    while right < len(nums):
        currentSum += nums[right]

        while currentSum >= target:
            minLength = min(minLength, right - left + 1)
            currentSum -= nums[left]
            left += 1

        right += 1

    return minLength if minLength != float('inf') else 0


# assert minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]) == 2
print(minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
