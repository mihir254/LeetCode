class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # Attempt 6: For each box, instead of calculating sum of N elements, we can use a sliding window.
        #            This window will keep on shifting to the right and we will remove an element when K >= N.
        #            It's difficult to see this without drawing the solution, so, a lesson learnt.
        prev = [0] * (k + 1)
        prev[0] = 1
        for N in range(1, n + 1):
            cur = [0] * (k + 1)
            addition = 0
            for K in range(k + 1):
                if K >= N:
                    addition -= prev[K - N]
                addition = (addition + prev[K]) % MOD
                cur[K] = addition
            prev = cur
        return prev[k] % MOD

        # Attempt 5: Optimized traditional Bottom-Up by freeing up space that is no longer of importance
        prev = [0] * (k + 1)
        prev[0] = 1
        for N in range(1, n + 1):
            cur = [0] * (k + 1)
            for K in range(k + 1):
                for ip in range(N):
                    if (K - ip) >= 0:
                        cur[K] += (prev[K - ip] % MOD)
            prev = cur
        return prev[k] % MOD

        # Attempt 4: Since Top-Down was exceeding time limit, used Bottom-Up, which only visits 1 level before the current level
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for N in range(1, n + 1):
            for K in range(k + 1):
                for ip in range(N):
                    if (K - ip) >= 0:
                        dp[N][K] += (dp[N - 1][K - ip] % MOD)
        return dp[n][k] % MOD

        # Attempt 3: Optimized by storing the number of valid combinations we could generate with n numbers and k inverse pairs
        cache = {} # (n, k) -> how many inverse pairs I can generate from there
        def recursion(N, K):
            if K < 0:
                return 0
            if N == 0 and K == 0:
                return 1
            if (N, K) in cache:
                return cache[(N, K)]
            cache[(N, K)] = 0
            for i in range(N):
                if (K - i) >= 0:
                    cache[(N, K)] += (recursion(N-1, K-i) % MOD)
            return cache[(N, K)] % MOD
        return recursion(n, k)

        # Attempt 2: Better way of visiting all combinations
        def recursion(N, K):
            if K < 0:
                return 0
            if N == 0 and K == 0:
                return 1
            res = 0
            for i in range(N):
                if (K - i) >= 0:
                    res += (recursion(N-1, K-i) % MOD)
            return res
        return recursion(n, k) % MOD

        # Attempt 1: Visit all valid combinations
        self.count = 0
        self.combinations([i for i in range(1, n+1)], [], k)
        return self.count % (10**9 + 7)

    def combinations(self, arr, cur, k):
        if k == 0 and not arr:
            self.count += 1
            return
        if k < 0 or not arr:
            return
        for i in range(len(arr)):
            lessOnLeft = 0
            for j in range(len(cur)):
                if cur[j] < arr[i]:
                    lessOnLeft += 1
            lessOnRight = arr[i] - lessOnLeft - 1
            self.combinations(arr[:i] + arr[i+1:], cur+[arr[i]], k - lessOnRight)