class SeatManager:
    def __init__(self, n):
        self.available_seats = [i for i in range(1, n + 1)]
    def reserve(self):
        seat_number = heapq.heappop(self.available_seats)
        return seat_number
    def unreserve(self, seat_number):
        heapq.heappush(self.available_seats, seat_number)