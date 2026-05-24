class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) -1
        water = 0

        while (i < j):
            cw = (j - i ) * min(heights[i], heights[j])

            water = max(water, cw)

            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1

        return water




        