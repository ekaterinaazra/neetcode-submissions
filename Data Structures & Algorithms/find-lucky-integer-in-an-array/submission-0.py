class Solution:
    def findLucky(self, arr: List[int]) -> int:
        numbers = {}
        for i in range(len(arr)):
            if arr[i] not in numbers:
                numbers[arr[i]] = 1
            else:
                numbers[arr[i]] += 1 
        largest = []
        for number in numbers:
            if number == numbers[number]:
                largest.append(number)

        if not largest:
            return -1
        return max(largest)