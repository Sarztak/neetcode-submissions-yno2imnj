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
     * @param {number} target
     * @return {TreeNode}
     */
    removeLeafNodes(root, target) {
        function foo(node) {
            if (node && !node.right && !node.left && node.val == target) {
                return null
            }

            if (node.left) {
                node.left = foo(node.left);
            }

            if (node.right) {
                node.right = foo(node.right);
            }

            if (node.val == target && !node.right && !node.left) {
                return null
            }

            return node;
        }

        return foo(root);
    }
}
