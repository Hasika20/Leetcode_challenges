//39. Combination Sum

class Solution {
public:
void findCombination(int index, int target, vector <int> &arr, vector<vector<int>> &res, vector<int> &ds) {
    if (index == arr.size()) {
        if (target == 0) {
            res.push_back(ds);
        }
        return;
    }
    if (arr[index] <= target) {
        ds.push_back(arr[index]);
        findCombination(index, target - arr[index], arr, res, ds);
        ds.pop_back();
    }
    findCombination(index + 1, target, arr, res, ds);
}
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> ds;
        findCombination(0, target, candidates, res, ds);
        return res;
    }
};