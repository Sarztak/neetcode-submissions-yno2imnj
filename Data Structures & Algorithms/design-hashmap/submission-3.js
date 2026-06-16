class MyHashMap {
    constructor() {
        this.arr = [];
    }

    /**
     * @param {number} key
     * @param {number} value
     * @return {void}
     */
    put(key, value) {
        if (this.arr.length > key) {
            this.arr[key] = value;
        } else {
            // using push(...new Array) causes the call stack to blow up because
            // millions of parameters might be passed to the push method
            // so concat should be used, but concat does not modify in place :)
            this.arr = this.arr.concat(new Array(key + 1 - this.arr.length).fill(-1));
            this.arr[key] = value;
        }
    }

    /**
     * @param {number} key
     * @return {number}
     */
    get(key) {
        if (this.arr.length > key) {
            return this.arr[key];
        } else {
            return -1
        }
    }

    /**
     * @param {number} key
     * @return {void}
     */
    remove(key) {
        if (this.arr.length > key) {
            this.arr[key] = -1
        }
        return null 
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * var obj = new MyHashMap()
 * obj.put(key,value)
 * var param_2 = obj.get(key)
 * obj.remove(key)
 */
