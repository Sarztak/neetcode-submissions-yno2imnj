class MyHashSet {
    constructor() {
        this.arr = [];
    }

    /**
     * @param {number} key
     * @return {void}
     */
    add(key) {
        if (this.arr.length > key) {
            this.arr[key] = key
        } else {
            // add that many -1 elements into the arr
            const temp = new Array(key + 1 - this.arr.length).fill(-1);
            this.arr.push(...temp);
            this.arr[key] = key;
        }
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        if (this.arr.length > key) {
            this.arr[key] = -1;
        } else {
            return null;
        }
    }

    /**
     * @param {number} key
     * @return {boolean}
     */
    contains(key) {
        return this.arr.length > key && this.arr[key] != -1;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * var obj = new MyHashSet()
 * obj.add(key)
 * obj.remove(key)
 * var param_3 = obj.contains(key)
 */
