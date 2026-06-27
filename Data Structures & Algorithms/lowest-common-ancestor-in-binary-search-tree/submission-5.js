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
     * @param {TreeNode} p
     * @param {TreeNode} q
     * @return {TreeNode}
     */
    lowestCommonAncestor(root, p, q) {

        function walk(node, target) {
            if (!node) return [];
            if (node.val == target) return [node];

            const left = walk(node.left, target);
            const right = walk(node.right, target);

            if (left.length > 0) {
                left.push(node);
                return left
            } else if (right.length > 0) {
                right.push(node);
                return right;
            }  else {
                return [];
            }
        }
        // they say p and q will exist in the tree so I am not checking whether they are null or not
        const pPath = walk(root, p.val).reverse();
        const qPath = walk(root, q.val).reverse();

        let i = 0;
        while (i < Math.min(pPath.length, qPath.length) && pPath[i].val == qPath[i].val) i++;
        return pPath[i - 1];
        // if (i - 1 < pPath.length) return  pPath[i - 1];
        // else return qPath[i - 1];
    }
}
