# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    P = prefix_sums(A)
    count = 0
    for index in xrange(N):
        if A[index] == 0:
            countOne = count_total(P, index+1, N-1)
            count += countOne
            if count > 1000000000:
                return -1
    
    return count
    
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in xrange(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def count_total(P, x, y):
    return P[y + 1] - P[x]