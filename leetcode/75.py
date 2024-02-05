def sortColors(nums: list[int]) -> None:
    left, mid, right = 0, 0, len(nums) - 1

    while right >= mid:
        if nums[mid] == 0:
            nums[mid], nums[left] = nums[left], nums[mid]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1


print(sortColors(nums=[2, 0, 2, 1, 1, 0]))
