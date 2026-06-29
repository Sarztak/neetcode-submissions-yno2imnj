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
    // a trivial solution to the problem is to just collect
    // values of all the nodes, and rebuilt just a linked list
    // by sorting the values and creating essentially a right
    // sided tree with all the left node set to null. This  is
    // still a valid BST
    deleteNode(root, key) {
        if (!root) return null;
        const stack = [root];
        const values = [];
        while (stack.length > 0) {
            const node = stack.pop();
            if (!node) continue;
            values.push(node.val);
            stack.push(node.left);
            stack.push(node.right);
        }

        // sort the values
        values.sort((a, b) => a - b)
        const newRoot = new TreeNode();
        let curr = newRoot;
        for (let i = 0; i < values.length; i ++) {
            if (values[i] == key) continue
            const node = new TreeNode(values[i]);
            // always attach to the right child, since values are sorted
            curr.right = node;
            curr = curr.right;
        }

        return newRoot.right;
    }
}
