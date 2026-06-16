class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const sorted = nums.map((val, idx) => [val, idx]).sort((a, b) => a[0] - b[0]);
        let l = 0;
        let h = nums.length - 1;
        while (l < h) {
            if (sorted[l][0] + sorted[h][0] == target) {
                const a = sorted[l][1];
                const b = sorted[h][1];
                return [Math.min(a, b), Math.max(a, b)];
            } else if (sorted[l][0] + sorted[h][0] < target) l ++;
            else h --;
        }

        return [-1, -1]
    }
}
