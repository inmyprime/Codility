# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    count = 0
    upper = [0]*N
    lower = [0]*N
    for i in range(0,N):
        upper[i] = i+A[i]
        lower[i] = i-A[i]
    
    upper.sort()
    lower.sort()
    
    lower_index = 0
    for upper_index in range(0,N):
        while lower_index < N and lower[lower_index] <= upper[upper_index]:
            lower_index += 1
        count += lower_index - upper_index -1
        if count > 10000000:
            return -1
    
    return count