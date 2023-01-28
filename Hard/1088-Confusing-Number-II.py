class Solution:
    # def confusingNumberII(self, n: int) -> int:
    #     answer = 0
    #     store = {
    #         0:0, 1:1, 6:9, 8:8, 9:6
    #     }
    #     for number in range(1, n+1):
    #         if self.valid(number, store):
    #             answer += 1
    #     return answer
    # def valid(self, number, store):
    #     origin = number
    #     new = 0
    #     while number > 0:
    #         last = number%10
    #         if last in store:
    #             new = new*10 + store[last]
    #             number -= last
    #             number //= 10
    #         else:
    #             return False
    #     if new != origin:
    #         return True
    #     else:
    #         return False
    def confusingNumberII(self, n):
        store = {0:0,1:1,6:9,8:8,9:6}
        self.answer = 0
        self.helper(0, 0, 0, n, store)
        return self.answer
    def helper(self, origin, new, newx, n, store):
        if origin != new:
            self.answer += 1
        for key, value in store.items():
            if origin==0 and key==0:
                continue
            if origin*10 + key > n:
                break
            self.helper(origin*10 + key, int(str(newx*10 + value)[::-1]), newx*10+value, n, store)