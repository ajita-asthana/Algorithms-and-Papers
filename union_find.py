class UnionFind:
  def __init__(self, size):
    self.parent = [i for i in range(size)]
    self.rank = [1] * size 

  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x] 

  def union(self, x, y):
    rootX = self.find(x)
    rootY = self.find(y) 

    if rootX == rootY:
      return False

  # Union by rank 
  if self.rank[rootX] > self.rank[rootY]:
    self.parent[rootY] = rootY 
  elif self.rank[rootX] < self.rank[rootY]:
    self.parent[rootX] = rootY
  else:
    self.parent[rootY] = rootX
    self.rank[rootX] += 1

return True
