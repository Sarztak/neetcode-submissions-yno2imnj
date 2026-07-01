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
     * @return {number[][]}
     */
    levelOrder(root) {
        // there is no native queue in javascript so a pointer 
        // need to be maintained to track which element to remove.
        const queue = [[root, 0]]; // store the depth and the root. 
        let i = 0;
        const ans = [];
        while (i < queue.length) {
            const [node, depth] = queue[i++]; // post fix operator.
            if (!node) continue // to catch if the root node itself if null;
            if (ans.length > depth) {
                ans[depth].push(node.val);
            } else {
                ans.push([node.val]);
            }
            if (node.left) queue.push([node.left, depth + 1]);
            if (node.right) queue.push([node.right, depth + 1]);
        }
        return ans;
    }
}
