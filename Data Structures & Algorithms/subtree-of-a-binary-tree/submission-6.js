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
     * @param {TreeNode} subRoot
     * @return {boolean}
     */
    // this problem is a good example of how to 
    // decompose the problem, first try to see if two trees are equal
    // which was done in the previous problem and then apply it to specific node
    // in this case to those in which subRoot value is equal to a node in the root

    isSameTree(p, q) {
        if (!p && !q) return true
        if (!(p && q) || p.val != q.val) return false
       return this.isSameTree(p.left, q.left) && this.isSameTree(p.right, q.right) && (p.val == q.val);
    }

    isSubtree(root, subRoot) {
        // try to find value at subRoot in the root tree
        if (!subRoot || !root) return false // should not happen since number of nodes are given to be 1 or more

        const stack = [root];
        while (stack.length > 0) {
            const node = stack.pop();
            if (!node) continue;
            if (node.val == subRoot.val) {
                const ans = this.isSameTree(node, subRoot);
                if (ans) return true;
            };

            stack.push(node.left);
            stack.push(node.right);
        }

        return false;
    }
}
