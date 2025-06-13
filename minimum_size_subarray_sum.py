# Given an array of positive integers nums and a positive integer target, return the minimal
length of a subarray whose sum is greater than or equal to target. If there is no such subarray return 0 instead. 

target = 7 
nums = [2,3,1,2,4,3] 

# Return the minimum length of a subarray whose sum is greater than or equal to target.

# Intuition:
  * Maintain a window [start, end] 
  * Expand end until the sum >= target 
  * Try shrinking from start to make the window smaller while keeping the sum >= target 
  * Track the minimum window size found


def minSubArrayLen(target, nums):
  left = 0
  total = 0
  min_len = float('inf') 

  for right in range(len(nums)):
    total += nums[right]

   while total >= target:
     min_len = min(min_len, right - left + 1)
     total -= nums[left] 
     left += 1 

  return min_len if min_len != float('inf') else 0
     
