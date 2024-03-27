class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) {
            return 0;
        }
        
        int count = 0;
        int product = 1;
        int first = 0;
        
        for (int last = 0; last < nums.length; last++) {
            product *= nums[last];
            while (product >= k) {
                product /= nums[first];
                first++;
            }
            count += last - first + 1;
        }
        
        return count;
    }
}