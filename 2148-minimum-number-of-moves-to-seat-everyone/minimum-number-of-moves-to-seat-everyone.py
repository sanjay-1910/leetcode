class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        c=0
        for i in range(0,len(seats)):
            ab=abs(students[i]-seats[i])
            c=c+ab
        return c
        