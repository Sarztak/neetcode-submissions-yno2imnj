class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    subarraySum(nums, k) {
        const ans = [];
        const map = new Map();
        map.set(0, [0]);
        let prefixSum = 0; // prefixSum is sum of first k elements
        for (let j = 0; j < nums.length; j ++) {
            prefixSum = prefixSum + nums[j]  // for j = 0 that is first element prefixSum
            if (map.has(prefixSum - k)) {
                const idx = map.get(prefixSum - k);
                // i represents that prefix sum of first i elements
                // so what is stored in the map is how many first i elements
                // give that prefixSum
                // if I need to convert from i to actual index then it will be i - 1
                idx.forEach(i => {
                    if (i < j + 1) {
                        ans.push(nums.slice(i, j + 1));
                    }
                });
            }
            const arr = map.get(prefixSum) || []; 
            arr.push(j + 1); // push j + 1 because j is actual index into the array
            map.set(prefixSum, arr);
        }
        console.log(ans, map);
        return ans.length
    }
}
