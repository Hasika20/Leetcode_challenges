class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_val = max(nums)
        count = i = max_count = 0
        n = len(nums)
        for j in range(n):
            if nums[j] == max_val:
                max_count += 1
            while max_count == k:
                if nums[i] == max_val:
                    max_count -= 1
                i += 1
            count +=i
        return count
