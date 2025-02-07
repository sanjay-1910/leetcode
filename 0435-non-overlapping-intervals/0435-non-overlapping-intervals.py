class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        # Step 1: Sort by the end time (Greedy approach)
        intervals.sort(key=lambda x: x[1])

        # Step 2: Track non-overlapping intervals
        prev_end = float('-inf')  # Track the end of the last included interval
        non_overlap_count = 0

        for start, end in intervals:
            if start >= prev_end:  # No overlap, include this interval
                prev_end = end
                non_overlap_count += 1  # Count this as non-overlapping
        
        # Step 3: Remove the overlapping ones
        return len(intervals) - non_overlap_count