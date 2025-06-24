# Leetcode problem: 297 

Serialize and Deserialize a Binary Tree. 
class Codec:
  def serialize(self, root):
    """
      Encode a tree into a single string. 
      :type root: TreeNode
      :rtype: str
    """
    def rserialize(root, string):
      """
      a recursive helper function for the serialize() function.
      """
      # Check base case
      if root is None:
        string += 'None,'
      else:
        string += str(root.val) + ','
        string = rserialize(root.left, string)
        string = rserialize(root.right, string)
      return string 
  return rserialize(root, '')

def deserialize(self, data):
  """
    Decodes your encoded data to tree. 
    :type data: str
    :rtype: TreeNode
  """

def rdeserialize(l):
  if l[0] == 'None':
    l.pop(0)
    return None 

  root = TreeNode(l[0])
  l.pop(0)
  root.left = rdeserialize(l)
  root.right = rdeserialize(l)
  return root 

