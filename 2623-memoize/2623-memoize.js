function memoize(fn) {
    const cache = {};
    let callCount = 0;

    return function (...args) {
        const key = args.join("-");
        if (key in cache) {
            return cache[key];
        } else {
            callCount += 1;
            const result = fn(...args);
            cache[key] = result;
            return result;
        }
    }
}

function sum(a, b) {
    return a + b;
}

function fib(n) {
    if (n <= 1) {
        return 1;
    }
    return fib(n - 1) + fib(n - 2);
}

function factorial(n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}
