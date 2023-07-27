class Solution:
    def numBusesToDestination(self, routes, source: int, target: int) -> int:
        if source == target:
            return 0
        graph = {}
        for bus in range(len(routes)):
            stops = routes[bus]
            for stop in stops:
                if stop not in graph:
                    graph[stop] = []
                graph[stop].append(bus)
        visited = set()
        queue = [source]
        busesTaken = 0
        while queue:
            busesTaken += 1
            for i in range(len(queue)):
                prevStop = queue.pop(0)
                for bus in graph[prevStop]:
                    if bus not in visited:
                        visited.add(bus)
                        for stop in routes[bus]:
                            if stop == target:
                                return busesTaken
                            queue.append(stop)
        return -1