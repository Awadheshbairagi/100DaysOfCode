/**
 * @param {number[]} nums
 * @return {void}
 */
var ArrayWrapper = function(nums) {
    this.array = nums;
};

/**
 * @return {number}
 */
ArrayWrapper.prototype.valueOf = function() {
    return this.array.reduce((acc, num) => acc + num, 0);
};

/**
 * @return {string}
 */
ArrayWrapper.prototype.toString = function() {
    return `[${this.array.join(',')}]`;
};
