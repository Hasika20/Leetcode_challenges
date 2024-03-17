class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list=[]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if (nums[i] + nums[j] == target):
                    if i not in list and j not in list:
                        list.append(i)
                        list.append(j)
                        return list