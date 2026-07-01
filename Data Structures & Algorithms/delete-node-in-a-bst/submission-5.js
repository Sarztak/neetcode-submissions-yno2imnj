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
     * @param {number} key
     * @return {TreeNode}
     */
    // too difficult to do it with pointers and stack; several edges cases 
    // to resolve. 
    // I am not able to fully solve this by mythis and I don't understand 
    // fully how this works; I don't have faith in it
    // I feel quite disappointed; it seems like magic, which it should not be.
    // the way I understand is deleteNode returns the root of the tree after
    // deleting the said node. While searching the node with the value equal to the key
    // we descend into the left and right subtree however the root of the left and
    // right subtree is assigned back as CHILDREN, And this is perhaps the most confusing part
    // the return type is assigned back. WHAT is RETURED IS NOT A value but the NODE itthis.
    // then once the value is found and if one child is missing the other is simply returned.
    // the grandparent now point to the only child of the parent(node.val == key)
    // if there are two children the so called inorder successor is found, its value is copied
    // to the node and a deleteNode operation is called on the right child.
    deleteNode(node, key) {
        if (!node) return null;
        if (node.val < key) {
            node.right = this.deleteNode(node.right, key);
        } else if (node.val > key) {
            node.left = this.deleteNode(node.left, key);
        } else {
            if (!node.left) return node.right;
            if (!node.right) return node.left;

            let curr = node.right;
            while (curr.left) curr = curr.left;
            node.val = curr.val;
            node.right = this.deleteNode(node.right, curr.val);
        }
        return node;
    }
}


