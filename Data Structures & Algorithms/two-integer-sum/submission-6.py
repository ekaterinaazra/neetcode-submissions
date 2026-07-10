
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for i in range(len(nums)):
            numbers[nums[i]] = i
        print(numbers)
        for j in range(len(nums)):
            if (target - nums[j]) in numbers: 
                if numbers[(target-nums[j])] != j:
                    return [j,numbers[(target-nums[j])]]