class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = Counter(nums)
        for i,j in a.items():
            if j < 2:
                return i


        
            
        