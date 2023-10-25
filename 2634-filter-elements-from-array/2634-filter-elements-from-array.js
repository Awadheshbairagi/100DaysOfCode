/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    var filteredArr = []; // Initialize an empty array to store filtered values
    
    // Loop through the input array and apply the provided function to each element
    for (var i = 0; i < arr.length; i++) {
        // Call the provided function with the current element and its index
        var shouldInclude = fn(arr[i], i);
        
        // Check if the function returns a truthy value, if yes, add the element to the filtered array
        if (shouldInclude) {
            filteredArr.push(arr[i]);
        }
    }
    
    return filteredArr; // Return the filtered array
};
