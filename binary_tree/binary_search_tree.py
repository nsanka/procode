# Check Binary Search Tree is valid or in-valid

# Define Node
class Node(object):
   def __init__(self, val, left=None, right=None) -> None:
      self.val = val
      self.left = left
      self.right = right

class Solution(object):
   def _isValidBSTHelper(self, n, low, high):
      # Empty Node is considered as Valid BST
      if not n:
         return True

      val = n.val
      if ((val > low and val < high) and
          self._isValidBSTHelper(n.left, low, val) and
          self._isValidBSTHelper(n.right, val, high)):
         return True
      return False

   def isValidBST(self, n):
      # Root node is between -inf to inf
      return self._isValidBSTHelper(n, float('-inf'), float('inf'))

#   5
#  / \
# 4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution().isValidBST(node))
# True

#   5
#  / \
# 4   7
#    /
#   2
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(2)
print(Solution().isValidBST(node))
# False