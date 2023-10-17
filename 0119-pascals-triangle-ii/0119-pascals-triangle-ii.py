from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]  # The first element is always 1
        for i in range(1, rowIndex + 1):
            # Generate the next row using the previous row
            new_row = [1]  # First element of the new row
            for j in range(1, len(row)):
                new_row.append(row[j - 1] + row[j])
            new_row.append(1)  # Last element of the new row
            row = new_row  # Update the row for the next iteration
        return row
