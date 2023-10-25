/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    var val = init; // Initialize val with the provided init value
    
    // Loop through the input array and apply the provided function to each element
    for (var i = 0; i < nums.length; i++) {
        // Call the provided function with the current accumulated value and the current element
        val = fn(val, nums[i]);
    }
    
    return val; // Return the final reduced value
};
