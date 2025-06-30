# Linked List Insertion Sort 

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next 

  def __repr__(self):
    return f"{self.val} -> {self.next}"

class Solution:
  def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      prev = dummy
      # Find where to insert the current node   
      while prev.next and prev.next.val < curr.val:
        prev = prev.next 

      # Save the next node
      next_temp = curr.next 

      # Insert curr between prev and prev.next 
      curr.next = prev.next
      prev.next = curr 

      # Move to the next node 
      curr = next_temp

return dummy.next
