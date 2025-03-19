class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        x = []
        for i in range(len(seats)):
            x.append(abs(seats[i]-students[i]))
        return sum(x)