def countSubarrays(nums, k):
  """
  Count the number of subarrays with score less than k.
  Score of a subarray is defined as sum * length

  Args:
    nums: List[int] - the input array of integers (positive only) 
    k: int - the maximum score allowed

  Returns:
    int - the count of subarrays with score < k
  """
  if not nums or k <= 0:
    return 0

  count = 0
  curr_sum = 0
  start = 0

  for end in range(len(nums)):
    # Add the current element to our running sum 
    curr_sum += nums[end]

    # Calculate current score: sum * length
    # Length of current window is (end - start + 1)
    while start <= end and curr_sum * (end - start + 1) >= k:
      curr_sum -= nums[start]
      start +=  1

    count += (end - start + 1)
  return count
