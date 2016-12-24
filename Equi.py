# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    prefix = [0] * (N + 1)
    for k in xrange(1, N + 1):
        prefix[k] = prefix[k - 1] + A[k - 1]
    
    total_sum = prefix[-1]
    for P in xrange(0, N):
        former_sum = prefix[P+1] - A[P]
        latter_sum = total_sum - former_sum - A[P]
        if former_sum == latter_sum:
            return P
    return -1