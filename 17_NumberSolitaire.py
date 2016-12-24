# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    MAX_INT = 100000000000
    dp = [A[0]] + [-MAX_INT]*(N-1)
 
    for j in xrange(1, N):
        for K in range(1,7):
            if (j - K >= 0):
                dp[j] = max(dp[j], dp[j-K] + A[j])
 
    return dp[-1]