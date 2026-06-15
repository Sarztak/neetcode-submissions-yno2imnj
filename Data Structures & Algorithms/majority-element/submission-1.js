class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums) {
        const map = new Map();
        nums.forEach(n => {
            map.set(n, (map.get(n) || 0) + 1);
        })
        for (const [key, value] of map) {
            if (value > Math.floor(nums.length / 2)) {
                return key;
            }
        }
    }
}
