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
    int Depth(TreeNode* node){
        int count_l=0,count_r=0;
        if(node==NULL)return 0;
        count_l=Depth(node->left);
        count_r=Depth(node->right);
        if(count_l==-1|| count_r==-1){
            return -1;
        }
        if(abs(count_l-count_r)>=2)return -1;
        return max(count_l,count_r)+1;
    }
    bool isBalanced(TreeNode* root) {
        int ans=-1;
        ans=Depth(root);
        if(ans==-1)return false;
        return true;
    }
};