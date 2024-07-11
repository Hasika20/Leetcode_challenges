class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return low

        def find_right(nums, target):
            low, high = 0, len(nums) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] <= target:
                    low = mid + 1
                else:
                    high = mid - 1
            return high

        left = find_left(nums, target)
        right = find_right(nums, target)

        if left <= right and left < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        else:
            return [-1, -1]
