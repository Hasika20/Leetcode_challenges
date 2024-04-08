class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        m = len(sandwiches)
        i = 0
        while i < n:
            if students[i] == sandwiches[0]:
                sandwiches.pop(0)
                students.pop(i)
                n -= 1
                i = 0  # Reset index to start from the beginning
            else:
                i += 1
            if len(sandwiches) == 0:
                return 0
        return len(students)
        