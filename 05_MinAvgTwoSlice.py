# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    min_value = (A[0] + A[1])/2.0
    min_pos = 0
    for i in range(0,N-2):
        if (A[i] + A[i+1])/2.0 < min_value:
            min_value = (A[i] + A[i+1])/2.0
            min_pos = i    
        if (A[i] + A[i+1] + A[i+2])/3.0 < min_value:
            min_value = (A[i] + A[i+1] + A[i+2])/3.0
            min_pos = i
    
    if (A[N-2] + A[N-1])/2.0 < min_value:
        min_value = (A[N-2] + A[N-1])/2.0
        min_pos = N-2
    
    return min_pos