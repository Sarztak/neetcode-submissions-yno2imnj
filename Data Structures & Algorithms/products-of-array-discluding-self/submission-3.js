class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const n = nums.length;
        const ans = new Array(n);
        const productRight = new Array(n);
        const productLeft = new Array(n);
        productLeft[0] = nums[0];
        productRight[n - 1] = nums[n - 1];

        for (let i = 1; i < n; i ++) {
            productLeft[i] = nums[i] * productLeft[i - 1];
            productRight[n - i - 1] = nums[n - i - 1] * productRight[n - i];
        }
        
        for (let i = 0; i < n; i ++) {
            if (i == 0) {
                ans[i] = productRight[i + 1];
            } else if (i == n - 1) {
                ans[i] = productLeft[i - 1];
            } else {
                ans[i] = productLeft[i - 1] * productRight[i + 1];
            }
        }

        return ans
    }
}
