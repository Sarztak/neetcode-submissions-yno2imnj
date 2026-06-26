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
    inorderTraversal(root) {
        const ans = [];
        const stack = [];
        let curr = root;

        while (stack.length > 0 || curr) {
            while(curr) {
                stack.push(curr);
                curr = curr.left;
            }

            curr = stack.pop();
            ans.push(curr.val);
            curr = curr.right;
        }
        return ans;
    }
}
