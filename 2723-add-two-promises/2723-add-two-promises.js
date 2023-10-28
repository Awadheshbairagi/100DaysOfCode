/**
 * @param {Promise} promise1
 * @param {Promise} promise2
 * @return {Promise}
 */
var addTwoPromises = async function(promise1, promise2) {
  // Wait for the first promise to resolve and retrieve its value
  const value1 = await promise1;

  // Wait for the second promise to resolve and retrieve its value
  const value2 = await promise2;

  // Return a new promise that resolves with the sum of the values
  return value1 + value2;
};
