class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    majorityElement(nums) {
        let c1 = null;
        let c2 = null;
        let count1 = 0;
        let count2 = 0;

        for (let i = 0; i < nums.length; i ++) {
            if (count1 == 0 && c2 != nums[i]) {
                c1 = nums[i];
                count1 ++;
            } else if (c1 == nums[i]) {
                count1 ++;
            } else if (count2 == 0 && c1 != nums[i]) {
                c2 = nums[i];
                count2 ++;
            } else if (c2 == nums[i]) {
                count2 ++;
            } else {
                count1 --;
                count2 --;
            }
        }

        count1 = 0;
        count2 = 0;

        for (let i = 0; i < nums.length; i ++) {
            if (nums[i] == c1) {
                count1 ++;
            } else if (nums[i] == c2) {
                count2 ++;
            }
        }

        const ans = [];

        if (c1 != null && count1 > Math.floor(nums.length / 3)) {
            ans.push(c1);
        }

        if (c2 != null && count2 > Math.floor(nums.length / 3)) {
            ans.push(c2);
        }

        return ans
    }
}
