class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior_count = 0

        # Iterate through each passenger's details
        for passenger_info in details:
            # Extract the age from the passenger_info string
            # Age is located at index 11 and 12 (2 characters)
            age = int(passenger_info[11:13])

            # Check if the passenger is a senior (strictly over 60 years old)
            if age > 60:
                senior_count += 1

        return senior_count