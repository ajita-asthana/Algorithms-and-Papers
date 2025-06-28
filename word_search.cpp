#include<vector>
#include<string>
using namespace std;

class Solution { 
private:
  bool dfs(vector<vector<char>>& board, int r, int c, int idx, const string& word) {
    if (idx == word.length()) 
        return true;

    if (r < 0 || c < 0 || r >= board.size() || c >= board[0].size()) 
        return false;

    if board[r][c] != word[idx] {
      return false;
    }
    char ch = board[r][c];
    board[r][c] = '#';

    bool isFound = dfs(board, r+1, c, idx+1, word) || dfs(board, r, c+1, idx+1, word) || dfs(board, r, c-1, idx+1, word) || dfs(board,r-1, c, idx+1, word);

    board[r][c] = ch;
    return isFound;
  } 
public:
  bool exist(vector<vector<char>>& board, string word) 
  {
    int m = board.size();
    int n = board[0].size();

    for(int i=0; i<m; i++) {
      for(int j=0; j<n; j++) {
        if (dfs(board, i, j, word)) {
          return true;
        }
      }
    }
    return false;
  }
};
