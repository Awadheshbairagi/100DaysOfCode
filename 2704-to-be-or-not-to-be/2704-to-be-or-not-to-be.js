/**
 * @param {any} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function(compareVal) {
            if (val !== compareVal) {
                throw new Error("Not Equal");
            }
            return true;
        },
        notToBe: function(compareVal) {
            if (val === compareVal) {
                throw new Error("Equal");
            }
            return true;
        }
    };
};
