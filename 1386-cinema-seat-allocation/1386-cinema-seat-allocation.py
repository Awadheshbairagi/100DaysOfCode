class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        cinemaSeats = {}
        leftAisle, rightAisle, middleAisle = 480, 30, 120
        
        for reserved in reservedSeats:
            row, col = reserved[0] - 1, reserved[1]
            if row not in cinemaSeats:
                cinemaSeats[row] = 0
            cinemaSeats[row] |= 1 << (10 - col)
        
        numFamilies = 0
        for row in cinemaSeats.values():
            row = ~(row) & ((1 << 10) - 1)
            if ((row & (leftAisle | rightAisle)) ^ (leftAisle | rightAisle)) == 0:
                numFamilies += 2
            elif ((row & leftAisle) ^ leftAisle) == 0 or ((row & rightAisle) ^ rightAisle) == 0 or ((row & middleAisle) ^ middleAisle) == 0:
                numFamilies += 1
        
        return numFamilies + 2 * (n - len(cinemaSeats))
