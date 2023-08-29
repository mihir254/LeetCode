class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ys, ns = 0, 0
        for customer in customers:
            if customer == "Y":
                ys += 1
            else:
                ns += 1
        mini = len(customers)
        yd, nd = 0, 0
        ind = -1
        for i in range(len(customers) + 1):
            penalty = (ys - yd) + nd
            if penalty < mini:
                mini = penalty
                ind = i
            if i < len(customers):
                if customers[i] == "Y":
                    yd += 1
                else:
                    nd += 1
        return ind if ind != -1 else len(customers)