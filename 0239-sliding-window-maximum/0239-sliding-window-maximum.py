import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        pq = []  # Max-heap (storing elements as negative values)
        ans = []
        
        for i in range(k):
            heapq.heappush(pq, (-nums[i], i))  # Store (negative value, index)
        
        ans.append(-pq[0][0])  # Get max by negating the top element
        
        for j in range(k, len(nums)):
            heapq.heappush(pq, (-nums[j], j))  # Push new element
            
            # Remove elements that are out of the window
            while pq[0][1] <= j - k:
                heapq.heappop(pq)  # Remove outdated elements
            
            ans.append(-pq[0][0])  # Get max from the top element
        
        return ans
