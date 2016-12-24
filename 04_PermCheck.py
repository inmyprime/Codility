# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    MAX = max(A)
    if MAX > N:
        return 0
        
    Count = [0] * N
    for i in A:
        Count[i-1] += 1
    for i in Count:
        if i != 1:
            return 0
    return 1