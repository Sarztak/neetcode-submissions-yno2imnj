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
        const stack = [];
        let curr = root;
        const ans = [];

        while (curr || stack.length > 0) {
            while (curr) {
                stack.push(curr);
                curr = curr.left; // if left is null then while loop will stop
            }
            
            curr = stack.pop();
            ans.push(curr.val);

            curr = curr.right; // if right is null then while loop will catch it else if stack is not empty we move on. 
        }

        return ans
    }
}
