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
     * @return {number[]}
     */
    /*
    The way to solve this problem is a modified level order
    traversal by putting right child first and then discarding
    all the other nodes at the same depth and doing this 
    depth by depth
    */
    rightSideView(root) {
        if (!root) return []
        const queue = [[root, 0]]; 
        const ans = [];
        let i = 0;
        while (i < queue.length) {
            const [node, depth] = queue[i++];
            if (!node) continue;

            ans.push(node.val);
            // it is important to push the right node before the left
            // so that the first node to come out it the right side
            if (node.right) queue.push([node.right, depth + 1]);
            if (node.left) queue.push([node.left, depth + 1]);

            while (i < queue.length && queue[i][1] == depth) {
                // discard all other nodes at the same depth
                const [n, d] = queue[i++];
                if (n.right) queue.push([n.right, depth + 1]);
                if (n.left) queue.push([n.left, depth + 1]);
            }
        }

        return ans;
    }
}
