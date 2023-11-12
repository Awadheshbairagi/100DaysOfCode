from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        stop_to_routes = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        visited_routes = set()
        visited_stops = set()
        queue = deque([(source, 0)])

        while queue:
            current_stop, buses_taken = queue.popleft()

            for route_index in stop_to_routes[current_stop]:
                if route_index in visited_routes:
                    continue

                visited_routes.add(route_index)

                for next_stop in routes[route_index]:
                    if next_stop in visited_stops:
                        continue

                    visited_stops.add(next_stop)

                    if next_stop == target:
                        return buses_taken + 1

                    queue.append((next_stop, buses_taken + 1))

        return -1

