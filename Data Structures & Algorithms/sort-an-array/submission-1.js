class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    merge(arr1, arr2) {
        // merges two sorted array into one sorted array
        let merged = [];
        let i = 0;
        let j = 0;
        while (i < arr1.length && j < arr2.length) {
            if (arr1[i] < arr2[j]) { 
                merged.push(arr1[i]);
                i ++;
            } else {
                merged.push(arr2[j]);
                j ++;
            }
        }

        if (i == arr1.length) {
            merged = merged.concat(arr2.slice(j, arr2.length));
        } else if (j == arr2.length) {
            merged = merged.concat(arr1.slice(i, arr1.length));
        }

        return merged;
    }
    
    sortArray(nums) {
        if (nums.length == 2) {
            const [a, b] = nums;
            return [Math.min(a, b), Math.max(a, b)];
        } else if (nums.length <= 1) {
            return nums;
        }
        const mid = Math.floor(nums.length / 2);
        const mergedArray = this.merge(this.sortArray(nums.slice(0, mid)), this.sortArray(nums.slice(mid, nums.length)));
        return mergedArray;
    }
}
