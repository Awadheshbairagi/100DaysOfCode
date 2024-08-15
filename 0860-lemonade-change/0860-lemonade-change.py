class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Count of $5 and $10 bills in hand
        five_dollar_bills = 0
        ten_dollar_bills = 0

        # Iterate through each customer's bill
        for customer_bill in bills:
            if customer_bill == 5:
                # Just add it to our count
                five_dollar_bills += 1
            elif customer_bill == 10:
                # We need to give $5 change
                if five_dollar_bills > 0:
                    five_dollar_bills -= 1
                    ten_dollar_bills += 1
                else:
                    # Can't provide change, return false
                    return False
            else:  # customer_bill == 20
                # We need to give $15 change
                if ten_dollar_bills > 0 and five_dollar_bills > 0:
                    # Give change as one $10 and one $5
                    five_dollar_bills -= 1
                    ten_dollar_bills -= 1
                elif five_dollar_bills >= 3:
                    # Give change as three $5
                    five_dollar_bills -= 3
                else:
                    # Can't provide change, return false
                    return False
        # If we've made it through all customers, return true
        return True