public class Solution {
    public int maxSubarrayLength(int[] v, int k) {
        int n = v.length;
        Map<Integer, Integer> m = new HashMap<>();
        int i = 0, j = 0, ans = 1;
        while (i < n && j < n) {
            m.put(v[j], m.getOrDefault(v[j], 0) + 1);
            while (m.get(v[j]) > k) {
                m.put(v[i], m.get(v[i]) - 1);
                i++;
            }
            ans = Math.max(ans, j - i + 1);
            j++;
        }
        return ans;
    }
}