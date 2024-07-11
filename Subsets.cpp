// 78. Subsets

class Solution {
public:
void findCombination(int index, vector<int>& arr, vector<vector<int>>& res, vector<int>& ds) {
    if (index == arr.size()) {
        res.push_back(ds);
        return;
    }
    ds.push_back(arr[index]);
    findCombination(index + 1, arr, res, ds);
    ds.pop_back();
    findCombination(index + 1, arr, res, ds);
}
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> res;
        vector<int> ds;
        findCombination(0, nums, res, ds);
        sort(res.begin(), res.end());
        return res;
    }
};