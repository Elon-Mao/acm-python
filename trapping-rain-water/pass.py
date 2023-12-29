# https://leetcode.cn/problems/trapping-rain-water/
from heapq import heappush, heappop

class Solution:
    def trap(self, height: list[int]) -> int:
        capacity = 0
        bar_heap = []
        for i, bar in enumerate(height):
            last_bar = bar
            while len(bar_heap) > 0:
                if bar_heap[0][0] > bar:
                    capacity += (i - bar_heap[0][1] - 1) * (bar - last_bar)
                    break
                else:
                    pop_bar = heappop(bar_heap)
                    capacity += (i - pop_bar[1] - 1) * (pop_bar[0] - last_bar)
                    last_bar = pop_bar[0]
            heappush(bar_heap, (bar, i))
        return capacity

solution = Solution()
print(solution.trap([4,2,0,3,2,5]))