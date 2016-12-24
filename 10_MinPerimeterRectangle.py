# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # write your code in Python 2.7
    i = 1
    largest = 1
    while (i*i <= N):
        if (N%i == 0):
            largest = i
        i += 1
    
    return 2 * (largest + N//largest)