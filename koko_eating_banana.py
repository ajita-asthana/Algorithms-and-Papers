# [3, 6, 7, 11]
# 1.......sum(piles) 
#      m 
# 3 // 1 + 6 // 1 + 7 // 1 + 11 // 1 <= 8
# 3 // 4 + 6 // 4 + 7 // 4 + 11 // 4 <= 8 

res = float('inf')
l, r = 1, sum(piles)
while l <= r:
  mid = (l + r) // 2
  cur = 0
  for p in piles:
    cur += math.ceil(p / mid) 
  if cur <= h:
    res = min(res, mid)
    r = mid - 1
  else:
    l = mid + 1 
return res 
