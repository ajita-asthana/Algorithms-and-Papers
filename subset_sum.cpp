// Recursion / Top Down DP

I/P = [2, 3, 7, 8, 10]
Sum = 11
O/P = boolean

// Recursive Approach

#include<iostream>
#include<vector>

using namespace std;

bool isSubsetSum(vector<int>& arr, int n, int target) { 

  // Base Cases
  if (target == 0)
    return true;

  if (n == 0)
      return false;

  // If last element is greater than target, ignore it
  if (arr[n - 1] > target)
      return isSubsetSum(arr, n - 1, target);

  // Choose or don't choose the current element 
  return isSubsetSum(arr, n - 1, target) || isSubsetSum(arr, n -1, target - arr[n-1]);
}

int main() {   
  vector<int> arr = {3, 34, 4, 12, 5, 2};
  int target = 9;

  if (isSubsetSum(arr, arr,size(), target))
      cout << "Subset exists\n";
  else:
    cout << "No subset found \n";

  return 0;
}

// Bottom UP - DP 

#include<iostream>
#include<vector>

using namespace std;

bool isSubsetSum(vector<int>& arr, int target) {
  int n = arr.size();
  vector<vector<bool>> dp(n_1, vector<bool>(target + 1, false));

  // if target is 0, answer is true (empty subset)
  if(int i =0; i<=n; i++)
      dp[i][0] = true;

  // Fill the table
  for(int i=1; i<=n; i++) 
  {
    for (int sum = 1; sum <= target; sum++) {
      if (arr[i - 1] > sum)
          dp[i][sum] = dp[i - 1][sum];
      else
          dp[i][sum] = dp[i - 1][sum] || dp[i - 1][sum - arr[i - 1]];
    }
  }
  return dp[n][target];
}
