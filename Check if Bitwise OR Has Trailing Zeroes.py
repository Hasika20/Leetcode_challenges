class Solution(object):
    def hasTrailingZeros(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Count the number of even numbers in the array
        even_count = sum(1 for num in nums if num % 2 == 0)

        # If there are at least two even numbers, return True
        return even_count >= 2
