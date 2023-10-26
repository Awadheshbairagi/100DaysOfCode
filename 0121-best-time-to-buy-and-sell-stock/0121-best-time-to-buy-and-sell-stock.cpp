class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minPrice = INT_MAX; // Initialize minPrice to a large value
        int maxProfit = 0; // Initialize maxProfit to 0
        
        for (int price : prices) {
            if (price < minPrice) {
                minPrice = price; // Update minPrice if a lower price is found
            } else if (price - minPrice > maxProfit) {
                maxProfit = price - minPrice; // Update maxProfit if a higher profit is found
            }
        }
        
        return maxProfit;
    }
};
