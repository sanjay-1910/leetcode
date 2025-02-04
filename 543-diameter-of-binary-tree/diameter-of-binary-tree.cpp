/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int traversal(TreeNode* root, int &maximum) {
        if (root == NULL) {
            return 0; // Return height as 0 for NULL node
        }

        // Recursively calculate left and right subtree heights
        int ls = traversal(root->left, maximum);
        int rs = traversal(root->right, maximum);

        // Update the maximum diameter found so far
        maximum = max(maximum, ls + rs); 

        // Return height of the current node
        return max(ls, rs) + 1;
    }
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int maximum = 0;
        traversal(root, maximum);
        return maximum;
        
        
    }
};