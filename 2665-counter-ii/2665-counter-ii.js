/**
 * @param {integer} init
 * @return {Object}
 */
var createCounter = function(init) {
    let currentValue = init;
    
    return {
        increment: function() {
            currentValue++;
            return currentValue;
        },
        decrement: function() {
            currentValue--;
            return currentValue;
        },
        reset: function() {
            currentValue = init;
            return currentValue;
        }
    };
};
