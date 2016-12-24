# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    leader, total_count = goldenLeader(A)
    if leader == -1:
        return 0
    N = len(A)
    equi_count = 0
    count = 0
    for k in xrange(N):
        if (A[k] == leader):
            count += 1
        if count > (k+1) // 2 and (total_count - count) > (N-k-1)//2:
            equi_count += 1
    return equi_count
        

def goldenLeader(A):
    n = len(A)
    size = 0
    for k in xrange(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1
    candidate = -1
    if (size > 0):
        candidate = value
    leader = -1
    count = 0
    for k in xrange(n):
        if (A[k] == candidate):
            count += 1
    if (count > n // 2):
            leader = candidate
    return leader, count