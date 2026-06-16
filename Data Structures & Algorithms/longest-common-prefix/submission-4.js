class Solution {
    /**
     * @param {string[]} strs
     * @return {string}
     */
    longestCommonPrefix(strs) {
        const sorted = strs.sort();
        const n = Math.min(sorted[0].length, sorted[sorted.length - 1].length);
        let i = 0;
        while (i < n) {
            if (sorted[0][i] != sorted[sorted.length - 1][i]) break;
            i ++;
        }
        return sorted[0].slice(0, i);
    }
}
