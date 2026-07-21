class Solution {
    /**
     * @param {number[]} stones
     * @return {number}
     */
    lastStoneWeight(stones) {
        const maxHeap = new MaxPriorityQueue();
        for (const stone of stones) {
            maxHeap.enqueue(stone);
        }

        while (maxHeap.size() > 1) {
            const heaviest = maxHeap.dequeue();
            const secondHeaviest = maxHeap.dequeue();
            if (heaviest == secondHeaviest) {
                continue;
            }
            maxHeap.enqueue(Math.abs(heaviest - secondHeaviest));
        }

        if (maxHeap.size() == 1) {
            return maxHeap.front();
        } else {
            return 0;
        }
    }
}
