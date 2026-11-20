class Solution:
    def maxArea(self, heights: List[int]) -> int:
        finalMax = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            currentMax = (r - l) * min(heights[l], heights[r])
            if currentMax > finalMax:
                finalMax = currentMax
            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] <= heights[r]:
                l += 1
            
        return finalMax
