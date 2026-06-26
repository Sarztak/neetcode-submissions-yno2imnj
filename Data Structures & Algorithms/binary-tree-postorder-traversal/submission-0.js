/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    /**
     * @param {TreeNode} root
     * @return {number[]}
     */
    postorderTraversal(root) {
        if (!root) return [];
        const ans = [];
        const stack = [root];
        
        while(stack.length > 0) {
            const curr = stack.pop();
            ans.push(curr.val);
            if (curr.left) stack.push(curr.left);
            if (curr.right) stack.push(curr.right);
        }

        return ans.reverse()
    }
}
