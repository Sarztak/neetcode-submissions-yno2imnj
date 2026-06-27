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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {boolean}
     */
    isSameTree(p, q) {
        // if both p and q are null then they are equal so return true
        if (!p && !q) return true
        // if either p is null or q is null or their values are not equal return false
        if (!(p && q) || p.val != q.val) return false
        // if left and right subtree are okay and the values are equal then return true else false
        return this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right) && (p.val == q.val);
    }
}
