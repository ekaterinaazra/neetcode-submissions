class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = {}
        for i in range(len(nums)):
            if nums [i] not in elements:
                elements[nums[i]] = 1
            else:
                elements[nums[i]] += 1
        answer = nums[0] 
        largest = elements[nums[0]]
        for element in elements:
            if elements[element] > largest:
                largest = elements[element]
                answer = element 
        return answer