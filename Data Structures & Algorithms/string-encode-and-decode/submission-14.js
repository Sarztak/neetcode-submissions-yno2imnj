class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        if (strs.length == 0) return "null";
        return strs.map(str => [...str].map(c => String(c.charCodeAt(0))).join("&")).join("_");
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        if (str == "null") return []
        const strs = str.split("_");
        const ans = [];
        for (const s of strs) {
            if (s.length === 0) {
                // this step is important because parseInt("") does not give any error
                // but produces undefined and then String converts that to \x00
                ans.push(s);
                continue
            }
            const c = s.split("&");
            const word = [];
            for (const i of c) {
                const cc = String.fromCharCode(parseInt(i));
                word.push(cc);
            }
            ans.push(word.join(""));
        }
        return ans
    }

}
