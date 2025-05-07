# Sliding Window

## Problem: 
Given an array  ```nums[]``` and an integer  ```k```, find the length of the longest subarrat such that the sum of elements in the subarray is less than or equal to k.

## Approach:
If all numbers are non-negative, we can use a sliding window technique:

## Intuition:    
  * As long as the sum is ```<=k```, exoand the window
  * If the sum becomes ```>k```, shrink the window form the left until it becomes valid again.

## Example:

```
nums = [1, 2, 1, 0, 1, 1, 0]
k = 4 
```

```
def longest_subarray_with_sum_at_most_k(nums, k):
  left = 0
  curr_sum = 0
  max_len = 0

  for right in range(len(nums)):
    curr_sum += nums[right]

    while curr_sum > k:
      curr_sum -= nums[left]
      left += 1

    max_len = mx(max_len, right-left+1)

    return max_len
```
