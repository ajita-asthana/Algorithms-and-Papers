class Solution:
  def maxArea(self, height: List[int]) -> int:
    # Two pointer approach
    a_pointer = 0
    b_pointer = len(height)
    max_area = 0 

    while a_pointer < b_pointer:
      if height[a_pointer] < height[b_pointer]:
        max_area = max(max_area, height[a_pointer] * (b_pointer - a_pointer))
        a_pointer += 1
      else:
        max_area = max(max_area, height[b_pointer] * (b_pointer - a_pointer))
  return max_area 
