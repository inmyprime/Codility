# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # write your code in Python 2.7
    i = 1
    count = 0
    while (i*i < N):
        if (N%i == 0):
            count += 2
        i += 1
    if (i*i == N):
        count += 1
    
    return count