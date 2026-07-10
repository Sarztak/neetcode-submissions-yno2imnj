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
     * The main thing to realize in this problem is that 
     * when you rob a parent node that affects both the left and
     * right child simultaneously and those decides are tied together
     * Therefore the decision to rob or not needs to be made from 
     * the left node all the way up to the root node by passing the values
     * if the current node was robbed or not and both decisions needs
     * to be passed up and then compared.
     */
    rob(root) {

        function foo(node) {
            if (!node) {
                return [0, 0]
            };

            const [leftSkipped, leftRobbed] = foo(node.left);
            const [rightSkipped, rightRobbed] = foo(node.right);

            // if I decided to rob the current node then I cannot
            // rob the immediate children
            const robbed = node.val + leftSkipped + rightSkipped;
            
            // if I don't decide to rob the current node then I can choose
            // to rob the immediate children or I can move on
            // so I take the max profit from this decision
            const skipped = Math.max(leftSkipped, leftRobbed) + 
            Math.max(rightSkipped, rightRobbed)

            return [skipped, robbed];
            
        };

        const [skipped, robbed] = foo(root);
        return Math.max(skipped, robbed)
    }
}
