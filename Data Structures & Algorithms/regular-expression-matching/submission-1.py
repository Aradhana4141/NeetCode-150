#Optimize solution: using DP(Memo)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        m = len(s)
        n = len(p)

        dp = [[-1 for _ in range(n+1)] for _ in range(m+1)]

        def dfs(i, j):

            # Base case
            if j == n:
                if i == m:
                    return True
                else:
                    return False

            # Check DP
            if dp[i][j] != -1:
                return dp[i][j]

            # Check current character
            if i < m:
                if s[i] == p[j] or p[j] == '.':
                    match = True
                else:
                    match = False
            else:
                match = False

            # If next character is *
            if j + 1 < n and p[j+1] == '*':

                # Choice 1: Skip
                # Choice 2: Match one and stay
                result = (
                    dfs(i, j+2) or
                    (match and dfs(i+1, j))
                )

            else:
                # Normal matching
                result = match and dfs(i+1, j+1)

            dp[i][j] = result

            return dp[i][j]

        return dfs(0, 0)
