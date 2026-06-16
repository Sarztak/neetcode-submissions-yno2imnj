class Solution {
    /**
     * @param {number[]} nums
     * @param {number} val
     * @return {number}
     */
    removeElement(nums, val) {
        let k = 0;
        const arr = [];
        for (let i = 0; i < nums.length; i ++) {
            if (nums[i] == val) continue;
            arr.push(nums[i])
        }
        for (let i = 0; i < arr.length; i ++) {
            nums[i] = arr[i];
        }
        return arr.length;
    }
}
