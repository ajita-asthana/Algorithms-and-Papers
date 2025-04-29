def longestSubarrayDistinct(nums):
  """
  Find the length of the longest subarray containing distince elements.
  Args:
    nums: List[int] - the input array of integers 
  Returns:
    int - the length of the longest subarray with all distinct elements
  """
  if not nums:
      return 0

  # Dictionary to store the most recent index of each element
  last_seen = {}
  start =  0
  max_length = 0 

  for end in range(len(nums)):
    # If we've seen this element before and it's in our current window
    if nums[end] in last_seen and last_seen[nums[end]] >= start:
      # Move start to the position right after the last occurence
      start = last_seen[nums[end]] + 1

    # Update the last seen position of the current element
    last_seen[nums[end]] = end

    # Update the maximum length if current window is longer
    curr_length = end - start + 1
    max_length = max(max_length, current_length)

  return max_length
