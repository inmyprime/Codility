# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    # write your code in Python 2.7
    covered = [False]*X
    uncovered = X
    for i in xrange(len(A)):
        if covered[A[i]-1] == False:
            covered[A[i]-1] = True;
            uncovered -= 1
            if uncovered == 0:
                return i
    
    return -1