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
     * @return {TreeNode}
     */
    invertTree(root) {
        if (!root) return null;
        const stack = [root];
        while(stack.length > 0) {
            console.log(stack);
            const node = stack.pop();
            if (!node) continue;
            const temp = node.left;
            node.left = node.right;
            node.right = temp;
            stack.push(node.right);
            stack.push(node.left);
        }
        return root;
    }
}
