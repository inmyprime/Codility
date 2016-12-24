# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    A.sort()
    N = len(A)
    if N < 3:
        return 0
    for i in range(0,N-2):
        if A[i] + A[i+1] > A[i+2] and A[i] + A[i+2] > A[i+1] and A[i+2] + A[i+1] > A[i]:
            return 1
    
    return 0