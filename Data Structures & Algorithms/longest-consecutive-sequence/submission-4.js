class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const set = new Set(nums);
        let maxLen = 0;
        set.forEach(s => {
            let n = s;
            if (!set.has(n - 1)) {
                // n - 1 is not in the set, then s is the starting point
                let currLen = 1;
                while (set.has(n + 1)) {
                    currLen ++;
                    n ++;
                }
                maxLen = Math.max(maxLen, currLen)
            }
        })

        return maxLen
    }

}
