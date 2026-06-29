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
     * @param {number} val
     * @return {TreeNode}
     */
    insertIntoBST(root, val) {
        if (!root) return new TreeNode(val);
        let node = root;
        while (true) {
            // given that the val does not already exists 
            // in the tree val cannot be equal to a value
            // of the node which means it will either be 
            // more or else hence I am not comparing for 
            // equality.
            // also since it is given that there is a place
            // where the val will be place, I am not 
            // explicitly escaping the while loop
            if (val > node.val) {
                if (!node.right) {
                    const newNode = new TreeNode(val);
                    node.right = newNode;
                    return root;
                } else {
                    node = node.right;
                }
            } else {
                if (!node.left) {
                    const newNode = new TreeNode(val);
                    node.left = newNode;
                    return root;
                } else {
                    node = node.left;
                }
            }
        }
    }
}
