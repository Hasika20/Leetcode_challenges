// 46. Permutations

class Solution {
    private:
        void findPermutation(int index, vector<int>& nums, vector<vector<int>>& res) {
            if (index == nums.size()) {
                res.push_back(nums);
                return;
            }
            for(int i = index; i < nums.size(); i++) {
                swap(nums[index], nums[i]);
                findPermutation(index + 1, nums, res);
                swap(nums[index], nums[i]);
            }
        }
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        findPermutation(0, nums, res);
        return res;
    }
};