class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        if (tickets[k] == 0) {
            return 0;
        }
        int i = 0;
        int time = 0;
        while (true) {
            if (tickets[i] > 0) {
                tickets[i]--;
                time++;
            }
            if (i == k && tickets[i] == 0) {
                return time;
            }
            i++;
            if (i == tickets.length) {
                i = 0;
            }
        }
    }
}