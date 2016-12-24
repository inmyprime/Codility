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
    stack = [0]*N
    for i in range(0,N):
        if S[i] == '(' or S[i] == '[' or S[i] == '{':
            stack[size] = S[i]
            size += 1
        elif S[i] == ')':
            if size > 0 and stack[size-1] == '(':
                size -= 1
            else:
                return 0
        elif S[i] == ']':
            if size > 0 and stack[size-1] == '[':
                size -= 1
            else:
                return 0
        elif S[i] == '}':
            if size > 0 and stack[size-1] == '{':
                size -= 1
            else:
                return 0
        
    if size == 0:
        return 1
    else:
        return 0