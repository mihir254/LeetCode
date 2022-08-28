class Solution:
    def garbageCollection(self, garbage, travel) -> int:
        M, P, G = [0], [0], [0]
        for i in range(len(garbage)):
            if "M" in garbage[i]:
                M.append(i)
            if "P" in garbage[i]:
                P.append(i)
            if "G" in garbage[i]:
                G.append(i)
        travel.insert(0, 0)
        for i in range(1, len(travel)):
            travel[i] += travel[i-1]
        total_time = 0
        for i in range(1, len(M)):
            travel_time = travel[M[i]]-travel[M[i-1]]
            pickup_time = garbage[M[i]].count("M")
            total_time += travel_time + pickup_time
        for i in range(1, len(P)):
            travel_time = travel[P[i]]-travel[P[i-1]]
            pickup_time = garbage[P[i]].count("P")
            total_time += travel_time + pickup_time
        for i in range(1, len(G)):
            travel_time = travel[G[i]]-travel[G[i-1]]
            pickup_time = garbage[G[i]].count("G")
            total_time += travel_time + pickup_time
        return total_time