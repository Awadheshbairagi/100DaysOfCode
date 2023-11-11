class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Handle division by zero
        if denominator == 0:
            return "Undefined"

        # Handle the sign
        sign = "" if numerator * denominator >= 0 else "-"
        numerator, denominator = abs(numerator), abs(denominator)

        # Calculate the integer part
        integer_part = numerator // denominator
        remainder = numerator % denominator

        # If remainder is zero, return the integer part only
        if remainder == 0:
            return sign + str(integer_part)

        # Initialize the result with the integer part
        result = sign + str(integer_part) + "."

        # Use a dictionary to store the index of the remainder for each step
        remainder_dict = {}
        recurring_part = ""
        index = len(result)

        while remainder != 0:
            # If the remainder is repeating, break the loop
            if remainder in remainder_dict:
                index = remainder_dict[remainder]
                recurring_part = result[index:]
                break

            remainder_dict[remainder] = index
            quotient = remainder * 10 // denominator
            result += str(quotient)
            remainder = remainder * 10 % denominator
            index += 1

        # If there is a recurring part, enclose it in parentheses
        if recurring_part:
            result = result[:index] + "(" + recurring_part + ")"

        return result
