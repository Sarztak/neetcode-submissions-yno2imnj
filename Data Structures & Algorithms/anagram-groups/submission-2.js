class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const map = new Map();
        strs.forEach(str => {
            const key = [...str].sort().join("");
            if(!map.has(key)) map.set(key, []);
            map.get(key).push(str);
        })
        return [...map.values()];
    }
}
