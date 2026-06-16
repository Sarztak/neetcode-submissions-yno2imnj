class Solution {
    /**
     * @param {number[]} nums
     * @return {void} Do not return anything, modify nums in-place instead.
     */
    sortColors(nums) {
        let i = 0;
        let j = 0;
        for (let k = 0; k < nums.length; k ++) {
            if (nums[k] == 0 && i < nums.length) {
                const t = nums[i];
                nums[i] = nums[k];
                nums[k] = t;
                i ++;
            }
        }
        
        j = i;

        for (let k = i; k < nums.length; k ++) {
            if (nums[k] == 1 && j < nums.length) {
                const s = nums[j];
                nums[j] = nums[k];
                nums[k] = s;
                j ++;
            }
        }
    }
}
