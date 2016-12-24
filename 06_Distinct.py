# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    A.sort()
    N = len(A)
    if N == 0:
        return 0
    count = 1
    for i in range(1,len(A)):
        if A[i] != A[i-1]:
            count += 1
    return count