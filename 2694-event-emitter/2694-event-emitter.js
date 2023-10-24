class EventEmitter {
    constructor() {
        this.subscriptions = [];
    }

    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    subscribe(eventName, callback) {
        const subscription = { eventName, callback };
        this.subscriptions.push(subscription);

        return {
            unsubscribe: () => {
                const index = this.subscriptions.indexOf(subscription);
                if (index !== -1) {
                    this.subscriptions.splice(index, 1);
                }
            }
        };
    }

    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        const results = [];

        for (const subscription of this.subscriptions) {
            if (subscription.eventName === eventName) {
                results.push(subscription.callback(...args));
            }
        }

        return results;
    }
}
