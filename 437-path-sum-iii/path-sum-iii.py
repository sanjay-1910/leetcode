# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root, prefix, sumo, k, count):
        if root is None:
            return
        sumo += root.val
        if sumo == k:
            count[0] += 1
        if (sumo - k) in prefix:
            count[0] += prefix[sumo - k]
        prefix[sumo] += 1
        
        self.traversal(root.left, prefix, sumo, k, count)
        self.traversal(root.right, prefix, sumo, k, count)

        prefix[sumo] -= 1  # Backtrack to maintain correct prefix sums
        
    def pathSum(self, root: Optional['TreeNode'], targetSum: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 0  # To handle edge cases where the sum from root itself equals targetSum
        count = [0]  # Use a list to pass count by reference
        self.traversal(root, prefix, 0, targetSum, count)
        return count[0]

        