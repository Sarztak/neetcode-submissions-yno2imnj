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
     * @return {number}
     */
    // maybe only when it happens for either good or bad
    // that we can imagine that possiblities beyond the current
    // even exists.
    diameterOfBinaryTree(root) {
        let maxDiameter = 0;
        function walk(node) {
            if (!node) return 0; // this is different from the return type, here null return to node hence answer is 0
            const leftDepth = walk(node.left);
            const rightDepth = walk(node.right);
            
            maxDiameter = Math.max(maxDiameter, leftDepth + rightDepth);
            
            // here node return to node therefore 
            // that path counts as 1, which is different from null -> node
            return Math.max(leftDepth, rightDepth) + 1; 
        };

        walk(root);
        return maxDiameter;
    }
    
}
