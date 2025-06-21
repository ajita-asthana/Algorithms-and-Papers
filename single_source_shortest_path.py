import heapq
from collections import defaultdict
from typing import List, Dict, Tuple 

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Dict[int, int]:
  """
  Find shortest paths from start node to all other nodes using Dijkstra's algorithm.
  Args:
    graph: Adjacency list representation {node: [(neighbor, weight)...]}
    start: Starting node 

  Returns:
    Dictionary mapping each node to its shortest distance from start 
  """

  # Initialize distances - all nodes start at infinity except start 
  distances = defaultdict(lambda: float('inf')) 
  distance[start] = 0 

  # Priority queue: (distance, node)
  # We use distance as first element so heapq sorts by distance 
  pq = [(0, start)] 

# keep track of visited ndoes to avoid processing them multiple times 
visited = set() 

while pq:
  # get the node with minimum distance
  current_dist, current_node = heapq.heappop(pq)

  # skip if we've already processed this node 
  if current_node in visited:
    continue 

  # Mark as visited 
  visited.add(current_node)

  # check all neighbors
  if current_node in graph:
    for neighbor, weight in graph[current_node]:
      # skip if already visited
      if neighbor in visited:
        continue

    new_distance = current_dist + weight 

    # if we found a shorter path, update it
    if new_distance < distances[neighbor]:
      distances[neighbor] = new_distance
      heapq.heappush(pq, (new_distance, neighbor)) 

return dict(distances) 

def build_graph_from_edges(edges: List[List[int]]) -> Dict[int, List[Tuple[int, int]]]:
  graph = defaultdict(list)

  for edge in edges:
    from_node, to_node, weight = edge 
    graph[from_node].append((to_node, weight))
    graph[to_node].append((from_node, weight))

return graph 
