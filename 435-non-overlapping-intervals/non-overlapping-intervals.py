class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        c = 1
        intervals.sort(key=lambda x: x[1])
        prev = intervals[0][1]
        for i in range(1, len(intervals)):
            sta,en = intervals[i][0],intervals[i][1]
            if(sta>=prev):
                prev = en
                c+=1
        return len(intervals)-c