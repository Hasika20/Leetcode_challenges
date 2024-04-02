class Solution {
    public boolean isIsomorphic(String s, String t) {
        List<Integer> S = new ArrayList<>();
        List<Integer> T = new ArrayList<>();
        for (char c : s.toCharArray()) {
            S.add(s.indexOf(c));
        }
        for (char c : t.toCharArray()) {
            T.add(t.indexOf(c));
        }
        return S.equals(T);
    }
}