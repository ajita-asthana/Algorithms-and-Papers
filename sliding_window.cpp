# Problem Statement 
Given a string s, find the length of the longest substring without repeating characters.

  # Intuition
  * Using sliding window technique
      * You want a window where all characters are unique
      * Use a set to track characters in the current window 
      * Expand the window with right pointer
      * If a duplicate is found, move the right pointer forward until duplicate is removed.


#include <iostream>
#include <unordered_set>
#include <string>

  int lengthOfLongestSubstring(string s) {
    unordered_set<char> seen;
    int left = 0;
    int maxLen = 0;

    for(int right =0; right < s.length(); right++) {
      while(seen.find(s[right]) != seen.end()) {
          seen.erase(s[left]);
          left++;
      }
      seen.insert(s[right]);
      maxLen = max(maxLen, right - left + 1);
    }
  return maxLen;
}

int main() {
  string input = "abcabcbb";
  int result = lengthOfLongestSubstring(input);
  cout << "Length of longest substring without repeating characters is " << result << endl;
  return 0;
}
