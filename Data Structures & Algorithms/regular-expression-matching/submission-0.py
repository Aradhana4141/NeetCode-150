#Brute Force: using Recursion 

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def dfs(i,j):
            if j >= len(p):
                if i >= len(s):
                    return True
                else: return False

#case1 : both char equal or p has '.' /  # Check current character
            if i < len(s):
                if s[i]==p[j] or p[j]=='.':
                    match=True
                else:match=False
            else:match =False    
#case2: if p has "*" then 2 possiblities  1. we have to keep a char in p 2.keep j on same char

            if j+1<len(p) and p[j+1]=="*":
                return (
                dfs(i,j+2)  # Choice 1: Skip current character and *
                or 
                (match and dfs(i+1,j))  # Choice 2: Match one character and stay 
            )
            return match and dfs(i+1,j+1)  # Normal matching(str with no . ,*)
        return dfs(0,0)

