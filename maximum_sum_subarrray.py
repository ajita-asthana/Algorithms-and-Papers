# Brute Force Solution in O(n2)
max_sum = float('-inf')
for i in range(len(nums)):
  curr_sum = 0
  for j in range(i, len(nums)):
    current_sum += nums[j];
    max_sum = max(max_sum, current_subarray);

return max_sum


Kadane's algorithm

max_sum = nums[0]
curr_sum = nums[0]

for i in range(1, len(nums)):
  curr_sum = max(curr_sum + nums[i], nums[i])
  max_sum = max(max_sum, curr_sum)

return max_sum

