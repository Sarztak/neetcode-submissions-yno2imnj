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
/**
 * Using inorder and preorder traversal to encode and decode tree will
 * only work if the node values are unique. In case they are not, then it does not work
 */
class Codec {
    /**
     * Encodes a tree to a single string.
     *
     * @param {TreeNode} root
     * @return {string}
     */


    levelOrder(root) {
        const queue = [root];
        let i = 0;
        const answer = [];
        while (i < queue.length) {
            const node = queue[i];
            if (!node) {
                answer.push('null');
                i ++;
                continue;
            } else {
                answer.push(String(node.val));
            };
            queue.push(node.left);
            queue.push(node.right);
            i ++;
        }
        return answer.join(',');

    }
    serialize(root) {
        const encoded = this.levelOrder(root);
        return encoded

    }

    /**
     * Decodes your encoded data to tree.
     *
     * @param {string} data
     * @return {TreeNode}
     */
    deserialize(data) {
        const nodes = data.split(',');
        if (nodes.length > 0 && nodes[0] == 'null') return null;
        const root = new TreeNode(parseInt(nodes[0], 10));
        const queue = [root];
        let i = 0;
        let j = 1;
        while (i < queue.length && j < nodes.length - 1) {
            const node = queue[i];
            if (nodes[j] != 'null') {
                const leftChild = new TreeNode(parseInt(nodes[j], 10));
                node.left = leftChild;
                queue.push(leftChild);
            }
            if (nodes[j + 1] != 'null') {
                const rightChild = new TreeNode(parseInt(nodes[j + 1], 10));
                node.right = rightChild;
                queue.push(rightChild);
            }
            j = j + 2;
            i = i + 1;
        }
        return root;
    }
}
