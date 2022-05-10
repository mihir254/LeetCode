class Solution:
    def combinationSum3(self, k: int, n: int):
        res = []
        self.recursion(res, k, n, 1, [])
        return res
    def recursion(self, ans, size, goal, current_index, current_set):
        if current_index == size+1:
            if sum(current_set)==goal:
                ans.append(current_set)
            return
        else:
            x = 1 if current_set == [] else current_set[-1]+1
            for i in range(x, 10):
                self.recursion(ans, size, goal, current_index+1, current_set+[i])