class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = Counter(nums)
        for i, j in dict.items():
            if dict[i] > len(nums)/2:
                return i
        return -1

        