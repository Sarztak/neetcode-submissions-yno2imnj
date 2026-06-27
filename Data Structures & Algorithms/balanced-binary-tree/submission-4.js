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
    Another approach to exists early is to throw an error
    By early mean not wait to get if the left and right subtrees were balanced or not
    */
    isBalanced(root) {
        class Unbalanced extends Error {};

        function walk(node) {
            if (!node) return 0;
            const leftHeight = walk(node.left);
            const rightHeight = walk(node.right);
            if (Math.abs(leftHeight - rightHeight) > 1) throw new Unbalanced(); // throw error and start unwiding the stack
            return Math.max(leftHeight, rightHeight) + 1
        }

        try {
            walk(root);
            return true;
        } catch (e){
            return false; 
        }
    }
}
