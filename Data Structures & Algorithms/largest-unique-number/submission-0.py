class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numbers = {}
        for i in range(len(nums)):
            if nums[i] not in numbers:
                numbers[nums[i]] = 1
            else:
                numbers[nums[i]] += 1
        answer = []
        for number in numbers:
            if numbers[number] == 1:
                answer = answer + [number]
        if len(answer) == 0:
            return -1
        return max(answer)
            