class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const map = new Map();
        nums.forEach(n => {
            map.set(n, (map.get(n) || 0) + 1);
        });
        
        const bucket = new Array(nums.length + 1).fill(null).map(() => []);
        
        map.forEach((value, key) => {
            bucket[value].push(key);
        });
        const ans = [];
        let i = nums.length;
        while (k != 0 && i > 0) {
            if (bucket[i].length != 0) {
                let j = 0;
                while (k != 0 && j < bucket[i].length) {
                    ans.push(bucket[i][j]);
                    j ++;
                    k --;
                }
            }
            i --;
        }

        return ans;
    }

}
