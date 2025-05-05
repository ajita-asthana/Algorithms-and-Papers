# Search in a rotated sorted array 

1. Find the pivot index (smallest element) in the rotated array
2. Determine which portion of the array to search based on the target value
3. Perform standard binary search in the appropiate section
```
class Solution {
public:
  int search(vector<int>&& nums, int target) {
    if(nums.empty())
        return -1;

    // Find the pivot point
    int left = 0;
    int right = nums.size() - 1;
    while (left < right) {
      int mid = left + (right - left) // 2;
      if (nums[mid] > nums[right]) {
        left = mid+1;
      } else {
        right = mid;
      }
    }

    // left is the smallest element
    int pivot = left;
    // Decide which half to search in 
    left = 0;
    right = nums.size() - 1;
    if(target >= nums[pivot] && target <= nums[right]) 
      left = pivot;   // Search in the right half
    else 
      right = pivot - 1;    // Search in the left half 

    while(left <= right) {
      int mid = left + (right - left) // 2;
      if (nums[mid] == target) {
        return mid;
      } else if (nums[mid] < target) {
          left = mid + 1;
      } else {
          right = mid - 1;
      }
    }
    return -1;
  }
}
```
