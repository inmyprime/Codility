# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    if N < 2:
        return 0
        
    max_price = A[N-1]
    max_profit = 0
    for k in xrange(N-2,-1,-1):
        max_profit = max(max_profit, max_price - A[k])
        max_price = max(max_price, A[k])
    return max_profit