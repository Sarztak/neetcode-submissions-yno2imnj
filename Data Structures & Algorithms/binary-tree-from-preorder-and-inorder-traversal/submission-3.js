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
     * @param {number[]} preorder
     * @param {number[]} inorder
     * @return {TreeNode}
     */
    buildTree(preorder, inorder) {
        if (preorder.length == 0 || inorder.length == 0) {
            return null;
        }

        const root = new TreeNode(preorder[0]);

        let j = 0;

        while (j < inorder.length) {
            if (inorder[j] == root.val) break
            j ++;
        }

        const leftChild = this.buildTree(
            preorder.slice(1, j + 1), 
            inorder.slice(0, j)
        );

        const rightChild = this.buildTree(
            preorder.slice(j + 1, preorder.length),
            inorder.slice(j + 1, inorder.length)
        );

        root.left = leftChild;
        root.right = rightChild;

        return root;
    }
}
