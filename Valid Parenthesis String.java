class Solution {
    public boolean checkValidString(String s) {
        int ptr1 = 0;
        for (char i : s.toCharArray()) {
            if (i == '(' || i == '*') {
                ptr1++;
            } else if (i == ')') {
                ptr1--;
            }
            if (ptr1 < 0) {
                return false;
            }
        }
        int ptr2 = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            char ch = s.charAt(i);
            if (ch == ')' || ch == '*') {
                ptr2--;
            } else if (ch == '(') {
                ptr2++;
            }
            if (ptr2 > 0) {
                return false;
            }
        }
        return true;
    }
}