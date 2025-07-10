# Range sum BST problem 

#include<vector>

struct TreeNode {
  int val;  
  TreeNode* left;
  TreeNode* right;
TreeNode(int x) : val(x) , left(nullptr), right(nullptr) {}
};

class Solution { 
public:
  int rangeSumBST(TreeNode* root, int low, int high) {
    int res = 0;
    std::vector<int> lst;

    // Inorder function traversal
    std::function<void(TreeNode*)> in_order = [&](TreeNode* node) {
            if (!node) return;
            in_order(node->left);
            lst.push_back(node->val);
            in_order(node->right);
        };

    in_order(root);
    for(int num : lst ) {
        if num >= low && num <= high {
          res += num;
        }

    }
}

}
