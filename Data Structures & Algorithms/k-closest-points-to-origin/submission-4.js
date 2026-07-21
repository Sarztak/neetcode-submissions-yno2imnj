class Solution {
    /**
     * @param {number[][]} points
     * @param {number} k
     * @return {number[][]}
     */
    kClosest(points, k) {
        const minHeap = new MinPriorityQueue((item) => item[0]);
        for (const [x, y] of points) {
            const d = Math.sqrt(x * x + y * y);
            minHeap.enqueue([d, [x, y]]);
        }

        const ans = [];
        while (k > 0) {
            ans.push(minHeap.dequeue()[1]);
            k --;
        }

        return ans;
    }
}
