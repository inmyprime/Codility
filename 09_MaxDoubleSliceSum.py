# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    max_ending = [0] * N
    max_ending_temp = 0
    for k in xrange(1,N-1):
        max_ending_temp = max(0, max_ending_temp + A[k])
        max_ending[k] = max_ending_temp
    
    max_starting = [0] * N
    max_starting_temp = 0
    for k in xrange(N-2,0,-1):
        max_starting_temp = max(0, max_starting_temp + A[k])
        max_starting[k] = max_starting_temp
    
    max_double_slice = 0
    for index in xrange(0, N-2):
        max_double_slice = max(max_double_slice, max_ending[index] + max_starting[index+2])
        
    return max_double_slice