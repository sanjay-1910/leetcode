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
public:
    void traverse(TreeNode* root,int tot,int &c)
    {
        if(root==NULL)
        {
            return;
        }
        if(root->right==NULL && root->left==NULL)
        {
            c=c+(tot*10)+root->val;
            return;
        }
        tot=(tot*10)+root->val;
        traverse(root->left,tot,c);
        traverse(root->right,tot,c);
    }
    int sumNumbers(TreeNode* root) {
        int c=0;
        int tot=0;
        traverse(root,tot,c);
        return c;
    }
};