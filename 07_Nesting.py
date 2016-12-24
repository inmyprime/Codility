# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(S):
    # write your code in Python 2.7
    N = len(S)
    if N == 0:
        return 1
    if N%2 != 0:
        return 0
    size = 0
    for i in range(0,N):
        if S[i] == '(':
            size += 1
        else:
            size -= 1
        if size < 0:
            return 0
    if size == 0:
        return 1
    else:
        return 0