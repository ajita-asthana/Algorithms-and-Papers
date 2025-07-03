#include<unordered_set>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
  int longestConsecutive(vector<int>& nums) {
    unordered_set<int> num_set(num.begin(), nums.end());
    int max_seq_len = 0;

    for(int num: num_set) {
      if(num_set.find(num-1) == num_set.end()) {
        int curr_num = num;
        int curr_seq_len = 1;

        while(num_set.find(curr_num + 1) != num_set.end()) {
          curr_num++;
          curr_seq_len++;
        }

        max_seq_len = max(max_seq_len, curr_seq_len);
      }
    }
    return max_seq_len;
  }
}
