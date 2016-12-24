# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    
    return (N + 2) * (N + 1) / 2 - sum(A)
