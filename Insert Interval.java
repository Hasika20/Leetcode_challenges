class Solution {
    public int[][] insert(int[][] inter, int[] newI) {
        int till = -1, from = -1;
        int n = inter.length;
        int[][] res;
        if(n == 0){
            res = new int[1][2];
            res[0] = newI;
            return res;
        }
        if(newI[1] < inter[0][0]){
            res = new int[n + 1][2];
            System.arraycopy(inter, 0, res, 1, n);
            res[0] = newI;
            return res;
        }
        for(int i = 0; i < n; i++){
            if(till == -1 && inter[i][1] >= newI[0])
                till = i;
            if(newI[1] < inter[i][0]){
                from = i - 1;
                break;
            }
            if(newI[1] == inter[i][0]){
                from = i;
                break;
            }
        }
        if(till == -1){
            res = new int[n + 1][2];
            System.arraycopy(inter, 0, res, 0, n);
            res[n] = newI;
            return res;
        }
        from = from == -1 ? n - 1 : from;
        newI[0] = Math.min(newI[0], inter[till][0]);
        newI[1] = Math.max(newI[1], inter[from][1]);

        res = new int[till + n - from][2];
        res[till] = newI;
        System.arraycopy(inter, 0, res, 0, till);
        System.arraycopy(inter, from + 1, res, till+1, n - from - 1);
        return res;
    }
}