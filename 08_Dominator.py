# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    dominator = []
    N = len(A)
    size = 0
    for k in xrange(N):
        if size == 0:
            value = A[k]
            size += 1
        else:
            if value != A[k]:
                size -= 1
            else:
                size += 1
                
    if size == 0:
        return -1
        
    count = 0
    for k in xrange(N):
        if A[k] == value:
            if count == 0:
                dominator = k
            count += 1
    if count > N//2:
        return dominator
    return -1