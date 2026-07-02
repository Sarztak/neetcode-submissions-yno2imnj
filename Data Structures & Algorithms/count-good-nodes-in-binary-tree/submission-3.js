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
    /*
    This is a quite simple problem, when the node is a left it will return a 0 or 1
    based on its own value and the previous maximum value and since it has no children a zero
    can be returned from left and right children and all subsequent node in the call will
    just count the values they receive from the left and right children and add one more
    if the node itself has value greater than the previous maximum. Also a stack or queue based
    approach cannot be used here since the path is important. Those approaches are good for 
    parsing and finding one specific thing in the tree easily.
    */
    foo(node, max_val) {
        const c3 = node.val >= max_val ? 1: 0;

        max_val = Math.max(max_val, node.val);
        
        const c1 = node.left ? this.foo(node.left, max_val) : 0;
        const c2 = node.right ? this.foo(node.right, max_val): 0;

        return c1 + c2 + c3;
    }

    goodNodes(root) {
        // root cannot be null as given that there is at least one node
        return this.foo(root, -Infinity);
    }
}
