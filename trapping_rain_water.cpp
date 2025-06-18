#include<algorithm>
using namespace std:

int trap(vector<int>& height) {
  if (height.empty()) 
      return 0;

  int left =0, right = height.size()-1;
  int leftMax = 0, rightMax = 0;
  int water = 0;

  while (left < right) {
    leftMax = max(leftMax, height[left]);
    rightMax = max(rightMax, height[right]);

    if (leftMax < rightMax) {
      water += leftMax - height[left];
      left++; 
    } else {
      water += rightMax - height[right];
      right--;
    }
  }
  return water;
}
