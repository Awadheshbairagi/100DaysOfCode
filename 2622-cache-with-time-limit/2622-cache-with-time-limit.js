var TimeLimitedCache = function() {
    this.cache = new Map();
};

TimeLimitedCache.prototype.set = function(key, value, duration) {
    const currentTime = Date.now();
    const expirationTime = currentTime + duration;
    
    if (this.cache.has(key)) {
        this.cache.set(key, { value, expirationTime });
        return true;
    } else {
        this.cache.set(key, { value, expirationTime });
        return false;
    }
};

TimeLimitedCache.prototype.get = function(key) {
    const currentTime = Date.now();
    if (this.cache.has(key)) {
        const { value, expirationTime } = this.cache.get(key);
        if (expirationTime > currentTime) {
            return value;
        } else {
            this.cache.delete(key);
        }
    }
    return -1;
};

TimeLimitedCache.prototype.count = function() {
    const currentTime = Date.now();
    let count = 0;
    for (const [key, { expirationTime }] of this.cache) {
        if (expirationTime > currentTime) {
            count++;
        } else {
            this.cache.delete(key);
        }
    }
    return count;
};
