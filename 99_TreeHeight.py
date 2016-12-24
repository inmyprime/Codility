# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(T):
    # write your code in Python 2.7
    if T.l == None and T.r == None:
        return 0
    elif T.l == None:
        return 1 + solution(T.r)
    elif T.r == None:
        return 1 + solution(T.l)
    else:
        return 1 + max(solution(T.l), solution(T.r))