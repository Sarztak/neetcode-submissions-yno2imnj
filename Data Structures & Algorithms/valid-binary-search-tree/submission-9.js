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
    // the only point to remember is that just checking node.val is not sufficient
    // as the nodes need to consider all the ancestors all the way up to the root
    // so the bounds needs to be passed. 
    // this of this as a rod that gets lower and lower as you go more and more to the left
    // and you need to go even lower that the rod. 
    // when you go to the right you need to jump above the rod and the height gets higher and higher
    /*
    The lower bound for the right subtree is the max that has been found so far
    The upper bound for the left subtree is the min that has been found so far.
    Each right tree and its child need to have value greater than its parent it is the principal
    Therefore we have a series of progressively increasing lower bounds as we mode right down
    The same argument can be made for the left subtree that all the values to the left
    should have values less that the parent. Hence we have progressively descreasing upper bounds.
    */
    foo(node, lower_bound, upper_bound) {
        if (!node) return true;
        if (node.val <= lower_bound || node.val >= upper_bound) return false
        return this.foo(node.left, lower_bound, node.val) && this.foo(node.right, node.val, upper_bound);
    };

    isValidBST(root) {
        return this.foo(root, -Infinity, Infinity);
    }
}
