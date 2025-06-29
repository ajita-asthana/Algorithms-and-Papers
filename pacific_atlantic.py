# Pacific Atlantic Waterflow 
from typing import List
from collections import deque

class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    if not heights or not heights[0]:
      return []

    self.heights = heights
    self.m, self.n = len(heights), len(heights[0])

    pacific_queue = deque()
    atlantic_queue = deque() 

    for i in range(self.n):
      pacific_queue.append((0, i))
      atlantic_queue.append((self.m-1, i))

    for i in range(self.m):
      pacific_queue.append((i, 0))
      atlantic_queue.append((i, self.n-1))

    result = []
    for i in range(self.m):
      for j in range(self.n):
        if pacific_reachable[i][j] and atlantic_reachable[i][j]:
            result.append([i, j])

    return result
