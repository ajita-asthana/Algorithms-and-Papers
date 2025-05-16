# Reverse Nodes in K-Group

The "Reverse Nodes in k-Group" problem is a challenging problem extension of linked list manipulation. Let me explain this problem and walk through a solution. 

Problem Description

Given a linked list, reverse the nodes of the list k at a time and return the modified list. If the number of nodes is not a multiple of k, then the remaining nodes should 
be left as is. 

For example:
  Input: 1->2->3->4->5, k = 2
  Output: 2->1->4->3->5


  Input 1->2->3->4->5, k=3
  Output 3->2->1->4->5

# Approach 
This problem requires caredul pointer manipulatiom. Here's a step-by-step approach:

1. Count the number of nodes to determine how many complete groups of k we have
2. For each complete group
    * Reverse k nodes 
    *Connect the reversed group back to the main list 

3. Leave any remaining nodes (fewer than k) unchanged

## Understanding "Reverse Nodes in K-Group"

This problem is one of the more challenging linked list manipulation problems and is a common interview question at top tech companies. Let me break down the key components to understand it thoroughly. 

## Problem Core
You're given a linked list and a number k. You task is to reverse each consecutive group of k nodes, and if there are fewer than k nodes left at the end, leave them as is. 

1. Multiple Pointer Management: Youi need to keep track of several pointers simultaneously
2. Boundary Conditions: Connecting the reversed groups correctly with the rest of the list.
3. Edge Cases: Handling situations like k=1, empty lists or groups shorter than k nodes. 

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next 
  def reverseKGroup(head, k):
    """
    Reverse nodes in k-group in a linked list.
    Args:
      head: Head of the linked list 
      k: Group size for reversal 
    Returns:
      Head of the modified linked list
    """

# Count the nodes in the list 
count = 0 
current = head 
while current:
  count += 1
  current = current.next 

# Create a dummy node to simplify edge cases 
dummy = ListNode(0)
dummy.next = head 

# Prev points to the node before each k-group 
prev = dummy 
curent = head 

# Process complete k-groups
# We use the count to determine how many complete groups we have 
for _ in range(count // k):
  # Variables to keep track of the group 
group_prev = prev 
group_first = current 

# Reverse k nodes 
for i in range(k):
    next_temp = current.next 
    current.next = prev 
    prev = current 
    current = next_temp

group_prev.next = prev
group_first.next = current 

# Prepare for the next group 
prev = group_first 

return dummy.next 

# Helper function to create a linked list from a list of values
def create_linked_list(values):
  if not values:
    return None 

  head = ListNode(values[0])
  current = head 

  for val in values[1:]:
    current.next = ListNode(val)
    current = current.next 
  return head 

# Helper function to convert linked list to list for printing 
def linked_list_to_list(head):
  result = []
  current = head 

  while current:
    result.append(current.val)
    current = current.next
    
  return result 

# Test Cases 
def test_reverse_k_group():
# Test Case 1: k = 2
  list1 = create_linked_list([1,2,3,4,5])
  result1 = reverseKGroup(list1, 2)
  print(f"k=2: {linked_list_to_list(result1)}")


  # Test case 2: k =3 
list2 = create_linked_list([1,2 ,3,4, 5])
result2 = reverseKGroup(list2, 3)
print(f"k=2: {linked_list_to_list(result2)}") # Expected: [3,2,1,4,5]


  

  
