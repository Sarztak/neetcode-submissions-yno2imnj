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
     * @return {boolean}
     */
    /*
    The way I was thinking about this problem was 
    how I solved the last problem by. Both problem require finding 
    max height of the tree. And if the problem does not specific which
    height is mentioned then it means the max height or the longest
    path from that node to the right and the left. 
    So the procedure is simply to find the max height and then give
    a decision based on comparing the lengths of the left and right
    path height. But here to avoid checking all over the tree and 
    return even if one imbalanced node is found two thing needs to be 
    returned. One is the height and if that tree subtree was itself
    balanced or not.
    */
    isBalanced(root) {
        function walk(node) {
            if (!node) return [0, true];

            const [leftHeight, isLeftBalanced] = walk(node.left);
            const [rightHeight, isrightBalanced] = walk(node.right);

            const isBalanced = (isLeftBalanced 
                                && isrightBalanced 
                                && Math.abs(leftHeight - rightHeight) <= 1);
            return [Math.max(leftHeight, rightHeight) + 1, isBalanced];
        }

        const [_, ans] = walk(root);

        return ans
    }
}
