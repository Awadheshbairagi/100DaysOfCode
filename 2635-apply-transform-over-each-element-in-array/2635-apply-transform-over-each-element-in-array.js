/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    var mappedArray = []; // Initialize an empty array to store the transformed values
    
    // Loop through the input array and apply the provided function to each element
    for (var i = 0; i < arr.length; i++) {
        // Call the provided function with the current element and its index
        var transformedValue = fn(arr[i], i);
        
        // Add the transformed value to the mappedArray
        mappedArray.push(transformedValue);
    }
    
    return mappedArray; // Return the transformed array
};
