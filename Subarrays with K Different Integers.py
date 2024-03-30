class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most(nums, k) - self.at_most(nums, k-1)
    
    def at_most(self, nums, k):
        hm = {}
        l = 0
        cnt = 0
        for r in range(len(nums)):
            hm[nums[r]] = hm.get(nums[r], 0) + 1
            while len(hm) > k:
                hm[nums[l]] -= 1
                if hm[nums[l]] == 0:
                    hm.pop(nums[l])
                l += 1
            cnt += r - l + 1
        return cnt