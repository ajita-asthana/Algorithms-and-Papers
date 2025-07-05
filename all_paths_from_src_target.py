from collections import defaultdict
from typing import List 

class Solution:
  def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    adjLst = defaultdict(list)
    visited = [False] * n 

    for edge in edges:
      adjLst[edge[0]].append(edge[1])

    def backtrack(adjLst, src, dest, visited):
      if visited[src]:
        return src == dest 

      if src not in adjLst:
        return src == dest 

      visited[src] = True 
      for next_node in adjLst[src]:
        if not backtrack(adjLst, next_node, dest, visited):
          return False
      visited[src] = False 
      return True 

  return backtrack(adjLst, source, destination, visited)
