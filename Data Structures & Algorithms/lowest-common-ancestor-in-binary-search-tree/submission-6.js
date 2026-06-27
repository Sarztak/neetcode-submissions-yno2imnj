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

        // the idea is to find the path to both the nodes from the root which 
        // I am storing in the array and then after that start walking from 
        // the root after reversing the list and find the first value
        // that last value that is common to both, that will the deepest node
        // to do this find the index where they differ and then answer is i - 1 
        // in the path array that has length greater than i - 1
        // surely there are better ways to solve this problem 
        // the so called "elegant, orgasmic" methods that just brings tears 
        // but I am idiot so I will solve by whatever method I can when I don't
        // know what method is good or bad. 
        let i = 0;
        while (i < Math.min(pPath.length, qPath.length) && pPath[i].val == qPath[i].val) i++;
        return pPath[i - 1];
    }
}
