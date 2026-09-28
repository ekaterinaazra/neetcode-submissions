class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        finish = len(heights)-1
        max_area = 0
        while start < finish:
            area = min(heights[start], heights[finish])*(finish-start)
            max_area = max(area,max_area)
            
            if heights[start] < heights[finish]:
                start += 1
            else:
                finish -= 1  
        
        return max_area


        