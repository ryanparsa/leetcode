package main

func twoSum1(nums []int, target int) []int {
    // Time: O(n^2), Space: O(1)
    for i := 0; i < len(nums); i++ {
        for j := i + 1; j < len(nums); j++ {
            if nums[i]+nums[j] == target {
                return []int{i, j}
            }
        }
    }
    return nil
}

func twoSum2(nums []int, target int) []int {
    // Time: O(n), Space: O(n)
    data := make(map[int]int)

    for i, num := range nums {
        complement := target - num
        if index, ok := data[complement]; ok {
            return []int{index, i}
        }
        data[num] = i
    }

    return nil
}

func main() {
    
}
