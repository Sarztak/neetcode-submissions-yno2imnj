class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    findKthLargest(nums, k) {
        const minHeap = new MinPriorityQueue();
        for (const n of nums) {
            minHeap.enqueue(n);
        }
        while(minHeap.size() > k) {
            minHeap.dequeue();
        }
        return minHeap.front();
    }
}
