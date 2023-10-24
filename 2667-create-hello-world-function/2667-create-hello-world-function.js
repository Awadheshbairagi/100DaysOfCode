function createHelloWorld() {
    return function() {
        return "Hello World";
    };
}

// Example usage
const f = createHelloWorld();

// Calling the function returned by createHelloWorld will always return "Hello World"
console.log(f()); // Output: "Hello World"

// No matter what arguments you pass, it will still return "Hello World"
console.log(f({}, null, 42)); // Output: "Hello World"
