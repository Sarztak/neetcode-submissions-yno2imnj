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
    /**
     * The problem in this case is the different role that are played by the max and val
     * The max is the max of a particular path that is compared against other paths, while the val
     * is the value of the downward path that is only ever added to the parent
     * In the base case the max needs to be set to -Infinity as a guard when all the values
     * are negative. Setting it to zero would mean that the max is zero though that value does not exists
     * Also, since val is only ever added to the value of the parent node, it needs to be zero for a null 
     * node because there is nothing to add. It also means do not extend this path downwards.
     */
    maxPathSum(root) {
        function foo(node) {
            if (!node) {
                return [-Infinity, 0];
            }

            const [leftMax, leftVal] = foo(node.left);
            const [rightMax, rightVal] = foo(node.right);

            const val = node.val + Math.max(leftVal, rightVal, 0);
            const max = Math.max(
                leftMax, 
                rightMax, 
                node.val + Math.max(leftVal, 0) + Math.max(rightVal, 0) 
            )

            return [max, val];
        };
        const [max] = foo(root);
        return max;
    }
}
