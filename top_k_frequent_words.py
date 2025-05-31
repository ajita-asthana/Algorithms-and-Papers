from collections import Counter 
import heapq 

class Solution:
  def topKfrequent(self, words, k):
    # Step1 : Count word frequencies 
    count = Counter(words)

    # Step 2: Use a heap with custum sort: (-freq, word)
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)

    # Step 3: Extract top k more frequent 
    result = [heapq.heapop(heap)[1] for _ in range(k)]
    return result
