// 200. Number of Islands

class Solution {
private:
    void bfs(int row, int col, vector<vector<int>>& visited, vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        visited[row][col] = 1;
        queue<pair<int, int>> q;
        q.push({row, col});
        
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        while (!q.empty()) {
            int currentRow = q.front().first;
            int currentCol = q.front().second;
            q.pop();
            
            for (auto dir : directions) {
                int newRow = currentRow + dir.first;
                int newCol = currentCol + dir.second;
                
                if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < m 
                    && grid[newRow][newCol] == '1' && !visited[newRow][newCol]) {
                    visited[newRow][newCol] = 1;
                    q.push({newRow, newCol});
                }
            }
        }
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int count = 0;
        vector<vector<int>> visited(n, vector<int>(m, 0));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && grid[i][j] == '1') {
                    bfs(i, j, visited, grid);
                    count++;
                }
            }
        }
        return count;
    }
};
