# Check Binary Search Tree is valid or in-valid

# Define Node
#%%
class Node(object):
   def __init__(self, val, left=None, right=None) -> None:
      self.value = val
      self.left = left
      self.right = right

class Solution(object):
   def find_closest(self, node, number, prev_diff=float('inf'), closest=float('inf')):
      if node.value < number:
         if abs(node.value - number) < prev_diff:
            prev_diff = abs(node.value - number)
            closest = node.value
         if node.right:
            return self.find_closest(node.right, number, prev_diff, closest)
      elif node.value > number:
         if abs(node.value - number) < prev_diff:
            prev_diff = abs(node.value - number)
            closest = node.value
         if node.left:
            return self.find_closest(node.left, number, prev_diff, closest)
      else:
         return node.value
      return closest

#       7
#     /    \
#   3        12
#  / \      /  \
# 0    5   8     19
# \   /     \    / \
#  2  4     10  18  20
#%%
node = Node(7)
node.left = Node(3)
node.right = Node(12)
node.left.left = Node(0)
node.left.right = Node(5)
node.left.left.right = Node(2)
node.left.right.left = Node(4)
node.right.left = Node(8)
node.right.right = Node(19)
node.right.left.right = Node(10)
node.right.right.left = Node(18)
node.right.right.right = Node(20)
print(Solution().find_closest(node, 21))
# 20

#       15
#     /    \
#  -100     100
#   \
#    6
#   /  \
#  4     10
#%%
node = Node(15)
node.left = Node(-100)
node.right = Node(100)
node.left.right = Node(6)
node.left.right.left = Node(4)
node.left.right.right = Node(10)
print(Solution().find_closest(node, 12))
# 10
# %%
print(Solution().find_closest(node, 13))
# 15